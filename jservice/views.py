from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

from .serializers import RandomQuestionSerializer
from .models import RandomQuestion

import requests
from typing import List, Dict, Tuple

# Create your views here.


class RandomQuestionAPIView(APIView):

    # Получить рандомный вопрос-ответ с внешнего API
    def get_random_question(self, param: int) -> Dict:
        url = f'https://jservice.io/api/random?count={param}'
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

        return {"status_code": response.status_code}

    # Распределение ответа от jservice.io на существующие и несуществующие вопросы в нашей БД.
    # где count - кол-во уже существующих вопросов в нашей БД.
    def have_exist_questions(self, existing_ids: List, pending_ids: List) -> Tuple[int, List, List]:
        count = 0
        exist_ids = []
        not_exist_ids = []
        for item in existing_ids:
            if item in pending_ids:
                count += 1
                exist_ids.append(item)
            else:
                not_exist_ids.append(item)

        return count, exist_ids, not_exist_ids

    def get_pending_ids(self, data: Dict) -> List:  # list of json
        pending_ids = []
        for elem in data:
            pending_ids.append(elem.get("id", None))
        return pending_ids

    def post(self, request):
        count = None
        exist_ids = None
        param = request.POST.get('count', None)

        if param is None or not param:
            return JsonResponse({"error input": "parameter 'count' not given"})

        all_existing_ids = list(RandomQuestion.objects.values_list("question_id", flat=True))
        external_data = self.get_random_question(param=param)

        if "status_code" in external_data:
            return JsonResponse({"error_connect": external_data})

        serializer = RandomQuestionSerializer(data=external_data, many=True)
        serializer.is_valid(raise_exception=True)

        pending_ids = self.get_pending_ids(serializer.data)
        count, exist_ids, not_exist_ids = self.have_exist_questions(all_existing_ids, pending_ids)

        new_questions = [*[elem for elem in external_data if elem["id"] in not_exist_ids]]

        while count != 0:
            external_data = self.get_random_question(param=count)
            pending_ids = self.get_pending_ids(external_data)
            _, exist_ids, not_exist_ids = self.have_exist_questions(all_existing_ids,
                                                                    pending_ids)
            if bool(not_exist_ids):
                pack = [elem for elem in external_data if elem["id"] in not_exist_ids]
                new_questions.append(*pack[:])
                count -= len(pack)
        try:
            last_question = RandomQuestion.objects.latest('id')
            last_question = RandomQuestion.to_dict(last_question)
        except RandomQuestion.DoesNotExist:
            last_question = {None}

        if bool(new_questions):
            serializer = RandomQuestionSerializer(data=new_questions, many=True)

            if serializer.is_valid(raise_exception=True):
                serializer.create(serializer.data)
        else:
            serializer.create(serializer.data)

        return Response(last_question)

from django.contrib.sites import requests
from rest_framework import serializers
from .models import RandomQuestion


class RandomQuestionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('question_id')
        self.fields['id'].source = "question_id"

    def create(self, validated_data):
        question_id = validated_data.pop('id')
        question = validated_data.pop('question')
        created_at = validated_data.pop('created_at')
        answer = validated_data.pop('answer')

        random_question = RandomQuestion.objects.create(question_id=question_id,
                                                        question=question,
                                                        created_at=created_at,
                                                        answer=answer)
        return random_question

    class Meta:
        model = RandomQuestion
        fields = ('__all__')

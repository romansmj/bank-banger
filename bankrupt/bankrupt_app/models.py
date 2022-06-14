from django.db import models

# Create your models here.


question_types = (
    ("optional", "optional"),
    ("handwritten", "handwritten")
)

class Questions(models.Model):
    question = models.CharField(max_length=300)
    type = models.CharField(max_length=20, choices=question_types, default="optional")


    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ["-id"]

class Answers(models.Model):
    question_id = models.IntegerField()
    answer = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ["-question_id"]
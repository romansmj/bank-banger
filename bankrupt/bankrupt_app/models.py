from django.db import models

# Create your models here.


question_types = (
    ("OP", "Опционально"),
    ("HW", "Вручную")
)

class Questions(models.Model):
    question = models.TextField(max_length=300, default="")
    type = models.CharField(max_length=2, choices=question_types, default="OP")


    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ["-id"]

class Answers(models.Model):
    question_id = models.IntegerField()
    answer = models.TextField(max_length=300, default="")

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ["-question_id"]

calls_status = (
    ("N", "Новый"),
    ("CF", "Звонок не состоялся"),
    ("CS", "Звонок состоялся"),
)

class Calls(models.Model):
    name = models.CharField(max_length=300, unique=False, null=True, blank=True)
    phone = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=2, choices=calls_status, default="N")
    comment = models.TextField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Звонок'
        verbose_name_plural = 'Звонки'
        # ordering = ["-status", "-created_at", "-updated_at"]

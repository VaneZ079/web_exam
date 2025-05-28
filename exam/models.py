from django.db import models
from django.contrib.auth.models import User

class Izexam(models.Model):
    title = models.CharField("Название экзамена", max_length=200)
    create_date = models.DateTimeField("Дата создания", auto_now_add=True)
    exam_date = models.DateField("Дата проведения экзамена")
    image = models.ImageField("Изображение задания", upload_to='images/')
    write_users = models.ManyToManyField(User, verbose_name="Участники экзамена")
    is_public = models.BooleanField("Опубликовано", default=False)

    def __str__(self):
        return self.title

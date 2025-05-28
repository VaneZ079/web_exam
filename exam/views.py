# exam/views.py
from django.shortcuts import render
from .models import Izexam

def exham_list(request):
    # Получаем только опубликованные записи
    exams = Izexam.objects.filter(is_public=True)

    context = {
        'fio': 'Злыгостев Иван Дмитриевич',  # Замените на своё ФИО
        'group_number': 'Группа 241-671',   # Замените на номер группы
        'exams': exams,
    }
    return render(request, 'exam/exham_list.html', context)

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import MyModelFirst
from .forms import SurveyForm

# Create your views here.
def qest(request: HttpRequest):
    if request.method == 'GET':
        # Получим случайную запись с полем Garbage=None
        random_data = MyModelFirst.objects.filter(Garbage=None).order_by('?').first()
        # Проверка, что такие данные были найдены
        if random_data:
            print("Я нашёл объект: " + str(random_data.id))
            # Создаем форму на основе данных из случайной записи
            form = SurveyForm(initial={
                'id': random_data.id,  # Передаем id запись в форму
            })
            context = {
                'form': form,
                "random_data":random_data,
            }
            return render(request, 'labeling/index.html', context=context)
        else:
            return HttpResponse("Больше данных для разметки нет!")
        
    elif request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            data_id = form.cleaned_data['id']  # Получаем id из формы
            form.save(data_id) # Обновляем запись с указанным id
            print("Сохранил объект:" + str(data_id))
            return redirect('labeling:qest')  # Перенаправляем на страницу успеха или куда вам нужно
        else:
            data_id = form.cleaned_data['id']  # Получаем id из формы
            random_data = MyModelFirst.objects.get(id=data_id)
            context = {
            'form': form,
            "random_data":random_data,
        }
            return render(request, 'labeling/index.html', context=context)
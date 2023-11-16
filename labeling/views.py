from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import MyModelFirst, Profile
from .forms import SurveyForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView


def register_view(request: HttpRequest):
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        print(5)
        if form.is_valid():
            print(6)
            form.save()
            username = form.cleaned_data.get("username")
            raw_pas = form.cleaned_data.get("password2")
            user = authenticate(username=username, password=raw_pas)
            login(request, user)
            return redirect('labeling:qest')
    else:
        form = RegisterForm()
    return render(request, 'labeling/register.html', {'form': form})

def login_view(request: HttpRequest):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('labeling:qest')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'labeling/login.html', {'form': form})

def logout_view(request: HttpRequest):
    logout(request)
    return redirect('labeling:login')

def qest(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect('labeling:login')
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
            return render(request, 'labeling/main.html', context=context)
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
            return render(request, 'labeling/main.html', context=context)
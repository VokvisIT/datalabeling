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
    profile = request.user.profile
    if request.method == 'GET':
        random_data = MyModelFirst.objects.filter(Garbage=None).order_by('?').first()
        if random_data:
            form = SurveyForm(initial={
                'id': random_data.id,
            })
            context = {
                'profile': profile,
                'form': form,
                "random_data":random_data,
            }
            return render(request, 'labeling/main.html', context=context)
        else:
            return HttpResponse("Больше данных для разметки нет!")
        
    elif request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            data_id = form.cleaned_data['id'] 
            form.save(data_id)
            profile.increment_count_task()
            # Получаем объект по data_id
            obj = MyModelFirst.objects.get(id=data_id)
            print(obj)
            # Проверяем тип объекта
            if obj.Type == 'Комментарий' and (form.cleaned_data['Garbage']):  # Замените 'type' на реальное поле, обозначающее тип объекта
                selected_emotion = form.cleaned_data['selected_emotion']
                Pos = selected_emotion == 'Positive'
                Neg = selected_emotion == 'Negative'
                post_obj = MyModelFirst.objects.filter(Text=obj.Text, Type='Пост').first()
                print(post_obj)
                if Pos:
                    post_obj.plus_count_ton()
                elif Neg:
                    post_obj.minus_count_ton()

            return redirect('labeling:qest') 
        else:
            data_id = form.cleaned_data['id']
            random_data = MyModelFirst.objects.get(id=data_id)
            context = {
            'profile': profile,
            'form': form,
            "random_data":random_data,
        }
            return render(request, 'labeling/main.html', context=context)
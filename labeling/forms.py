from django import forms
from .models import MyModelFirst, Profile
from django.core.exceptions import ValidationError
from django.forms.widgets import Select
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class SurveyForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    Garbage = forms.NullBooleanField(
        widget=Select(choices=[(True, 'Да'), (False, 'Нет')]),
        required=True,
        label="Мусор",
        initial=False
    )
    Healthcare = forms.BooleanField(required=False, label="Здравоохранение")
    Housing_and_Public_Utilities = forms.BooleanField(required=False, label="ЖКХ")
    Education = forms.BooleanField(required=False, label="Образование")
    Infrastructure = forms.BooleanField(required=False, label="Инфраструктура")
    Culture = forms.BooleanField(required=False, label="Культура")
    Environmental_Conditions = forms.BooleanField(required=False, label="Экология")
    Social_Security = forms.BooleanField(required=False, label="Социальное обеспечение")
    Politics = forms.BooleanField(required=False, label="Политика")
    Safety = forms.BooleanField(required=False, label="Безопасность")
    Availability_of_Goods_and_Services = forms.BooleanField(required=False, label="Доступность товаров и услуг")
    Official_Statements = forms.BooleanField(required=False, label="Официальные заявления")
    Tourism = forms.BooleanField(required=False, label="Туризм")
    Facts = forms.BooleanField(required=False, label="Факты")
    Positive = forms.BooleanField(required=False, label="Позитивная")
    Negative = forms.BooleanField(required=False, label="Негативная")
    Neutral = forms.BooleanField(required=False, label="Нейтральная")

    def clean(self):
        cleaned_data = super().clean()
        Garbage = bool(cleaned_data['Garbage'])
        Positive = cleaned_data['Positive']
        Negative = cleaned_data['Negative']
        Neutral = cleaned_data['Neutral']
        print(Positive, Negative, Neutral)
        print(Garbage, type(Garbage))
        if Garbage:
            # Если Garbage равно True, устанавливаем все булевые поля на False
            for field_name in ['Healthcare', 'Housing_and_Public_Utilities', 'Education', 'Infrastructure',
                               'Culture', 'Environmental_Conditions', 'Social_Security', 'Politics',
                               'Safety', 'Availability_of_Goods_and_Services', 'Official_Statements', 'Tourism', 'Facts','Positive','Negative', 'Neutral']:
                cleaned_data[field_name] = False
            print("1 Условие выполнено")
        else:
            # Если Garbage равно False, проверяем, что хотя бы одно из Positive, Negative или Neutral выбрано
            if not (Positive or Negative or Neutral):
                print("2 Условие выполнено")
                raise forms.ValidationError("Выберите хотя бы одно из полей Positive, Negative или Neutral.")
            # Проверка, что ни одно из полей от Healthcare до Facts не выбрано
            if not any([
                cleaned_data[field_name]
                for field_name in ['Healthcare', 'Housing_and_Public_Utilities', 'Education', 'Infrastructure',
                                  'Culture', 'Environmental_Conditions', 'Social_Security', 'Politics',
                                  'Safety', 'Availability_of_Goods_and_Services', 'Official_Statements', 'Tourism', 'Facts']
            ]):
                # Если ни одно из полей от Healthcare до Facts не выбрано, устанавливаем Garbage в True
                cleaned_data['Garbage'] = True
                print("3 Условие выполнено")
        print(cleaned_data)

    def save(self, id):
        instance = MyModelFirst.objects.get(id=id)
        instance.Garbage = self.cleaned_data['Garbage']
        instance.Healthcare = self.cleaned_data['Healthcare']
        instance.Housing_and_Public_Utilities = self.cleaned_data['Housing_and_Public_Utilities']
        instance.Education = self.cleaned_data['Education']
        instance.Infrastructure = self.cleaned_data['Infrastructure']
        instance.Culture = self.cleaned_data['Culture']
        instance.Environmental_Conditions = self.cleaned_data['Environmental_Conditions']
        instance.Social_Security = self.cleaned_data['Social_Security']
        instance.Politics = self.cleaned_data['Politics']
        instance.Safety = self.cleaned_data['Safety']
        instance.Availability_of_Goods_and_Services = self.cleaned_data['Availability_of_Goods_and_Services']
        instance.Official_Statements = self.cleaned_data['Official_Statements']
        instance.Tourism = self.cleaned_data['Tourism']
        instance.Facts = self.cleaned_data['Facts']
        instance.Positive = self.cleaned_data['Positive']
        instance.Negative = self.cleaned_data['Negative']
        instance.Neutral = self.cleaned_data['Neutral']
        
        instance.save()

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(label="Введите пароль", widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    class Meta:
        model = User  # Используйте вашу модель Profile
        fields = ['username', 'password']

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='username', min_length=5, max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Введите ваш username'}))
    first_name = forms.CharField(label='first_name', min_length=4, max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}))
    last_name = forms.CharField(label='last_name', min_length=4, max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Введите вашу фамилию'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Введите вашу корп. почту'}))
    group_number = forms.CharField(required=True, max_length=6, widget=forms.TextInput(attrs={'placeholder': 'Введите ваш номер группы'}))
    password1 = forms.CharField(label="Введите пароль", widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'group_number', 'email','password1', 'password2']

    def clean_username(self):
        cleaned_data = super().clean()
        username = cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("Пользователь уже существует")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError("Email уже существует")
        return email
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name'].lower()
        return last_name.capitalize()

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name'].lower()
        return first_name.capitalize()

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают")
        return password2

    def save(self):  # исправлен метод save
        print(self.cleaned_data)
        username = self.cleaned_data['username']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        raw_password = self.cleaned_data['password1']
        group_number = self.cleaned_data['group_number']
        user = Profile.register(
            username=username,
            first_name=first_name,
            last_name = last_name,
            email=email,
            password=raw_password,
            group_number=group_number,
        )
        return user
        
    
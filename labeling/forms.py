
from django import forms
from .models import MyModelFirst, Profile
from django.core.exceptions import ValidationError
from django.forms.widgets import Select
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
class SurveyForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    type_text = forms.CharField(widget=forms.HiddenInput(), required=False)
    Garbage = forms.NullBooleanField(
        widget=Select(choices=[(True, 'Да'), (False, 'Нет')]),
        required=True,
        label="Мусор",
        initial=False
    )
    CHOICES_Tonality = [
        ('Positive', 'Позитивная'),
        ('Negative', 'Негативная'),
        ('Neutral', 'Нейтральная'),
    ]
    CHOICES = [
        ('Healthcare', 'Здравоохранение'),
        ('Housing_and_Public_Utilities', 'ЖКХ'),
        ('Education', 'Образование'),
        ('Infrastructure', 'Инфраструктура'),
        ('Culture', 'Культура'),
        ('Environmental_Conditions', 'Экология'),
        ('Social_Security', 'Социальное обеспечение'),
        ('Politics', 'Политика'),
        ('Safety', 'Безопасность'),
        ('Availability_of_Goods_and_Services', 'Доступность товаров и услуг'),
        ('Official_Statements', 'Официальные заявления'),
        ('Tourism', 'Туризм'),
        ('Facts', 'Факты'),
        ('Another', "Другое..."), # Пустой элемент
    ]
    selected_field = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-selected_field'}))
    selected_emotion = forms.ChoiceField(
        choices=CHOICES_Tonality,
        widget=forms.RadioSelect(attrs={'class': 'form-selected_emotion'}),
        label='Выберите эмоцию',
        required=False,
    )

    def clean(self):
        cleaned_data = super().clean()
        Garbage = bool(cleaned_data['Garbage'])
        type_text = cleaned_data['type_text']
        selected_field = cleaned_data['selected_field']
        selected_emotion = self.cleaned_data['selected_emotion']
        text_garbage = selected_field == 'Another'
        Positive = selected_emotion == 'Positive'
        Negative = selected_emotion == 'Negative'
        Neutral = selected_emotion == 'Neutral'
        if type_text == 'Пост':
            if not Garbage:
                if not (Positive or Negative or Neutral):
                    self.add_error('selected_emotion', "Выберите тональность.")
                if text_garbage:
                    cleaned_data['Garbage'] = True
        else:
            if Garbage:
                if not (Positive or Negative or Neutral):
                    self.add_error('selected_emotion', "Нам пригодится тональность этого комментария.")
            else:
                if not (Positive or Negative or Neutral):
                    self.add_error('selected_emotion', "Нам пригодится тональность этого комментария.")
                if text_garbage:
                    cleaned_data['Garbage'] = True

    def save(self, id):
        instance = MyModelFirst.objects.get(id=id)
        selected_field = self.cleaned_data['selected_field']
        selected_emotion = self.cleaned_data['selected_emotion']
        instance.Garbage = self.cleaned_data['Garbage']
        instance.Healthcare = selected_field == 'Healthcare'
        instance.Housing_and_Public_Utilities = selected_field == 'Housing_and_Public_Utilities'
        instance.Education = selected_field == 'Education'
        instance.Infrastructure = selected_field == 'Infrastructure'
        instance.Culture = selected_field == 'Culture'
        instance.Environmental_Conditions = selected_field == 'Environmental_Conditions'
        instance.Social_Security = selected_field == 'Social_Security'
        instance.Politics = selected_field == 'Politics'
        instance.Safety = selected_field == 'Safety'
        instance.Availability_of_Goods_and_Services = selected_field == 'Availability_of_Goods_and_Services'
        instance.Official_Statements = selected_field == 'Official_Statements'
        instance.Tourism =  selected_field == 'Tourism'
        instance.Facts = selected_field == 'Facts'
        instance.Positive = selected_emotion == 'Positive'
        instance.Negative = selected_emotion == 'Negative'
        instance.Neutral =  selected_emotion == 'Neutral'
        print('Save')
        print(id)
        instance.save()

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='username',
        widget=forms.TextInput(attrs={'placeholder': 'username'}),
        )
    password = forms.CharField(
        label="Введите пароль",
        widget=forms.PasswordInput(attrs={'placeholder': 'password'}),
        )
    error_messages = {
        'invalid_login': _(
            "Пожалуйста проверьте username и password. Убедитесь, что вы ввели их корректно."
        ),
        'inactive': _("This account is inactive."),
    }
    class Meta:
        model = User  # Используйте вашу модель Profile
        fields = ['username', 'password']

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='username', min_length=3, max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Введите ваш username'}))
    first_name = forms.CharField(label='first_name',  max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}))
    last_name = forms.CharField(label='last_name',  max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Введите вашу фамилию'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Введите вашу корп. почту'}))
    group_number = forms.CharField(required=True, max_length=6, widget=forms.TextInput(attrs={'placeholder': 'Введите номер группы'}))
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
            raise ValidationError("Данный username уже занят!")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError("Почта уже занята!")
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
            raise ValidationError("Пароли не совпадают!")
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
        
    
from django import forms
from .models import MyModelFirst  # Замените YourModel на имя вашей модели
from django.core.exceptions import ValidationError
from django.forms.widgets import Select

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

"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class NotebookFilterForm(forms.Form):
    CHOICESt = (
        ('',''),
        ('Ноутбук', 'Ноутбук'),
        ('Нетбук', 'Нетбук'),
        ('Ультрабук', 'Ультрабук'),
    )    
    CHOICES = (
        ('',''),
        ('Исправен', 'Исправен'),
        ('Не исправен', 'Не исправен'),
    )
    num_audience = forms.IntegerField(label="Аудитория", required=False)
    num_brand = forms.CharField(label="Бренд", required=False)
    num_model = forms.CharField(label="Модель", required=False)
    num_type = forms.ChoiceField(label="Тип", required=False, choices=CHOICESt)
    num_gpu = forms.ChoiceField(label="Процессор", required=False)
    num_ram = forms.IntegerField(label="Объем ОЗУ, ГБ", required=False, min_value=1)
    num_state = forms.ChoiceField(label="Состояние", required=False, choices=CHOICES)
    num_term = forms.IntegerField(label="Срок амортизации, года", required=False, min_value=1)

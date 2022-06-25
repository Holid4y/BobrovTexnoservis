from .models import message
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput

class messageForm(ModelForm):
    class Meta:
        model = message
        fields = ['FirstName', 'Phone', 'Email', 'Message', 'Checkbox']
        widgets = {
            'FirstName': TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Имя',
                'type':'Firstname'
            }),
            'Phone': TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Телефон',
                'type':'tel'
            }),
            'Email': TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'E-mail',
                'type':'email'
            }),
            'Message': Textarea(attrs={
                'class': 'form-control mb-3',
                'cols': '30',
                'rows': '3',
                'placeholder': 'Сообщение'
            }),
            'Checkbox': CheckboxInput(attrs={
                'class': 'form-check-input',
                'type': 'checkbox',
                'id': 'exampleCheck1'
            })
        }
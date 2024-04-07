from django import forms

options = [
    ('low','low'),
    ('medium','medium'),
    ('higth','higth'),
]

class Contact(forms.Form):
    first_name = forms.CharField(label="Nombre",
                                 max_length=50,
                                 widget=forms.TextInput(attrs={'class': 'input'}),) #da la clase al formulario
    last_name = forms.CharField(label="Apellidos",
                                max_length=50,
                                widget=forms.TextInput(attrs={'class': 'input'}),)
    message = forms.CharField(label='Mensaje',
                              max_length=100,
                              widget=forms.TextInput(attrs={'class': 'input'}),)
    subject = forms.CharField(label='Asunto',
                              max_length=100,
                              widget=forms.TextInput(attrs={'class': 'input'}),)
    importance = forms.ChoiceField(choices=options,
                                   widget=forms.Select(attrs={'class': 'select'}))
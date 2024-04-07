from django import forms


class Formulario1(forms.Form):
    tipo = forms.CharField(label='Tipo de documento',
                           max_length=2,
                           widget=forms.TextInput(attrs={'class': 'input'}))
    
class Formulario2(forms.Form):
    nombre = forms.CharField(label='Nombre',
                             max_length=10,
                             widget=forms.TextInput(attrs={'class': 'input'}))
    apellido = forms.CharField(label='Apellido',
                               max_length=10,
                               widget=forms.TextInput(attrs={'class': 'input'}))
    correo = forms.EmailField(label='Correo electronico',
                              max_length=100,
                              widget=forms.TextInput(attrs={'class': 'input'}))
    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento',
                                       widget=forms.TextInput(attrs={'class': 'input', 'type': 'date'}))
    tipo_documento = forms.CharField(label='Tipo de documento',
                                     max_length=2,
                                     widget=forms.TextInput(attrs={'class': 'input'}))
    
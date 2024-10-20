from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    widget = {
        'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        'apellido': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.TextInput(attrs={'class': 'form-control'}),
        'message': forms.Textarea(attrs={'class': 'form-control'})
    }
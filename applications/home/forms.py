from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Nombre y Apellido'}))
    email = forms.CharField(max_length=50,widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    mensaje = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'placeholder': 'Mensaje'}))

    class Meta:
        fields = (
            'full_name',
            'email',
            'mensaje'
        )
        widgets = {
            'full_name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre y apellido'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo electronico'
                }
            )
        }

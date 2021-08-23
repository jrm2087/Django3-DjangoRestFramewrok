from django import forms
from django.contrib.auth import authenticate

from .models import User


class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'contraseña'}
        )
    )

    password2 = forms.CharField(
        label='contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Repetir contraseña'}
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'nombres', 'apellidos', 'genero')

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas deben ser iguales')


class LoginForm(forms.Form):
    username = forms.CharField(
        label='usuario',
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Usuario'}
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'contraseña'}
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError(
                'Los datos de usuario no son correctos')

        return self.cleaned_data


class UpdatePasswordForm(forms.Form):
    password1 = forms.CharField(
        label='Contraseña actual',
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'contraseña actual'}
        )
    )
    password2 = forms.CharField(
        label='Contraseña nueva',
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'contraseña nueva'}
        )
    )


class VerificationForm(forms.Form):
    cod_registro = forms.CharField(label='Código de registro', required=True)

    def __init__(self, pk, *args, **kwargs):
        self.id_user = pk
        super(VerificationForm, self).__init__(*args, **kwargs)

    def clean_cod_registro(self):
        codigo = self.cleaned_data['cod_registro']
        if len(codigo) == 6:
            # verificamos si el codigo y el id de usuario son validos
            activo = User.objects.cod_validation(
                self.id_user,
                codigo
            )
            if not activo:
                raise forms.ValidationError(
                    'El codigo debe ser de 6 caracteres.')
        else:
            raise forms.ValidationError('El codigo debe ser de 6 caracteres.')

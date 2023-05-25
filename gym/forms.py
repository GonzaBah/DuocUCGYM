from django import forms

#Este es el formulario del login
class FormLoginUsuario(forms.Form):
    correo = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'id':'email1',
                'type': 'email',
                'class': 'form-control'
            }
        )
    )

    contrasenia = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'contrasenia',
                'type': 'password',
                'class': 'form-control',
            }
        )
    )


#Este es el formulario de registro
class FormRegisUsuario(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'id': 'name',
                'type': 'text',
                'class': 'form-control'
            }
        )
    )
    apellido1 = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'id': 'lastname1',
                'type': 'text',
                'class': 'form-control'
            }
        )
    )
    apellido2 = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'id': 'lastname2',
                'type': 'text',
                'class': 'form-control'
            }
        )
    )
    rut = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'id': 'rut',
                'type': 'text',
                'class': 'form-control'
            }
        )
    )
    correo = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'id': 'email',
                'type': 'email',
                'class': 'form-control'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'password',
                'type': 'password',
                'class': 'form-control'
            }
        ))

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'password2',
                'type': 'password',
                'class': 'form-control'
            }
        ))


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las Contraseñas no coinciden')
        return cd['password2']



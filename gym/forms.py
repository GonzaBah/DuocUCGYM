from django import forms

#Este es el formulario del login

inputClass = 'px-3 py-2 bg-white border shadow-sm border-slate-200 placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-sky-500 block w-full rounded-lg sm:text-sm focus:ring-1 contrast-more:border-slate-400 contrast-more:placeholder-slate-500'

class FormLoginUsuario(forms.Form):
    correo = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'id':'email',
                'type': 'email',
                'class': inputClass
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'password',
                'type': 'password',
                'class': inputClass
            }
        )
    )


#Este es el formulario de registro
class FormRegisUsuario(forms.Form):
    rut = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'id': 'rut',
                'type': 'text',
                'class': inputClass
            }
        )
    )
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'id': 'name',
                'type': 'text',
                'class': inputClass
            }
        )
    )
    apellido1 = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'id': 'lastname1',
                'type': 'text',
                'class': inputClass
            }
        )
    )
    apellido2 = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'id': 'lastname2',
                'type': 'text',
                'class': inputClass
            }
        )
    )
    correo = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'id': 'email',
                'type': 'email',
                'class': inputClass
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'password',
                'type': 'password',
                'class': inputClass
            }
        ))

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'password2',
                'type': 'password',
                'class': inputClass
            }
        ))

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las Contraseñas no coinciden')
        return cd['password2']



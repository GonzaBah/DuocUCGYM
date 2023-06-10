from django import forms
from .models import Sucursal

#Este es el formulario del login

inputClass = 'px-3 py-2 bg-white border shadow-sm border-slate-200 placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-sky-500 block w-full rounded-lg sm:text-sm focus:ring-1 contrast-more:border-slate-400 contrast-more:placeholder-slate-500'
sucursales = Sucursal.objects.all()

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

#Este es el formulario de ficha
class FormFichaUsuario(forms.Form):
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
    altura = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'id': 'altura',
                'type': 'number',
                'class': inputClass
            }
        )
    )
    peso = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'id': 'peso',
                'type': 'number',
                'class': inputClass
            }
        )
    )
    fechaNac = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'id': 'fechaNac',
                'type': 'date',
                'class': inputClass
            }
        )
    )
    porcGrasa = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'id': 'porcGrasa',
                'type': 'number',
                'class': inputClass
            }
        )
    )
    observaciones = forms.CharField(
        max_length=500,
        widget=forms.Textarea(
            attrs={
                'id': 'obs',
                'type': 'text',
                'class': inputClass
            }
        )
    )

class FormRegisPlan(forms.Form):
    nombre = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'id': 'name',
                'type': 'text',
                'class': inputClass
            }
        )
    )
    descripcion = forms.CharField(
        max_length=200,
        widget=forms.Textarea(
            attrs={
                'id': 'desc',
                'type': 'text',
                'class': inputClass
            }
        )
    )
    sucursalLibre = forms.BooleanField(
        widget=forms.TextInput(
            attrs={
                'id': 'sucursalLibre',
                'type': 'checkbox',
                'class': "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
            }
        )
    )
    precio = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'id': 'precio',
                'type': 'number',
                'class': inputClass
            }
        )
    )

# class FormModPerfil(forms.Form):
#     rut = forms.CharField(
#         max_length=12,
#         widget=forms.TextInput(
#             attrs={
#                 'id': 'rut',
#                 'type': 'text',
#                 'class': inputClass
#             }
#         )
#     )

#     name = forms.CharField(
#         max_length=12,
#         widget=forms.TextInput(
#             attrs={
#                 'id': 'name',
#                 'type': 'text',
#                 'class': inputClass
#             }
#         )
#     )

#     lastname1 = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'id': 'apellido1',
#                 'type': 'text',
#                 'class': inputClass
#             }
#         )
#     )

#     correo = forms.EmailField(
#         widget=forms.TextInput(
#             attrs={
#                 'id':'email',
#                 'type': 'email',
#                 'class': inputClass
#             }
#         )
#     )
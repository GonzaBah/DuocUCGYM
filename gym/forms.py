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

class PictureForm(forms.Form):
    CHOICES = [
        ('1', 'Si'),
        ('2', 'No'),
    ]

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
    CHOICES = [
        ('1', 'Si'),
        ('2', 'No'),
    ]
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
   
    fechaNac = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'id': 'fechaNac',
                'type': 'date',
                'class': inputClass
            }
        )
    )
    edad = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'id': 'edad',
                'type': 'number',
                'class': inputClass
            }
        )
    )
    direccion = forms.CharField(
        max_length=125,
        widget=forms.Textarea(
            attrs={
                'id': 'direccion',
                'type': 'text',
                'class': inputClass
            }
        )
    )
    comuna = forms.CharField(
        max_length=35,
        widget=forms.Textarea(
            attrs={
                'id': 'comuna',
                'type': 'text',
                'class': inputClass
            }
        )
    )
    ciudad = forms.CharField(
        max_length=35,
        widget=forms.Textarea(
            attrs={
                'id': 'ciudad',
                'type': 'text',
                'class': inputClass
            }
        )
    )
    gSanguineo = forms.CharField(
        max_length=3,
        widget=forms.Textarea(
            attrs={
                'id': 'gSanguineo',
                'type': 'text',
                'class': inputClass
            }
        )
    )
    emergenciacontacto = forms.CharField(
        max_length=35,
        widget=forms.Textarea(
            attrs={
                'id': 'emergenciacontacto',
                'type': 'text',
                'class': inputClass
            }
        )
    )
    emergenciacontactoNumero = forms.CharField(
        max_length=9,
        widget=forms.Textarea(
            attrs={
                'id': 'emergenciacontactoNumero',
                'type': 'text',
                'class': inputClass
            }
        )
    )

    estatura = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'id': 'estatura',
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
    pLesion = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES
    )
    dLesion = forms.CharField(
        max_length=120,
        widget=forms.Textarea(
            attrs={
                'id': 'dLesion',
                'type': 'text',
                'class': inputClass
            }
        )
    )
    pEnfermedad = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES
    )
    dEnfermedad = forms.CharField(
        max_length=120,
        widget=forms.Textarea(
            attrs={
                'id': 'dEnfermedad',
                'type': 'text',
                'class': inputClass
            }
        )
    )
    pArt = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES
    )
    dArt = forms.CharField(
        max_length=120,
        widget=forms.Textarea(
            attrs={
                'id': 'dArt',
                'type': 'text',
                'class': inputClass
            }
        )
    )
    pDep = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES
    )
    dDep = forms.CharField(
        max_length=120,
        widget=forms.Textarea(
            attrs={
                'id': 'dDep',
                'type': 'text',
                'class': inputClass
            }
        )
    )
    fDeportes = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'id': 'fDeportes',
                'type': 'number',
                'class': inputClass
            }
        )
    )
    asmatico = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES
    )
    diabetico = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES
    )
    epileptico = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES
    )
    fumador = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES
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

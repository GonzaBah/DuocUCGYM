from django import forms
from .models import Sucursal

#Este es el formulario del login

inputClass = 'px-3 py-2 bg-white border shadow-sm border-slate-200 placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-sky-500 block w-full rounded-lg sm:text-sm focus:ring-1 contrast-more:border-slate-400 contrast-more:placeholder-slate-500'
checkClass = 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'
selectClass = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
sucursales = Sucursal.objects.all()
COMUNAS = [
        ('1', 'Huechuraba'),
        ('2', 'Providencia'),
]
SUCURSALES =[('', 'Seleccione')]+ list(map(lambda x: (x.idSucursal, x.nombreSucursal ), sucursales))

class FormLoginUsuario(forms.Form):
    correo = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id':'email',
                'type': 'email',
                'class': inputClass
            }
        )
    )

    password = forms.CharField(
        required=True,
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
        ('1', 'Huechuraba'),
        ('2', 'Providencia'),
    ]
#Este es el formulario de registro
class FormRegisUsuario(forms.Form):
    rut = forms.CharField(
        max_length=10,
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'rut',
                'type': 'text',
                'class': inputClass,
            }
        )
    )
    nombre = forms.CharField(
        max_length=100,
        required=True,
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
        required=True,
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
        required=False,
        widget=forms.TextInput(
            attrs={
                'id': 'lastname2',
                'type': 'text',
                'class': inputClass
            }
        )
    )
    correo = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'email',
                'type': 'email',
                'class': inputClass
            }
        )
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'id': 'password',
                'type': 'password',
                'class': inputClass
            }
        ))

    password2 = forms.CharField(
        required=True,
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
        min_value=18,
        widget=forms.NumberInput(
            attrs={
                'id': 'edad',
                'type': 'number',
                'class': inputClass
            }
        )
    )
    sucursal = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'id': 'sucursalSelect',
                'class': selectClass
            }
        ),
        choices=SUCURSALES,
    )
    direccion = forms.CharField(
        max_length=125,
        widget=forms.TextInput(
            attrs={
                'id': 'direccion',
                'type': 'text',
                'class': inputClass
            }
        )
    )
    comuna = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'id': 'comuna',
                'class': selectClass
            }
        ),
        choices=COMUNAS
    )
    ciudad = forms.CharField(
        max_length=35,
        widget=forms.TextInput(
            attrs={
                'id': 'ciudad',
                'type': 'text',
                'class': inputClass
            }
        )
    )
    gSanguineo = forms.CharField(
        max_length=3,
        widget=forms.TextInput(
            attrs={
                'id': 'gSanguineo',
                'type': 'text',
                'class': inputClass
            }
        )
    )
    emergenciacontacto = forms.CharField(
        max_length=35,
        widget=forms.TextInput(
            attrs={
                'id': 'emergenciacontacto',
                'type': 'text',
                'class': inputClass
            }
        )
    )
    emergenciacontactoNumero = forms.CharField(
        max_length=9,
        widget=forms.TextInput(
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
    pLesion = forms.BooleanField(
        initial=False,
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'id': 'pLesion',
                'type': 'checkbox',
                'class': checkClass
            }
        )
    )
    dLesion = forms.CharField(
        max_length=120,
        widget=forms.Textarea(
            attrs={
                'id': 'dLesion',
                'type': 'text',
                'class': inputClass
            }
        ),
        required=False
    )
    pEnfermedad = forms.BooleanField(
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                'id': 'pEnfermedad',
                'type': 'checkbox',
                'class': checkClass
            }
        ),
        required=False
    )
    dEnfermedad = forms.CharField(
        max_length=120,
        widget=forms.Textarea(
            attrs={
                'id': 'dEnfermedad',
                'type': 'text',
                'class': inputClass
            }
        ),
        required=False
    )
    pArt = forms.BooleanField(
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                'id': 'pArt',
                'type': 'checkbox',
                'class': checkClass
            }
        ),
        required=False
    )
    dArt = forms.CharField(
        max_length=120,
        widget=forms.Textarea(
            attrs={
                'id': 'dArt',
                'type': 'text',
                'class': inputClass
            }
        ),
        required=False
    )
    pDep = forms.BooleanField(
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                'id': 'pDep',
                'type': 'checkbox',
                'class': checkClass
            }
        ),
        required=False
    )
    dDep = forms.CharField(
        max_length=120,
        widget=forms.Textarea(
            attrs={
                'id': 'dDep',
                'type': 'text',
                'class': inputClass
            }
        ),
        required=False
    )
    fDeportes = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'id': 'fDeportes',
                'type': 'number',
                'class': inputClass,
                'value': 0
            }
        ),
        required=False
    )
    asmatico = forms.BooleanField(
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                'id': 'asmatico',
                'type': 'checkbox',
                'class': checkClass
            }
        ),
        required=False
    )
    diabetico = forms.BooleanField(
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                'id': 'diabetico',
                'type': 'checkbox',
                'class': checkClass
            }
        ),
        required=False
    )
    epileptico = forms.BooleanField(
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                'id': 'epileptico',
                'type': 'checkbox',
                'class': checkClass
            }
        ),
        required=False
    )
    fumador = forms.BooleanField(
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                'id': 'fumador',
                'type': 'checkbox',
                'class': checkClass
            }
        ),
        required=False
    )
    titularPlan = forms.CharField(
        max_length=120,
        widget=forms.TextInput(
            attrs={
                'id': 'titularPlan',
                'type': 'text',
                'class': inputClass
            }
        ),
        required=False
    )
    rutina = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(
            attrs={
                'id': 'rutina',
                'type': 'text',
                'class': inputClass
            }
        ),
        required=True
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


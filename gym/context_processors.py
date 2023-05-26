from .forms import FormLoginUsuario, FormRegisUsuario, FormFichaUsuario



def login_form(request):
    login_form = FormLoginUsuario()
    signup_form = FormRegisUsuario()
    
    ficha_form = FormFichaUsuario()
    return {
        'loginForm': login_form,
        'signupForm': signup_form,
        'fichaForm': FormFichaUsuario
    }
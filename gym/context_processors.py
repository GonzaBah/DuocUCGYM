from .forms import FormLoginUsuario, FormRegisUsuario, FormFichaUsuario, FormRegisPlan



def login_form(request):
    login_form = FormLoginUsuario()
    signup_form = FormRegisUsuario()
    ficha_form = FormFichaUsuario()
    plan_form = FormRegisPlan()
    
    return {
        'loginForm': login_form,
        'signupForm': signup_form,
        'fichaForm': ficha_form,
        'planForm': plan_form
    }
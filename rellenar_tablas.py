
from gym.models import Plan
planFamiliar = Plan(nombrePlan='Plan Familiar', estadoPlan=True, sucursalLibre=True, precio=120000)
planFamiliar.save()
planIndividualF = Plan(nombrePlan='Plan individual Full', estadoPlan=True, sucursalLibre=True, precio=80000)
planIndividualF.save()
planIndividualS = Plan(nombrePlan='Plan individual sucursal', estadoPlan=True, sucursalLibre=False, precio=45000)
planIndividualS.save()
planIndividualL = Plan(nombrePlan='Plan individual light', estadoPlan=True, sucursalLibre=True, precio=45000)
planIndividualL.save()
from gym.models import TipoUsuario
tipo = TipoUsuario(nombreTipo="Supervisor")
tipo.save()
tipo = TipoUsuario(nombreTipo="Profesor")
tipo.save()
tipo = TipoUsuario(nombreTipo="Socio")
tipo.save()

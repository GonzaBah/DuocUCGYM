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
tipo = TipoUsuario(nombreTipo="Administrador del sistema")
tipo.save()
tipo = TipoUsuario(nombreTipo="Administrador de sucursal")
tipo.save()
tipo = TipoUsuario(nombreTipo="Coordinador de sucursal")
tipo.save()
tipo = TipoUsuario(nombreTipo="Profesores de talleres")
tipo.save()
tipo = TipoUsuario(nombreTipo="Preparadores físicos")
tipo.save()
tipo = TipoUsuario(nombreTipo="Socio")
tipo.save()


from gym.models import Sucursal
suc = Sucursal(nombreSucursal="Plaza norte", direccionSucursal="Calle nueva")

suc.save()

suc = Sucursal(nombreSucursal="Antonio Varas", direccionSucursal="Calle Antonio")

suc.save()
from gym.models import Deporte
d = Deporte(nombreDeporte="Tenis")
d.save()
d = Deporte(nombreDeporte="Preparador físico")
d.save()
d = Deporte(nombreDeporte="Spinning")
d.save()
d = Deporte(nombreDeporte="Yoga")
d.save()
d = Deporte(nombreDeporte="Baile entretenido")
d.save()
d = Deporte(nombreDeporte="Natación")
d.save()
d = Deporte(nombreDeporte="Tenis de mesa")
d.save()
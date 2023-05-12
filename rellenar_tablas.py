from gym.models import TipoProfesor
tipoprofesor = TipoProfesor(nombreTipoProfesor='Tenis')
tipoprofesor.save()
tipoprofesor1 = TipoProfesor(nombreTipoProfesor='Preparador fisíco')
tipoprofesor1.save()
tipoprofesor2 = TipoProfesor(nombreTipoProfesor='Spinning')
tipoprofesor2.save()
tipoprofesor3 = TipoProfesor(nombreTipoProfesor='Yoga')
tipoprofesor3.save()
tipoprofesor4 = TipoProfesor(nombreTipoProfesor='Baile entretenido')
tipoprofesor4.save()
tipoprofesor5 = TipoProfesor(nombreTipoProfesor='Natación')
tipoprofesor5.save()
tipoprofesor5 = TipoProfesor(nombreTipoProfesor='Tenis de mesa')
tipoprofesor5.save()



from gym.models import Plan

planFamiliar = Plan(nombrePlan='Plan Familiar', estadoPlan=True, sucursalLibre=True, precio=120000)
planFamiliar.save()

planIndividualF = Plan(nombrePlan='Plan individual Full', estadoPlan=True, sucursalLibre=True, precio=80000)
planIndividualF.save()


planIndividualS = Plan(nombrePlan='Plan individual sucursal', estadoPlan=True, sucursalLibre=False, precio=45000)
planIndividualS.save()

planIndividualL = Plan(nombrePlan='Plan individual light', estadoPlan=True, sucursalLibre=True, precio=45000)
planIndividualL.save()
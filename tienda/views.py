from django.shortcuts import render
from tienda.models import Orden
from datetime import datetime
import zoneinfo

def traer_fecha_valida(fecha, conzonahoraria = False):
    if fecha is None:
        return None

    partes = fecha.split("-")
    if len(partes) != 3:
        return None
    
    try:
        year = int(partes[0])
        month = int(partes[1])
        day = int(partes[2])
        ff = datetime(year, month, day)
    except:
        return None

    if conzonahoraria:
        return ff.astimezone(zoneinfo.ZoneInfo('America/Santiago'))
    return ff

def v_index(request):
    fecha_inicio = request.GET.get("fecha_inicio", None)
    fecha_inicio = traer_fecha_valida(fecha_inicio)

    fecha_fin = request.GET.get("fecha_fin", None)
    fecha_fin = traer_fecha_valida(fecha_fin)

    fecha_e_inicio = request.GET.get("fecha_e_inicio", None)
    fecha_e_inicio = traer_fecha_valida(fecha_e_inicio, conzonahoraria = True)
    
    fecha_e_fin = request.GET.get("fecha_e_fin", None)
    fecha_e_fin = traer_fecha_valida(fecha_e_fin, conzonahoraria = True)


    consulta = Orden.objects.all()

    if fecha_inicio is not None and fecha_fin is not None:
        consulta = Orden.objects.filter(fecha__range = (fecha_inicio, fecha_fin))
    
    if fecha_e_inicio is not None and fecha_e_fin is not None:
        consulta = Orden.objects.filter(fecha_envio__range = (fecha_e_inicio, fecha_e_fin))
    
    context = {
        'ordenes': consulta
    }
    
    return render(request, 'index.html', context)
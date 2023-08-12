from django.test import TestCase
from tienda.models import Orden
from datetime import datetime
import zoneinfo
from django.utils import timezone

# Create your tests here.
class TiendaViewsTests(TestCase):
    def test_v_index(self):
        # print("Test 1")
        # print("-->>>>>>>>>>", Orden.objects.all().count())
        respuesta = self.client.get("/")
        ords = respuesta.context["ordenes"]
        self.assertEqual(0, len(ords))

        newO = Orden()
        newO.cliente = "Jaimito"
        newO.fecha = "2023-12-12"
        newO.fecha_envio = datetime(2023,12,12).astimezone(zoneinfo.ZoneInfo('America/Santiago'))
        newO.direccion = "Direccion"
        newO.save()

        respuesta = self.client.get("/")
        ords = respuesta.context["ordenes"]
        self.assertEqual(1, len(ords))

    def test_v_index_filtros(self):
            newO = Orden()
            newO.cliente = "Pedrito"
            newO.fecha = "2022-12-12"
            newO.fecha_envio = datetime(2022,12,12).astimezone(zoneinfo.ZoneInfo('America/Santiago'))
            newO.direccion = "Direccion"
            newO.save()   

            newO = Orden()
            newO.cliente = "Albertito"
            newO.fecha = "2023-12-12"
            newO.fecha_envio = datetime(2023,12,12).astimezone(zoneinfo.ZoneInfo('America/Santiago'))
            newO.direccion = "Direccion"
            newO.save()

            respuesta = self.client.get("/?fecha_inicio=%s&fecha_fin=%s" % (
                "2023-11-01", 
                "2023-12-25",
                ))
            
            ords = respuesta.context["ordenes"]
            self.assertEqual(1, len(ords))
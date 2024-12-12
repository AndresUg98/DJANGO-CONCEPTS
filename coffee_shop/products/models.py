from django.db import models


class Product(models.Model):
    # Verbose es como queremos que se muestre en nuestra aplicacion
    name = models.TextField(max_length=200, verbose_name="nombre")
    description = models.TextField(max_length=300, verbose_name="descripción")
    # agregando numeros, permite agregar numeros con decimales
    price = models.models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="precio"
    )
    available = models.BooleanField(default=True,verbose_name="disponible")
    photo = models.ImageField(upload_to="logos",null=True,blank=True, verbose_name="foto")

    def __str__(self):
        return self.name
# from django.db import models

# class LeerGewicht(models.Model):
#     id = models.AutoField(primary_key=True)
#     leer_gewicht = models.DecimalField(max_digits=5, decimal_places=2)

#     def __str__(self):
#         return f"{self.leer_gewicht}"
    
#     class Meta:
#         verbose_name = "Leer Gewicht"
#         verbose_name_plural = "Leer Gewichte"

# class API_Data(models.Model):
#     id = models.AutoField(primary_key=True)
#     datum = models.DateField()
#     zeit = models.TimeField()
#     temperatur = models.DecimalField(max_digits=5, decimal_places=2)
#     gewicht = models.DecimalField(max_digits=5, decimal_places=2)

#     @property
#     def honig(self):
#         leer_gewicht = LeerGewicht.objects.get(id=1).leer_gewicht
#         return self.gewicht - leer_gewicht

#     notiz = models.TextField()

#     def __str__(self):
#         return f"{self.datum} - {self.zeit}"
    
#     class Meta:
#         verbose_name = "API Daten"
#         verbose_name_plural = "API Daten"
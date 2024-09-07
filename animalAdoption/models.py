from django.db import models

# Create your models here.
class Animal(models.Model):
    nom = models.CharField(max_length=200)
    age = models.IntegerField()
    statut_vaccinal = models.BooleanField(default=False)
    sterilisation = models.BooleanField(default=False)

    class Meta:
        abstract = True
class chien(Animal):
    def __str__(self):
        return f"{self.nom}"
    pass
class chat(Animal):
    def __str__(self):
        return f"{self.nom}"
    pass
class oiseau(Animal):
    def __str__(self):
        return f"{self.nom}"
    pass
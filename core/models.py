from django import forms
from django.db import models

# Create your models here.


etatParent = [
    ('D', 'décédé(e)'),
    ('V', 'vivant(e)')
]


class famille(models.Model):
    nomFamille = models.CharField(max_length=255, verbose_name="nom famille")

    # model pere---------------
    nomP = models.CharField(max_length=255, verbose_name="nom pere")
    prenomP = models.CharField(max_length=255, verbose_name="prenom pere")
    etatP = models.CharField(choices=etatParent, max_length=200, verbose_name="état pere")
    professionP = models.CharField(max_length=255, verbose_name="Profession pere")
    santeP = models.CharField(max_length=200, null=True, verbose_name="sante Pere")
    revenuP = models.FloatField(default=0.00, verbose_name='revenu Pere')

    # model maman---------------
    nomM = models.CharField(max_length=255, verbose_name="nom Mère")
    prenomM = models.CharField(max_length=255, verbose_name="prenom Mère")
    etatM = models.CharField(choices=etatParent, max_length=200, verbose_name="état Mère")
    professionM = models.CharField(max_length=255, verbose_name="Profession Mère")
    santeM = models.CharField(max_length=200, null=True, verbose_name="sante Mère")
    revenuM = models.FloatField(default=0.00, verbose_name='revenu Mère')

    # Enfant ----------
    nmbreEnfant = models.IntegerField(default=0, verbose_name="nombre enfant")

    # Coordonées -------------

    def __str__(self):
        return self.nomFamille

    class Meta:
        verbose_name = 'famille'
        ordering = ['revenuP']


# i want to add a class from children so we can control it in a different way
# cuz we should have a from for every kid
class enfant(models.Model):
    # nomE = models.CharField(max_length=255)
    # famille = models.OneToOneField(famille, on_delete=models.CASCADE)



    class Meta:
        verbose_name = 'Enfant'




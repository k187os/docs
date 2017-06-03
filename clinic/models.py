from django.db import models


# Create your models here.


class Patient(models.Model):
    Nom = models.CharField(max_length=100)
    Prenom = models.CharField(max_length=100)
    choice = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    Gendre = models.CharField(max_length=1, choices=choice, default='M')
    Date_Naissance = models.DateField(blank=True)
    Age = models.CharField(max_length=10 , blank=True)
    Adresse = models.CharField(max_length=100, blank=True)
    Mobile = models.CharField(max_length=10, blank=True)
    create_date = models.DateTimeField(auto_now=True)
    NSS = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return "{0} {1}".format(self.Nom, self.Prenom)

    def save(self, force_insert=False, force_update=False):
        self.Nom = self.Nom.upper()
        self.Prenom = self.Prenom.upper()
        self.Age = self.Age.upper()
        super(Patient, self).save(force_insert, force_update)


class Consultation(models.Model):
    num = models.ForeignKey(Patient)
    date = models.DateTimeField(editable=True)
    Diag = models.TextField(blank=False,)

    def __str__(self):
        return '{0}'.format(self.num)


class Drug(models.Model):
    drug_nom = models.CharField(max_length=100)
    drug_famille = models.CharField(max_length=100)
    drug_forme = models.CharField(max_length=100)
    drug_dose = models.CharField(max_length=100)
    drug_obs= models.CharField(max_length=100)

    def __str__(self):
        return "{0}".format(self.drug_nom)
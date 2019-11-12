from django.db import models

# Create your models here.


class Doctor(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Patient(models.Model):

    name = models.CharField(max_length=100)
    doctors = models.ManyToManyField(Doctor, related_name="patients")  # ManyToMany model links 2 models with related method name

    def __str__(self):
        return self.name


# if you want save anoter information like reservation, use linked model like this
# class Reservation(models.Model):

#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     time = models.CharField(max_length=100)
#     location = models.CharField(max_length=100, default='3rd floor')

#     def __str__(self):
#         return f'{self.doctor.name} is doctor of {self.patient.name}'

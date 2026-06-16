from django.db import models

# Create your models here.


class People(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    def __str__(self):
        return f"{self.name}"

class Role(models.Model):
    role_name = models.CharField(max_length=255)
    responsible = models.ForeignKey(People, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.role_name}"


class Church(models.Model):
    church_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    fk_people = models.ForeignKey(People, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.church_name}"
    

class Archdiocese(models.Model):
    fk_people = models.ForeignKey(People, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    fk_church = models.ForeignKey(Church, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.fk_church} Archdiocese"
from django.db import models

# Create your models here.

class Institution(models.Model):
    name = models.CharField(max_length=100,unique=True)
    address = models.TextField()
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    contact_person_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Learner(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    institution = models.ForeignKey(Institution,on_delete=models.CASCADE)
    course = models.CharField(max_length=100, blank=True, null=True)
    batch = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Assessor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    institution = models.ForeignKey(Institution,on_delete=models.CASCADE)
    role = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name} role is {self.role}'

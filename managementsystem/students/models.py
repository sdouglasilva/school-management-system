from django.db import models


class Discipline(models.Model):

  DISCIPLINE_CHOICES = [
        ('matematica', 'Matemática'),
        ('portugues', 'Português'),
        ('historia', 'História'),
        ('geografia', 'Geografia'),
        ('ciencias', 'Ciências'),
        ('ingles', 'Inglês'),
        ('ed_fisica', 'Educação Física'),
        ('artes', 'Artes'),
        ('literatura', 'Literatura'),
        ('quimica', 'Química'),
        ('fisica', 'Física'),
        ('biologia', 'Biologia')]
  
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Students(models.Model):
  fist_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  date_of_birth = models.DateField()
  email = models.EmailField(unique=True)
  enrollment_date = models.DateField(auto_now_add=True)
  discipline = models.ManyToManyField(Discipline, related_name='students')#nome do app/tabela


def __str__(self):
    return f"{self.first_name} {self.last_name} - {self.enrollment_date}"



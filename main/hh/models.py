from django.db import models
from django.contrib.auth.models import User

class Skills(models.Model):
    name = models.CharField(max_length=100)
    percent = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    address = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    title = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    salary = models.IntegerField(max_length=200)
    skills = models.ManyToManyField(Skills)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    type_of_job = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Resume(models.Model):
    dream_job = models.CharField(max_length=30)
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    skills = models.ManyToManyField(Skills)
    experience = models.TextField(max_length=255)
    education = models.TextField()
    gender = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Request(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15)

    def __str__(self):
        return f"request {self.id}"

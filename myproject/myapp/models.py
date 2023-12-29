from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Person(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} - {self.email}"

class Address(BaseModel):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='addresses', null=True, blank=True)

    def __str__(self):
        return f"{self.street}, {self.city}"



class Job(BaseModel):
    title = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='jobs')

    def __str__(self):
        return f"{self.title} - Person: {self.person} - Salary: {self.salary}"


class Event(BaseModel):
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    person = models.ManyToManyField(Person, related_name='events')

    def __str__(self):
        return self.name

class Document(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    person = models.ManyToManyField(Person, related_name='documents')

    def __str__(self):
        return f"{self.title}"
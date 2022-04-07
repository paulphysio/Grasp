from django.db import models


class product(models.Model):
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField(default=200)

class ToDoList(models.Model):
    name = models.CharField(default = "name",max_length=200)
    content = models.CharField(default="Plans",max_length=200)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Notify(models.Model):
    name = models.CharField(default="e.g. John Simon",max_length=200)
    email = models.EmailField(default = "example@contact.com",max_length=200)

    def __str__(self):
        return self.name
    

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length= 300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
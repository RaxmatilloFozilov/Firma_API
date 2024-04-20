from django.db import models


# Create your models here.

class Title(models.Model):
    title_name = models.CharField(max_length=250)
    title_description = models.TextField()
    title_image = models.ImageField(upload_to='images/firma', default='images/firma/firma.jpg')


class Result(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    result_image = models.ImageField(upload_to='images/firma', default='images/firma/firma.jpg')


class Letters(models.Model):
    title_name = models.CharField(max_length=250)
    select_letter = models.CharField(max_length=25)
    letter_name = models.CharField(max_length=25)


class Search(models.Model):
    title_name = models.CharField(max_length=250)
    search_result = models.CharField(max_length=250)


class Absolute(models.Model):
    origin = models.CharField(max_length=250)
    phrase = models.CharField(max_length=250)
    dictionary_meaning = models.CharField(max_length=250)
    examples = models.CharField(max_length=250)

    def __str__(self):
        return self.origin


from django.db import models


class YearsServing(models.Model):
    years_serving_integer = models.IntegerField()


class Members(models.Model):
    members_integer = models.IntegerField()


class ReviewsImg(models.Model):
    reviews_image = models.ImageField()

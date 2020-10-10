from django.db import models

class User(models.Model) :
    user_email = models.CharField(max_length = 50, primary_key = True)
    user_name = models.CharField(max_length=50)

    def __str__(self) :
        return self.title

class Course(models.Model) :
    course_id = models.IntegerField(primary_key=True)
    region = models.CharField(max_length=10)
    sequence = models.CharField(max_length=50)
    course_name = models.CharField(max_length=50)

    def __str__(self) :
        return self.course_name

class Spot(models.Model) :
    spot_id = models.IntegerField(primary_key = True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    spot_name = models.CharField(max_length=20)

    def __str__(self) :
        return self.spot_name

class MyCourse (models.Model) :
    my_course_id = models.IntegerField(primary_key=True)
    user_email = models.ForeignKey(User, on_delete=models.CASCADE)
    sequence = models.CharField(max_length=50)
    my_course_name = models.CharField(max_length=50)
    region = models.CharField(max_length=10)

    def __str__(self) :
        return self.my_course_name
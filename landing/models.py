from django.db import models


class Athlete(models.Model):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_OTHER = 'O'

    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES)

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name

# class BasketballInfo(models.Model):

#     EXPERIENCE_PRO = 'P'
#     EXPERIENCE_COLLEGE = 'C'
#     EXPERIENCE_HIGHSCHOOL = 'H'
#     EXPERIENCE_STREET = 'S'
#     EXPERIENCE_BOOTCAMP = 'B'

#     EXPERIENCE_CHOICES = [
#         (EXPERIENCE_PRO, 'Pro'),
#         (EXPERIENCE_COLLEGE, 'College'),
#         (EXPERIENCE_HIGHSCHOOL, 'Highschool'),
#         (EXPERIENCE_STREET, 'Street'),
#         (EXPERIENCE_BOOTCAMP, 'Bootcamp'),
#     ]

#     POSITION_POINTGURD = 'PG'
#     POSITION_SHOOTINGGUARD = 'SG'
#     POSITION_SMALLFORWARD = 'SF'
#     POSITION_POWERFORWARD = 'PF'
#     POSITION_CENTER = 'CR'

#     POSITION_CHOICES = [
#         (POSITION_POINTGURD, 'Point guard'),
#         (POSITION_SHOOTINGGUARD, 'Shooting guard'),
#         (POSITION_SMALLFORWARD, 'Small forward'),
#         (POSITION_POWERFORWARD, 'Power forward'),
#         (POSITION_CENTER, 'Center'),
#     ]

#     athlete = models.ForeignKey(Athlete, on_delete=models.PROTECT)
#     experience = models.CharField(
#         max_length=1, choices=EXPERIENCE_CHOICES)
#     positiom = models.ForeignKey(Athlete, on_delete=models.PROTECT)
#     experience = models.CharField(
#         max_length=2, choices=POSITION_CHOICES)
    # frequency_of_play =
    # favourite_tean =

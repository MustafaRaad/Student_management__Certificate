from django.db import models
import uuid
from django.urls import reverse


class College(models.Model):
    abbreviation = models.CharField(max_length=10)
    title = models.CharField(max_length=128, choices=(
        ('BIC', 'Business Informatics College'), ('EC', 'College of Engineering'), ('MC', 'Medical College')))
    university = models.CharField(max_length=64, choices=(
        ('1', 'University of Information Technology and Communications'),))

    def __str__(self):
        return self.abbreviation


class Department(models.Model):
    abbreviation = models.CharField(max_length=10)
    title = models.CharField(max_length=64)
    college = models.ForeignKey(
        College, on_delete=models.CASCADE, related_name='department')

    def __str__(self):
        return self.abbreviation


class Student(models.Model):
    classGroups = [('A', 'A'), ('B', 'B'), ('C', 'C'),
                   ('D', 'D'), ('E', 'E'), ('F', 'F')]
    cities = [('Anbar', 'Anbar'), ('Babil', 'Babil'), ('Baghdad', 'Baghdad'), ('Basra', 'Basra'), ('Dhi Qar', 'Dhi Qar'), ('Al-Qādisiyyah', 'Al-Qādisiyyah'), ('Diyala', 'Diyala'), ('Duhok', 'Duhok'), ('Erbil', 'Erbil'),
              ('Karbala', 'Karbala'), ('Kirkuk', 'Kirkuk'), ('Maysan', 'Maysan'), ('Muthanna', 'Muthanna'), ('Najaf', 'Najaf'), ('Nineveh', 'Nineveh'), ('Saladin', 'Saladin'), ('Sulaymaniyah', 'Sulaymaniyah'), ('Wasit', 'Wasit')]
    stages = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')]
    status = [('Pass_1', 'Pass / first attepmt'), ('Pass_2', 'Pass / second attempt'),
              ('Fail', 'Fail'), ('Upload_1', 'Upload 1'), ('Upload_2', 'Upload 2'), ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    register_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='students_pics', blank=True)
    AR_full_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=16)
    second_name = models.CharField(max_length=16)
    third_name = models.CharField(max_length=16)
    fourth_name = models.CharField(max_length=16)
    sur_name = models.CharField(max_length=16)
    mother_full_name = models.CharField(max_length=64)
    gender = models.CharField(max_length=7, choices=(
        ('male', 'Male'), ('female', 'Female')))
    birthdate = models.DateTimeField()
    verified_personal_info = models.BooleanField(default=False)

    phone = models.IntegerField(blank=True, null=True)
    parent_phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True)
    first_address = models.CharField(max_length=64, blank=True)
    second_address = models.CharField(max_length=64, blank=True)
    verified_contact_info = models.BooleanField(default=False)

    nationality = models.CharField(max_length=16)
    birth_city = models.CharField(max_length=16, choices=cities, blank=True)
    living_city = models.CharField(max_length=16, choices=cities, blank=True)
    national_id = models.CharField(max_length=16, blank=True)
    national_id_issue_place = models.CharField(
        max_length=24, choices=cities, blank=True)
    passport_id = models.CharField(max_length=24, blank=True)
    passport_issue_place = models.CharField(
        max_length=16, choices=cities, blank=True)
    passport_expire_date = models.DateTimeField(blank=True, null=True)
    verified_nation_info = models.BooleanField(default=False)

    medical_status = models.CharField(max_length=128, blank=True)
    school_document = models.FileField(upload_to='school_docs', blank=True)
    degree_approval = models.FileField(upload_to='school_docs', blank=True)
    average = models.IntegerField()
    verified_school_info = models.BooleanField(default=False)

    college = models.ForeignKey(
        College, on_delete=models.CASCADE, null=True, related_name='student')
    AR_college = models.CharField(max_length=64, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, blank=True)
    AR_department = models.CharField(max_length=64, blank=True)
    stage = models.CharField(max_length=2, choices=stages, blank=True)
    group = models.CharField(max_length=2, choices=classGroups, blank=True)
    enroll_date = models.DateTimeField(blank=True, null=True)
    examination_id = models.CharField(max_length=24, blank=True)
    final_grade = models.CharField(max_length=64, blank=True)
    status = models.CharField(max_length=64, blank=True, choices=status)

    verified_college_info = models.BooleanField(default=False)

    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)

    def get_absolute_url(self):
        return reverse("student:student-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return '%s %s' % (self.first_name, self.second_name)
    

"""
##  Developed By:Mustafa Raad Mutashar  ##
##  mustafa.raad.7@gmail.com     2020   ##
"""


from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
import os,re
import uuid

class Faculty(AbstractUser):
    
    age = models.PositiveIntegerField(default=0)
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    department_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, null=False, blank=False,unique=True)
    ROLE=(('HOD','HOD'),('OTHER','OTHER'))
    role=models.CharField(max_length=10,choices=ROLE,default='OTHER')
    fac_id=models.UUIDField(default=uuid.uuid4(),null=False,blank=False,primary_key=True,editable='false')

    def clean(self):
        if not re.match(r'^(?:\+\d{2})?\d{10}$', self.phone_number):
            raise ValidationError("Invalid phone number format, it should be in the format of +91xxxxxxxxxx ")
    
    def __str__(self):
        return self.username



def validate_pdf(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf']
    if ext not in valid_extensions:
        raise ValidationError("File should be in pdf format")




class Conference(models.Model):
    fac_id=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    conference_id = models.CharField(primary_key=True,max_length=100)
    conference_name = models.CharField(max_length=255)
    conference_article = models.FileField(upload_to='conference/',validators=[validate_pdf])
    conference_doi=models.IntegerField(null=True,blank=True)
    ugc=(('Yes','Yes'),('No','No'))
    ugc_listed=models.CharField(max_length=10,choices=ugc)

    def __str__(self):
        return self.conference_name




class Journal(models.Model):
    fac_id=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    journal_id = models.CharField(primary_key=True,max_length=100)
    journal_name = models.CharField(max_length=255)
    journal_article = models.FileField(upload_to='journal/',validators=[validate_pdf])
    journal_doi=models.IntegerField(null=True,blank=True)
    ugc=(('Yes','Yes'),('No','No'))
    ugc_listed=models.CharField(max_length=10,choices=ugc)

    def __str__(self):
        return self.journal_name


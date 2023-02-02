
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
import os,re
import uuid

class Faculty(AbstractUser):
    name=models.CharField(max_length=100,default='Your Name',unique=False)
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
    fac_id=models.UUIDField(default=uuid.uuid4(),primary_key=True,editable=False)
    
    
    def clean(self):
        if not re.match(r'^(?:\+\d{2})?\d{10}$', self.phone_number):
            raise ValidationError("Invalid phone number format, it should be in the format of +91xxxxxxxxxx ")
    
    def save(self, *args, **kwargs):           # the uuid is created on the basis of the username which is unique
        self.fac_id = uuid.uuid5(uuid.NAMESPACE_DNS, self.username)
        super().save(*args, **kwargs)
        
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




def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')

class Post(models.Model):
    category=(('conference','conference'),('journal','journal'))
    fac_id=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    post_title=models.CharField(max_length=300,null=False,blank=False)
    post_snap = models.ImageField(upload_to='post_images/',validators=[validate_file_extension])
    post_details=models.TextField(max_length=1000,null=False,blank=False)
    post_time = models.DateTimeField(auto_now_add=True)
    post_category = models.CharField(max_length=100,choices=category)
    likes = models.ManyToManyField(Faculty, related_name='likes', blank=True)

    def __str__(self):
        return self.post_title


class Event(models.Model):
    fac_id = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    event_Location = models.TextField(max_length=500)
    event_Name = models.CharField(max_length=200)
    event_Date = models.CharField(max_length=100)
    event_details=models.TextField(max_length=1000,null=False,blank=False)
    post_event=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_Name
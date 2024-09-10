from django.db import models

# Create your models here.

class register(models.Model):
    id = models.AutoField(primary_key=True)
    fullname_reg = models.CharField(max_length=255,null=True,blank=False)
    dob_reg = models.DateField()
    age_reg = models.CharField(max_length=3,null=False,blank=False)
    email_reg = models.EmailField(max_length=255,null=False,blank=False)
    phono_reg = models.CharField(max_length=10,null=False,blank=False,unique=True)
    username_reg = models.CharField(max_length=255,null=False,blank=False)
    password_reg = models.CharField(max_length=255,null=False,blank=False)
    cpassword_reg = models.CharField(max_length=255,null=False,blank=False)
    gender_reg = models.CharField(max_length=6, null=True, blank=True)
    image_reg = models.ImageField(upload_to='user_profileimg/',max_length=250, null=True, blank=True)
    report = models.FileField(upload_to='user_report/',max_length=250, null=True, blank=True)
# def __str__(self):
#         return self.fullname_reg    

# class user_report(models.Model):
#     report = models.ImageField(upload_to='user_report/',max_length=250, null=True, blank=True)

class doctor(models.Model):
    doctor_name=models.CharField(max_length=255,null=False,blank=True)
    doctor_qualification=models.CharField(max_length=255,null=False,blank=True)
    doctor_experience=models.CharField(max_length=2,null=False,blank=True)
    doctor_contact=models.CharField(max_length=10,null=False,blank=True)
    doctor_email=models.CharField(max_length=255,null=False,blank=True)
    doctor_image=models.ImageField(upload_to='doctor_image/',max_length=250,null=True,blank=True)

class medicines(models.Model):
    medicines_name=models.CharField(max_length=255, null=False, blank=True)
    medicines_description=models.CharField(max_length=255, null=False, blank=True)
    medicines_price=models.CharField(max_length=255, null=False, blank=True)
    medicines_image=models.ImageField(upload_to='medicines_image/',max_length=250,null=True,blank=True)
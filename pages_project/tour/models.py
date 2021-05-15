from django.db import models
from django import forms
# Create your models here.

#this is for update of package
class Destination(models.Model):
    name=   models.CharField(max_length=100)
    img =   models.ImageField(upload_to='pics')
    desc=   models.TextField()
    price=  models.IntegerField()
    offer=  models.BooleanField(default=False)

# this is for Testimonial message display
class Testimonial(models.Model):
    desc = models.TextField()
    name=models.CharField(max_length=100)   


# this is for our gallery 
class Gallery_pics(models.Model):
    img =   models.ImageField(upload_to='pics', default=None)
    name=models.CharField(max_length=100,)
    desc=models.TextField()
    
class Gallery(models.Model):
    img =   models.ImageField(upload_to='pics')

    

class MyForm(forms.ModelForm):
    name = forms.CharField(error_messages={'required':'Please enter your name'})
    lname = forms.CharField(error_messages={'required':'Please enter your name'})
    phone_number=forms.CharField(error_messages={'required':'Please enter your name'})
    email=forms.CharField(error_messages={'required':'Please enter your name'})
    destination=forms.CharField(error_messages={'required':'Please enter your name'})
    startdate=forms.CharField(error_messages={'required':'Please enter your name'})
    adult=forms.CharField(error_messages={'required':'Please enter your name'})
    child=forms.CharField(error_messages={'required':'Please enter your name'})
 
    class Meta:
        model = Booking
        fields = ('name','lname','phone_number','email','destination','startdate','adult','child')


class Package(models.Model):
    name=models.CharField(max_length=100, default="Destination name")
    img =   models.ImageField(upload_to='pics')
    feature1= models.CharField(max_length=100, default="feature1")
    feature2= models.CharField(max_length=100, default="feature1")
    feature3= models.CharField(max_length=100, default="feature1")
    feature4= models.CharField(max_length=100, default="feature1")
    feature5= models.CharField(max_length=100, default="feature1")
    price=models.IntegerField(null=True)

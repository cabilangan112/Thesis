
from __future__ import unicode_literals

from django.db import models

class student(models.Model):
	Last_name    =	 models.CharField(max_length=100, help_text="Enter your Last_name ")
	First_name 	 = 	 models.CharField(max_length=200, help_text="Enter your First name ")
	MI 			 =	 models.CharField(max_length=200, help_text="Enter your Middle Name")
	Gender = (
        ('m', 'Male'),
        ('F', 'Female'),
	)
	Sex			  =   models.CharField(max_length=1, choices=Gender, blank=True, default='m')
	
	def get_absolute_url(self):
		return reverse(' student-detail', args=[str(self.id)])

	def __str__(self):
		return '%s, %s' % (self.Last_name, self.First_name)
	
	
class Department(models.Model):
	Dep = (
		('CITE', 'College of information and Technology  '),
		('CBA', 'College Busnisss And Accountancy'),
		('ASCEND', 'ASCEND '),
	)
	
	Department	 = models.CharField(max_length=8, choices=Dep, blank=True, default='b', help_text='Department')
	
	def __str__(self):
		return  self.Department
	
class Post(models.Model):
    text 			= models.TextField()
    created_date 	= models.DateTimeField(
            default	=timezone.now)
    published_date 	= models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

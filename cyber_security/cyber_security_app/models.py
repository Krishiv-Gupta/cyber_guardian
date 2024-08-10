from django.db import models
# Create your models here.
# from django import forms 

# A1 =( 
# 	("1", "To speed up internet connection"), 
# 	("2", "To protect the network from unauthorized access"), 
# 	("3", "To block spam emails"), 
# 	("4", "To manage user passwords"),
#     ("5", "To protect the network from unauthorized access"),
# ) 

# A2 =( 
# 	("1", "Phishing scams"), 
# 	("2", "Regular account monitoring"), 
# 	("3", "Strong password policies"), 
# 	("4", "Multi-factor authentication"),
#     ("5", "Phishing scams"),
# ) 
# A3 =(
#     ("1", "To make the transaction process faster"), 
# 	("2", "To ensure that data is readable by anyone"), 
# 	("3", "To protect sensitive information from unauthorized access"), 
# 	("4", "To create backups of transaction data"),
# )
# A4 =(
#     ("1", "HIPAA"), 
# 	("2", "PCI DSS"), 
# 	("3", "GDPR"), 
# 	("4", "SOX"),
# )
# A5 =(
#     ("1", "Receiving regular account statements"), 
# 	("2", "Noticing unfamiliar transactions or charges"), 
# 	("3", "Getting notified of a password change you initiated"), 
# 	("4", "Being asked to change your password for security reasons"),
# )
# class Quiz(forms.Form): 
# 	q1 = forms.MultipleChoiceField(choices = A1) 
# 	q2 = forms.MultipleChoiceField(choices = A2) 
# 	q3 = forms.MultipleChoiceField(choices = A3) 
# 	q4 = forms.MultipleChoiceField(choices = A4) 
# 	q5 = forms.MultipleChoiceField(choices = A5) 
	
class SafetyTest(models.Model): 
	q1 = models.BooleanField() 
	q2 = models.BooleanField()
	q3 = models.BooleanField() 
	q4 = models.BooleanField() 
	q5 = models.BooleanField()  
	
class e(models.Model):
    Name=models.CharField(max_length=50)
    Phone=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    W=models.CharField(max_length=500)


class sign(models.Model):
    email=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    
    

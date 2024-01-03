from django.db import models

# Create your models here.
class Emp(models.Model):
    Empno=models.IntegerField()
    Ename=models.CharField(max_length=100)
    sal=models.PositiveIntegerField()
    dept_no=models.PositiveIntegerField()

    def __str__(self):
        return self.Ename
class Dept(models.Model):
    dept_no=models.ForeignKey(Emp,on_delete=models.CASCADE)
    dname=models.CharField(max_length=100)
    dloc=models.CharField(max_length=100,default='india')
    
    def __str__(self):
        return self.dname
    



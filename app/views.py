from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
# Create your views here.
def display_emp(request):
    QLEO=Emp.objects.all()
    QLEO=Emp.objects.all().order_by('-Ename')
    QLEO=Emp.objects.all().order_by(Length('Ename').desc())
    QLEO=Emp.objects.filter(sal=3000).order_by('Ename')
    d={'emp':QLEO}
    return render(request,'display_emp.html',d)

def display_dept(request):
    QLDO=Dept.objects.all()
    QLDO=Dept.objects.all().order_by('dept_no')
    QLDO=Dept.objects.all().order_by('-dept_no')
    d={'dept':QLDO}
    return render(request,'display_dept.html',d)


def insert_emp(request):
    empno=int(input('enter empno'))
    ename=input('enter ename')
    sal=int(input('enter sal'))
    dept_no=int(input('enter dept_no'))
    EO=Emp.objects.get_or_create(Empno=empno,Ename=ename,sal=sal,dept_no=dept_no)[0]
    EO.save()
    return HttpResponse('insertion sucess')


def insert_dept(request):
    pk=int(input('enter pk'))
    dept_no=int(input('enter deptno'))
    dname=input('enter dname')
    dloc=input('enter loc')
    EO=Emp.objects.get(pk=pk)
    DO=Dept.objects.get_or_create(dept_no=EO,dname=dname,dloc=dloc)[0]
    DO.save()
    return HttpResponse('insertion sucess')

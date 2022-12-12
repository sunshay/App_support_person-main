from django.shortcuts import render,redirect
from rest_framework import mixins
from rest_framework import generics
from .models import User, Customer, Campany, Subject
from .serializers import (CustomerSerializer,CompanySerializer, SubjectSerializer)
from .forms import CustomerForm, CampanyForm, SubjectForm
from django.contrib import messages
  


 
# partials web fucitonlite

def create_subject(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
    context["subjects"] = Subject.objects.all()
 
    # add the dictionary during initialization
    form = SubjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f"Add succefuly")
         
    context['form']= form
    return render(request, "create_subject.html", context)

# function to save notification
def save_customer(request):
    if request.method == 'POST':
        email= request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        username = request.POST.get('username')
       
        customer = Customer(email=email, phone_number=phone_number,username=username)
        customer.save()
        messages.success(request, f"Add succefuly")
        return redirect('create_subject')
    
# function to save notification
def save_campany(request):
    if request.method == 'POST':
        name= request.POST.get('campany_name')
       
        campany = Campany(name=name)
        
        campany.save()
        messages.success(request, f"Add succefuly")

        return redirect('create_subject')


def create_customer(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "create_customer.html", context)


def create_campany(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = CampanyForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "create_campany.html", context)

# partials for api   
# view for User 
class CustomerList(generics.ListCreateAPIView):
    
    queryset =Customer.objects.all()
    serializer_class = CustomerSerializer


# view for Campany
class CampanyList(generics.ListCreateAPIView):
    
    queryset = Campany.objects.all()
    serializer_class = CompanySerializer

# view for subject   
class SubjectList(generics.ListCreateAPIView):
    
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
  

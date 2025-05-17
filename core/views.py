from django.shortcuts import render,redirect
from django.http import HttpResponse
from core.models import *
from django.contrib import messages

# Create your views here.

def institution_form(request):
    if request.method == "POST":
        data = request.POST
        
        
        name = data.get('name')
        if not Institution.objects.filter(name=name).exists():
            address = data.get('address')
            state = data.get('state')
            pincode = data.get('pincode')
            contact_person_name = data.get('contact_person_name')
            email = data.get('contact_person_email')
            mobile = data.get('contact_person_mobile')
            
            Institution.objects.create(
                name=name, 
                address=address,
                state=state,
                pincode=pincode,
                contact_person_name=contact_person_name,
                email=email,
                mobile=mobile
            )
            
            messages.success(request, "Institution registered successfully!")
            return redirect("index")
        else:
            messages.info(request, "Institution already exists")
            return render(request,'institution.html')

    else:
        return render(request,'institution.html')
    

def index(request):
    return render(request,'index.html')
    
def learner_form(request):
    if request.method == "POST":
        data = request.POST
        
        name = data.get('name')
        email = data.get('email')
        mobile = data.get('mobile')
        institution_name = data.get('institution')
        course = data.get('course')
        batch = data.get('batch') 
        if Learner.objects.filter(email=email).exists():
            messages.info(request, "Learner with this email already exists.")
            return redirect('learner')
        
        instance = Institution.objects.get(name = institution_name)
        Learner.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            institution=instance,
            course=course,
            batch=batch

        )
        messages.success(request, "Learner registered successfully!")
        return redirect('index')
    else:
        institution = Institution.objects.all()
        context = {
            'institutions': institution
        }
        return render(request, 'learner.html', context)
    
def assessor(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        mobile = data.get('mobile')
        institution_name = data.get('institution')
        role = data.get('role')
        if Assessor.objects.filter(email=email).exists():
            messages.info(request, "Assessor with this email already exists.")
            return redirect('assessor')
        Assessor.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            institution= Institution.objects.get(name = institution_name),
            role=role
        )
        messages.success(request, "Assessor registered successfully!")
        return redirect('index')

    else:
        institution = Institution.objects.all()
        context = {'institutions': institution}
        return render(request, 'assessor.html', context)

def summary(request):
    learners = Learner.objects.count()
    assessors = Assessor.objects.count()
    institutions = Institution.objects.count()

    data = {
        'total_learners': learners,
        'total_assessors': assessors,
        'total_institutions':institutions,
    }
    return render(request,'summary.html',context = data)       


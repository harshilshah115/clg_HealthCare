from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from HealthCare.models import register,doctor,medicines

# Create your views here.

def submit_register(request):
    if request.method == 'POST':
        fname=request.POST.get('txtfullName')
        dob=request.POST.get('txtdob')
        age=request.POST.get('txtage')
        emil=request.POST.get('txtemail')
        phone=request.POST.get('txtphone')
        uname=request.POST.get('txtusername')
        pasword=request.POST.get('txtpassword')
        cpasword=request.POST.get('txtconfirmPassword')
        store=register(fullname_reg=fname,dob_reg=dob,age_reg=age,email_reg=emil,phono_reg=phone
                       ,username_reg=uname,password_reg=pasword,cpassword_reg=cpasword)
        store.save()
        return redirect('register')
    else:
        # If it's a GET request, render the registration page
        return render(request, 'registration.html')
    
def submit_login(request):
    if request.method == 'POST':
        uname = request.POST.get('txtuname')
        pas = request.POST.get('txtpwd')

        # Query the database for the user with the provided username and password
        try:
            user = register.objects.get(username_reg=uname, password_reg=pas)
            # Store the username in the session
            request.session['username'] = uname
            # If the user is found, redirect to the desired page
            return redirect('home')  # Replace 'register' with the correct URL name
        except register.DoesNotExist:
            # If no user matches, return an error message
            return HttpResponse("Username or password is incorrect")

    # If the request method is not POST, you might want to redirect or show the login page
    return render(request, 'login.html')


def submit_home(request):
    # Retrieve the username from the session
    username = request.session.get('username')
    try:
        profiles = register.objects.get(username_reg=username)
    except register.DoesNotExist:
        profiles = None

    # Fetch all doctor data
    doctordata = doctor.objects.all()
    
    # Pass the profiles to the template context (Key:value)
    # Pass both the profiles and doctor data to the template context
    return render(request, 'home.html', {'profiles': profiles, 'doctordata': doctordata})
    
def submit_profile(request):
    return render(request, 'profile.html')

def submit_update_profile(request):
   # Retrieve the username from the session
    username = request.session.get('username')
    
    try:
        # Fetch the user's profile based on the stored username
        user_profile = register.objects.get(username_reg=username)

        if request.method == 'POST':
            # Update the profile fields with form data
            user_profile.fullname_reg = request.POST.get('txtfullName')
            user_profile.age_reg = request.POST.get('txtage')
            user_profile.gender_reg = request.POST.get('txtgender')
            user_profile.dob_reg = request.POST.get('txtdob')
            user_profile.email_reg = request.POST.get('txtemail')
            user_profile.phono_reg = request.POST.get('txtphone')
            if request.FILES.get('txtphoto'):
                user_profile.image_reg = request.FILES.get('txtphoto')
            
            # Save the updated profile
            user_profile.save()
            return redirect('home')

        else:
            # If it's a GET request, prepopulate the form with existing data
            return render(request, 'profile.html', {'profile': user_profile})

    except register.DoesNotExist:
        # Handle the case where the user's profile doesn't exist
        return HttpResponse("Profile not found")

@csrf_exempt
@login_required
def upload_report(request):
    if request.method == 'POST' and request.FILES.get('report'):
        username = request.session.get('username')
        try:
            user_profile = register.objects.get(username_reg=username)
            user_profile.report = request.FILES['report']
            user_profile.save()
            return HttpResponse("File uploaded successfully")
        except register.DoesNotExist:
            return HttpResponse("User does not exist", status=404)
    return HttpResponse("File upload failed", status=400)

def medicen(request):
    # Retrieve the username from the session
    username = request.session.get('username')
    try:
        user_profile = register.objects.get(username_reg=username)
        customer_name = user_profile.fullname_reg
    except register.DoesNotExist:
        customer_name = 'Unknown'

    medicendata = medicines.objects.all()
    
    # Pass the customer_name to the template
    return render(request, 'medicen.html', {'medicendata': medicendata, 'customer_name': customer_name})


@login_required
def submit_logout(request):
    logout(request)
    request.session.flush()  # Clear the session data
    return redirect(request,'login.html')



#import csv
from django.shortcuts import render
import pandas as pd
from .models import User
from django.http import HttpResponse

CSV_FILE_PATH = 'crimes/ipc_crimes.csv'

# View for inputting the IPC Section code and fetching IPC details
def ipc_input_view(request):
    if request.method == "POST":
        if 'ipc' in request.POST:
            section_code = request.POST.get("ipc")
            if section_code:
                #genre_name = EMOTION_GENRE.get(emotion)
                df = pd.read_csv(CSV_FILE_PATH)
                ipc_details = df[df['Section'].str.contains(section_code, case=False, na=False)]
                #ipc_details = ipc_details.sample(frac=1).reset_index(drop=True)
                ipc_list = ipc_details.to_dict(orient='records')
                return render(request, 'crime_details.html', {
                    'section_code': section_code,
                    'ipc': ipc_list,
                    
                })
        else:
            return HttpResponse("Section not found or IPC details unavailable.", status=404)

    return render(request, 'input_ipc.html')

def view(request):
    return render(request, 'test.html')

def crime_input_view(request):
    return render(request, 'input_ipc.html')

def log_in(request):
    ve = User.objects.filter(is_authenticated=True).first
    global val
    if ve==True:
        val=ve
        context = {
            'user': val,
        }
        return redirect('home')
    elif request.method == 'POST':
        email = request.POST.get('mail')
        pas = request.POST.get('password')
        val = User.objects.filter(email=email).first()
        
        if val:  
            if pas == val.password:  
                val.is_authenticated=True
                val.save()
                
                context = {
                    'user': val,
                }
                
                print(val)
                return redirect('home')
            else:
                context = {
                    'msg': 'Incorrect password'
                }
                
                return render(request, 'login.html', context)
        else:
            context = {
                'msg': 'Email not found.Please Register'
            }
            return render(request, 'login.html', context)
    
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        uname = request.POST['username']
        age = request.POST['age']
        emailid = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        
        val = User.objects.filter(email=emailid).first()
        
        if val: 
            context = {
                'msg': 'Email exists. Please change the email.'
            }
            return render(request, 'register.html', context)
        else:
            if pass1 == pass2:
                User(username=uname, firstname=fname, lastname=lname, age=age, email=emailid, password=pass2).save()
                return redirect('success')  
            else:
                context = {
                    'msg': 'Passwords do not match'
                }
                return render(request, 'register.html', context)
    
    return render(request, 'register.html')

def logout(request, idd):
    global val
    val = User.objects.get(id=idd)
    val.is_authenticated=False
    val.save()
    
    return redirect('home')
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from authentication.models import detail, answer, question
from ML_Model.models import Model
from datetime import datetime

# Create your views here.


def home(request):
    # print(user.first_name)
    if request.user.is_authenticated:

        return render(request, 'home.html')
    else:
        return redirect('signin')


def signup(request):
    try:
        if request.method == "POST":

            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            cpassword = request.POST.get('cpassword')

            if password != cpassword:
                messages.error(request, 'Passwords does not match :(')
                return redirect('signup')

            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()

            data = detail(fname=fname, lname=lname,
                          username=username, email=email)
            data.save()
            messages.success(
                request, 'Your account is successfully created! Signin here :)')

            return redirect('signin')
    except:
        messages.success(request, 'Username already exist! Signin here :)')
        return redirect('signin')

    return render(request, 'signup.html')


def signin(request):
    try:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                fname = user.get_full_name
                name = user.get_username
                print(name)
                print(1)

                login(request, user)

                data = {'email': username}

                return render(request, 'home.html', data)
            else:
                messages.error(request, 'Invalid credentials :(')
                return redirect('signin')

    except:
        return redirect('signin')

    return render(request, 'signin.html')


def signout(request):
    logout(request)
    return redirect('signin')


def profile(request, id):
    if request.user.is_authenticated and request.user.username==id:

        
        query1 = f"SELECT * FROM authentication_detail where username='{id}';"
        data1 = detail.objects.raw(query1)
        query2 = f"SELECT * FROM authentication_answer where username='{id}' ORDER BY id DESC;"
        data2 = answer.objects.raw(query2)
        data = {
            'details': data1,
            'tests': data2
        }

        return render(request, 'profile.html', data)
    
    elif request.user.is_authenticated and request.user.username!=id:
        query1 = f"SELECT * FROM authentication_detail where username='{id}';"
        data1 = detail.objects.raw(query1)
        data = {
            'details': data1,
        }
        return render(request,'profile.html',data)
    else:
        return redirect('signin')


def quiz(request):
    try:
        if request.method == "POST":
            question1 = int(request.POST.get('question1'))
            question2 = int(request.POST.get('question2'))
            question3 = int(request.POST.get('question3'))
            question4 = int(request.POST.get('question4'))
            question5 = int(request.POST.get('question5'))
            question6 = int(request.POST.get('question6'))
            question7 = int(request.POST.get('question7'))
            question8 = int(request.POST.get('question8'))
            question9 = int(request.POST.get('question9'))
            question10 = int(request.POST.get('question10'))
            values = [question1, question2, question3, question4, question5,
                    question6, question7, question8, question9, question10]

            username = request.user.username
            # print(username, 1, 2)

            model_ = Model()
            classifier = model_.svm_classifier()
            prediction = classifier.predict([values])
            # print(prediction[0])
            if prediction[0] == 0:
                result = 'No Depression'
            if prediction[0] == 1:
                result = 'Mild Depression'
            if prediction[0] == 2:
                result = 'Moderate Depression'
            if prediction[0] == 3:
                result = 'Moderately severe Depression'
            if prediction[0] == 4:
                result = 'Severe Depression'

            data = answer(username=username, answer1=question1+1, answer2=question2+1, answer3=question3+1, answer4=question4+1, answer5=question5+1,
                        answer6=question6+1, answer7=question7+1, answer8=question8+1, answer9=question9+1, answer10=question10+1, date=datetime.now(), result=result)
            data.save()

            query = "SELECT 'id','questions' FROM authentication_question ORDER BY id;"
            data1 = question.objects.all()
            totalscore=sum(values)
            last=values.pop()
            mylist=zip(data1,values)
            
            data={
                'answers':result,
                'last':last,
                'questions':mylist,
                'score':totalscore
            }

            return render(request,'result.html',data)
        

    except:
        return redirect('quiz')

    if request.user.is_authenticated:
        query = "SELECT 'id','questions' FROM authentication_question ORDER BY id;"
        data1 = question.objects.all()

        data = {
            'question': data1
        }
        return render(request, 'quiz.html', data)
    else:
        return redirect('signin')

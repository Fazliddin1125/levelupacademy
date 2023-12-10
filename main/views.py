from django.http import HttpResponse
from django.views import View
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .models import Course, Customer, CheckTest, CheckQuestion, Test, Question

class IndexView(View):
    def get(self, request):
        courses = Course.objects.filter(language='english')
        return render(request, 'base.html', {'courses': courses})
    def post(self, request):
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        course_num = request.POST['course']
        print('valid')
        if len(name) > 2 and len(phone_number) > 7 and course_num != '':
            print('validateed')
            course = Course.objects.all().filter(name=course_num)
            Customer.objects.create(
                name=name,
                phone_number=phone_number,
                email=email,
                course=course[0],
                checked=False
            )
        courses = Course.objects.filter(language='english')
        return render(request, 'base.html', {'courses': courses})


class OfertaView(View):
    def get(self, request):
        return render(request, 'oferta.html')

class IndexUzView(View):
    def get(self, request):
        courses = Course.objects.filter(language='uzbek')
        return render(request, 'uzbek.html', {'courses': courses})
    def post(self, request):
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        course_num = request.POST['course']
        print('valid')
        if len(name) > 2 and len(phone_number) > 7 and course_num != '':
            print('validateed')
            course = Course.objects.all().filter(name=course_num)
            Customer.objects.create(
                name=name,
                phone_number=phone_number,
                email=email,
                course=course[0],
                checked=False
            )
        courses = Course.objects.filter(language='uzbek')
        return render(request, 'uzbek.html', {'courses': courses})

class IndexGerView(View):
    def get(self, request):
        courses = Course.objects.filter(language='german')
        return render(request, 'german.html', {'courses': courses})
    def post(self, request):
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        course_num = request.POST['course']
        print('valid')
        if len(name) > 2 and len(phone_number) > 7 and course_num != '':
            print('validateed')
            course = Course.objects.all().filter(name=course_num)
            Customer.objects.create(
                name=name,
                phone_number=phone_number,
                email=email,
                course=course[0],
                checked=False
            )
        courses = Course.objects.filter(language='german')
        return render(request, 'german.html', {'courses': courses})

class IndexTestView(View):
    def get(self, request):
        tests = Test.objects.all()
        context = {
            'tests': tests
        }
        return render(request, 'index.html', context)



def test(request, test_id):
    test = get_object_or_404(Test, id=test_id)

    questions = Question.objects.filter(test=test)
    if request.method == 'POST':
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            phone_number = request.POST['phone_number']

        except:
            return HttpResponse('Ism, Familiya, telefon raqam kiritish majburiy')
        check_test = CheckTest.objects.create(
            test=test,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number
        )
        question_count = 0
        true_question_count = 0
        for index, question in enumerate(questions):
            question_count = question_count + 1

            try:
                given_answer = request.POST[str(question.id)]
            except:
                given_answer = 'None'
            if given_answer == question.true_answer:
                is_true = True
                true_question_count = true_question_count + 1
            else:
                is_true = False
            check_question = CheckQuestion.objects.create(
                check_test=check_test,
                question=question,
                given_answer=given_answer,
                true_answer=question.true_answer,
                is_true=is_true
            )
            check_question.save()
        user_passed = False
        percentage = true_question_count*100//question_count
        if percentage >= test.percentage:
            user_passed = True
        level = ''
        if check_test.test.title == 'english':
            if true_question_count >= 40:
                level = 'Intermediate'
            elif true_question_count >= 30:
                level = 'Pri-Intermediate'
            elif true_question_count >= 20:
                level = 'Elementary'
            elif true_question_count < 20:
                level = 'Beginner'
        elif check_test.test.title == 'german':
            if true_question_count >= 50:
                level = 'B1'
            elif true_question_count >= 40:
                level = 'A2'
            elif true_question_count >= 30:
                level = 'A1'
            elif true_question_count < 30:
                level = 'A1'
        check_test.level = level
        check_test.found_question = true_question_count
        check_test.user_passed = user_passed
        check_test.percentage = percentage
        check_test.save()
        return redirect('check', check_test.id)





    context = {
        'test': test,
        'questions': questions
    }
    return render(request, 'test.html', context)


class CheckTestView(View):
    def get(self, request, check_test_id):
        check_test = get_object_or_404(CheckTest, id=check_test_id)
        check_questions = CheckQuestion.objects.filter(check_test=check_test)
        print(check_test.test)
        level = ''
        if check_test.test.title == 'english':
            if check_test.found_question >= 40:
                level = 'Intermediate'
            elif check_test.found_question >= 30:
                level = 'Pri-Intermediate'
            elif check_test.found_question >= 20:
                level = 'Elementary'
            elif check_test.found_question < 20:
                level = 'Beginner'
        elif check_test.test.title == 'german':
            if check_test.found_question >= 50:
                level = 'B1'
            elif check_test.found_question >= 40:
                level = 'A2'
            elif check_test.found_question >= 30:
                level = 'A1'
            elif check_test.found_question < 30:
                level = 'A1'
        context = {
            'check_test': check_test,
            'check_questions': check_questions,
            'level': level
        }
        return render(request, 'check_test.html', context)
    
class LoginView(View):
    def get(self, requset):

        login_form = AuthenticationForm()
        context = {
            'form': login_form
        }
        return render(requset, 'login.html', context)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        context = {
            'form': login_form
        }

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
           
            return redirect('list')

        else:
            return render(request, 'login.html', context)   

from django.contrib.auth.mixins import LoginRequiredMixin
class ListView(LoginRequiredMixin, View):
    def get(self, request):
        check_test = CheckTest.objects.all().order_by('-created_at')
        customers = Customer.objects.all().order_by('-created_at')
        context = {
            'checks': check_test,
            'customers': customers
        }
        return render(request, 'list.html', context)
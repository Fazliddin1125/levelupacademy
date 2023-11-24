from django.shortcuts import render
from django.views import View
from .models import Course, Customer
class IndexView(View):
    def get(self, request):
        courses = Course.objects.all()
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
        courses = Course.objects.all()
        return render(request, 'base.html', {'courses': courses})



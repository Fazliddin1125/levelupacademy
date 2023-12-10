from django.contrib import admin
from .models import Course, Customer
# Register your models here.

from .models import CheckTest, CheckQuestion, Question, Test, Category
# Register your models here.
admin.site.register([CheckQuestion, CheckTest, Question, Test, Category])
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['price']
    search_fields = ['name', 'price']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'course']
    list_filter = ['checked']
    search_fields = ['name']

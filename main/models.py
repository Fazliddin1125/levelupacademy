from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50)
    month = models.FloatField()
    price = models.FloatField()
    student = models.IntegerField()
    title = models.CharField(max_length=150, default='Lorem ipsum, dolor sit amet consectetur adipisicing elit. Aspernatur, fuga?')
    language = models.CharField(max_length=20, default='english')
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=25)
    email = models.EmailField(null=True, blank=True)
    checked = models.BooleanField(default=False, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Test(models.Model):
   
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    spending_time = models.PositiveBigIntegerField(default=5)
    percentage = models.PositiveBigIntegerField(default=60)


    def __str__(self):
        return self.title
class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.TextField()
    TEST_CHOICES = (
        ('a', "a"),
        ('b', "b"),
        ('c', "c"),
        ('d', "d")
    )

    a = models.CharField(max_length=600)
    b = models.CharField(max_length=600)
    c = models.CharField(max_length=600)
    d = models.CharField(max_length=600)
    true_answer = models.CharField(max_length=1, help_text="E.x: a", choices=TEST_CHOICES)

    def __str__(self):
        return self.question

#  <input value="a"  name="{{ q.id }}" class="form-check-input" id="{{ q.id }}-a" type="radio" >-->
# <!--                <label for="{{ q.id }}-a" > {{q.a}}</label>-->

class CheckTest(models.Model):
    first_name = models.CharField(max_length=50)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    found_question = models.PositiveBigIntegerField(default=0)
    user_passed = models.BooleanField(default=False)
    percentage = models.PositiveBigIntegerField(default=0)
    level = models.CharField(max_length=25, default='beginner')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name} -- {self.percentage}"

class CheckQuestion(models.Model):
    check_test = models.ForeignKey(CheckTest, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    given_answer = models.CharField(max_length=1)
    true_answer = models.CharField(max_length=1)
    is_true = models.BooleanField(default=False)
from django.db import models
from student.models import Student
from teacher.models import Teacher  # ✅ to link course to a teacher


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    question_number = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.course_name


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField(default=1)
    question = models.CharField(max_length=600)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    cat = (
        ('Option1', 'Option1'),
        ('Option2', 'Option2'),
        ('Option3', 'Option3'),
        ('Option4', 'Option4'),
    )
    answer = models.CharField(max_length=200, choices=cat)
    question_file = models.FileField(
        upload_to='question_files/',
        null=True,
        blank=True,
        help_text="Upload question file (PDF, PPT, DOC, XLS)"
    )

    def __str__(self):
        return self.question


class StudentAnswer(models.Model):
    """✅ New model — store each student's answer for question-wise evaluation."""
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    marks_obtained = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.student.user.username} - {self.question}"


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} - {self.exam}"
# exam/models.py
from student.models import Student

class StudentAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    marks_obtained = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.student.user.username} - {self.question}"

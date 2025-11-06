from django import forms
from django.contrib.auth.models import User
from . import models


class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(
        max_length=500,
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 30})
    )


class TeacherSalaryForm(forms.Form):
    salary = forms.IntegerField()


class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ['course_name', 'question_number', 'total_marks']


class QuestionForm(forms.ModelForm):
    # Dropdown for selecting course
    courseID = forms.ModelChoiceField(
        queryset=models.Course.objects.all(),
        empty_label="Select Course",
        to_field_name="id"
    )

    class Meta:
        model = models.Question
        fields = [
            'courseID',
            'question',
            'marks',
            'option1',
            'option2',
            'option3',
            'option4',
            'answer',
            'question_file',  # ✅ file upload field
        ]
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 50})
        }

    # ✅ Fix: Properly save the selected course and file upload
    def save(self, commit=True):
        question = super().save(commit=False)
        course_obj = self.cleaned_data.get('courseID')
        if course_obj:
            question.course = course_obj  # Correct ForeignKey assignment
        if commit:
            question.save()
        return question

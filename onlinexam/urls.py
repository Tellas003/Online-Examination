from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView
from django.conf import settings
from django.conf.urls.static import static

from exam import views as exam_views
from teacher import views as teacher_views

urlpatterns = [

    # Main Pages
    path('admin/', admin.site.urls),
    path('teacher/', include('teacher.urls')),
    path('student/', include('student.urls')),
    path('', exam_views.home_view, name=''),

    # Authentication
    path('logout', LogoutView.as_view(template_name='exam/logout.html'), name='logout'),
    path('afterlogin', exam_views.afterlogin_view, name='afterlogin'),
    path('contactus', exam_views.contactus_view),

    # Admin Section
    path('adminclick', exam_views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='exam/adminlogin.html'), name='adminlogin'),
    path('admin-dashboard', exam_views.admin_dashboard_view, name='admin-dashboard'),

    # Teacher management
    path('admin-teacher', exam_views.admin_teacher_view, name='admin-teacher'),
    path('admin-view-teacher', exam_views.admin_view_teacher_view, name='admin-view-teacher'),
    path('update-teacher/<int:pk>', exam_views.update_teacher_view, name='update-teacher'),
    path('delete-teacher/<int:pk>', exam_views.delete_teacher_view, name='delete-teacher'),
    path('admin-view-pending-teacher', exam_views.admin_view_pending_teacher_view, name='admin-view-pending-teacher'),
    path('admin-view-teacher-salary', exam_views.admin_view_teacher_salary_view, name='admin-view-teacher-salary'),
    path('approve-teacher/<int:pk>', exam_views.approve_teacher_view, name='approve-teacher'),
    path('reject-teacher/<int:pk>', exam_views.reject_teacher_view, name='reject-teacher'),

    # Student management
    path('admin-student', exam_views.admin_student_view, name='admin-student'),
    path('admin-view-student', exam_views.admin_view_student_view, name='admin-view-student'),
    path('update-student/<int:pk>', exam_views.update_student_view, name='update-student'),
    path('delete-student/<int:pk>', exam_views.delete_student_view, name='delete-student'),
    path('admin-view-student-marks', exam_views.admin_view_student_marks_view, name='admin-view-student-marks'),
    path('admin-view-marks/<int:pk>', exam_views.admin_view_marks_view, name='admin-view-marks'),
    path('admin-check-marks/<int:pk>', exam_views.admin_check_marks_view, name='admin-check-marks'),

    # Course management
    path('admin-course', exam_views.admin_course_view, name='admin-course'),
    path('admin-add-course', exam_views.admin_add_course_view, name='admin-add-course'),
    path('admin-view-course', exam_views.admin_view_course_view, name='admin-view-course'),
    path('delete-course/<int:pk>', exam_views.delete_course_view, name='delete-course'),

    # Question management
    path('admin-question', exam_views.admin_question_view, name='admin-question'),
    path('admin-add-question', exam_views.admin_add_question_view, name='admin-add-question'),
    path('admin-view-question', exam_views.admin_view_question_view, name='admin-view-question'),
    path('view-question/<int:pk>', exam_views.view_question_view, name='view-question'),
    path('delete-question/<int:pk>', exam_views.delete_question_view, name='delete-question'),

    # Teacher View - See student marks
    path('teacher/student-marks', teacher_views.teacher_student_marks_view, name='teacher-student-marks'),

    # Admin View - See students under each teacher
    path('admin/teacher-student-marks', exam_views.admin_teacher_student_marks_view, name='admin-teacher-student-marks'),

    # Custom Admin View - Teacher–Student Marks
path('dashboard/teacher-student-marks', exam_views.admin_teacher_student_marks_view, name='admin-teacher-student-marks'),

# Default Django Admin — keep this last
path('admin/', admin.site.urls),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

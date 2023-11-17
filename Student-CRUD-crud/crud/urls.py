from django.urls import include, path
from django.contrib import admin
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('', views.StudentList.as_view(), name='student_list'),
    path('new/', views.StudentCreate.as_view(), name='student_new'),
    path('<int:pk>/edit/', views.StudentUpdate.as_view(), name='student_edit'),
    path('<int:pk>/delete/', views.StudentDelete.as_view(), name='student_delete'),
]

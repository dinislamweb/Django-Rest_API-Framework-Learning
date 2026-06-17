from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees',views.EmployeeViewSet,basename='employee')

urlpatterns = [
    path('students/',views.studentsView),
    path('students/<int:pk>/',views.StudentDetailView),
    # path('employees/',views.Employees.as_view()), 
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
    path('',include(router.urls)),
    
    # class based views
    path('blog/',views.BlogsView.as_view()),
    path('comment/',views.CommentView.as_view()),
    
    # primary key based views
    path('blog/<int:pk>/',views.BlogDetailView.as_view()),
    path('comment/<int:pk>/',views.CommentDetailView.as_view())
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('all-students/', views.all_students, name='all-students'),
    path('all-teachers/', views.all_teachers, name='all-teachers'),

    path('logout/', views.logout, name='logout'),
    path('faq/', views.faq, name='faq'),
    path('about/', views.faq, name='about'),

    path('predict/', views.grade_prediction, name='grade-prediciton'),
    path('result/', views.result, name='result')
]
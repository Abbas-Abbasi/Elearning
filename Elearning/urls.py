from allauth.account.views import PasswordResetDoneView
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from courses import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    #
    path('courses/', views.courses, name="courses"),
    path('courses/<int:course_id>/', views.course_detail, name="course_detail"),
    path('courses/english/', views.english, name="english"),
    path('courses/math/', views.math, name="math"),

    path('tinymce/', include('tinymce.urls')),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='account_login'),

    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('password_reset/', views.password_reset, name='password_reset'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from application import views

urlpatterns = [
    # --- Landing & Core ---
    path('', views.Home, name='home'),
    path('site/', views.SiteView, name='site'),
    path('index/', views.index, name='index'),

    # --- Authentication (Clients) ---
    path('register/', views.RegisterView, name='register'),
    path('login/', views.LoginView, name='login'),

    # --- Authentication (Workers/Professionals) ---
    path('reg/', views.RegView, name='reg'),  # Professional Registration
    path('login/worker/', views.WorkerLoginView, name='worker_login'),  # Professional Login

    # --- Shared Auth ---
    path('logout/', views.LogoutView, name='logout'),
    path('forgot-password/', views.ForgotPassword, name='forgot-password'),
    path('password-reset-sent/<str:reset_id>/', views.PasswordResetSent, name='password-reset-sent'),
    path('reset-password/<str:reset_id>/', views.ResetPassword, name='reset-password'),

    # --- Role-Specific Dashboards ---
    path('dashboard/', views.dashboard, name='dashboard'),  # For Workers
    path('client/dashboard/', views.client_dashboard, name='client_dashboard'),  # For Clients

    # --- Service Actions ---
    path('contact/', views.contact, name='contact'),
    path('workers/', views.workers, name='workers'),
    path('profile/', views.profile, name='profile'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('join/', views.RoleSelection, name='join'), # The selection page
    path('register/', views.RegisterView, name='register'), # Client Form
    path('reg/', views.RegView, name='reg'), # Worker Form
    path('join/guide/<str:role>/', views.OnboardingGuide, name='onboarding_guide'),
    # path('print/<int:id>/', views.print_appointment, name='print_appointment'),
    # path('appointmentapi/', views.appointmentapi, name='appointmentapi'),
    # path('mpesaapi/', views.mpesaapi, name='mpesaapi'),

]



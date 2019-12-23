from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Sum, Count
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from oddaj_app.models import Donations, Institution, Category


class LandingPage(View):
    def get(self, request):
        num_of_bags = Donations.objects.aggregate(Sum('quantity'))['quantity__sum']
        num_of_institutions = Donations.objects.aggregate(Count('institution'))['institution__count']

        foundations = Institution.objects.filter(type="Fundacja")
        gov_organizations = Institution.objects.filter(type="Organizacja")
        collections = Institution.objects.filter(type="Zbiorka")

        return render(request, 'index.html', {'bags': num_of_bags, 'institutions': num_of_institutions,
                                              "foundations": foundations, "gov_organizations": gov_organizations,
                                              "collections": collections})


class AddDonation(LoginRequiredMixin, View):
    login_url = "/login"

    def get(self, request):
        categories = Category.objects.all()
        organizations = Institution.objects.all()
        return render(request, 'form.html', {'categories': categories, 'organizations': organizations})


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('landing_page'))

        else:
            return redirect(reverse('register'))


class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            new_user = User.objects.create_user(username=email, email=email, password=password, first_name=name,
                                                last_name=surname)
        return redirect(reverse('login'))


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("landing_page"))


class UserProfileView(View):
    def get(self, request):
        user = request.user
        return render(request, 'user_profile.html', {'user': user})

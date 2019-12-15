from django.db.models import Sum, Count
from django.shortcuts import render
from django.views import View
from oddaj_app.models import Donations


class LandingPage(View):
    def get(self, request):
        num_of_bags = Donations.objects.aggregate(Sum('quantity'))['quantity__sum']
        num_of_institutions = Donations.objects.aggregate(Count('institution'))['institution__count']
        return render(request, 'index.html', {'bags': num_of_bags, 'institutions': num_of_institutions})


class AddDonation(View):
    def get(self, request):
        return render(request, 'form.html')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')


class Register(View):
    def get(self, request):
        return render(request, 'register.html')

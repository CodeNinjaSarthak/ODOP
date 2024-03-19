from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "core/index.html")


#
def account_view(request):
    # return render(request, 'core/account.html')
    return render(request, "userauths/sign-up.html")


def index_view(request):
    return render(request, "core/index.html")


#
def product_view(request):
    return render(request, "core/products.html")


def cart_view(request):
    return render(request, "core/cart.html")


def explore_view(request):
    return render(request, "core/explore.html")


def anaant_view(request):
    return render(request, "core/anaant.html")


def kathua_view(request):
    return render(request, "core/kathua.html")


def anantnag_view(request):
    return render(request, "core/anantnag.html")


def budgam_view(request):
    return render(request, "core/budgam.html")


def jammu_view(request):
    return render(request, "core/jammu.html")


def rajouri_view(request):
    return render(request, "core/rajouri.html")


def srinagar_view(request):
    return render(request, "core/srinagar.html")


def shopian_view(request):
    return render(request, "core/shopian.html")


def baramulla_view(request):
    return render(request, "core/baramulla.html")

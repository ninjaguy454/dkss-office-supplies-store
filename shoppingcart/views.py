from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.db.models import Sum
from _decimal import Decimal

# Create your views here.

now = timezone.now()


def home(request):
    return render(request, 'shoppingcart/home.html', {'shoppingcart': home})

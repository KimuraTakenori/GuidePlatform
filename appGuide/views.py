
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from .models import *
from .forms import SearchGuideForm

def search_guide(request):

    search_guide_form = SearchGuideForm()

    return render(request,
                  'appGuide/search_test1_1.html',
                  { "search_guide_form" : search_guide_form })



def testview1(request):

    return render(request,
                  'appGuide/testview1_1.html',
                  {})

def testview2(request):

    return render(request,
                  'appGuide/testview2_1.html',
                  {})
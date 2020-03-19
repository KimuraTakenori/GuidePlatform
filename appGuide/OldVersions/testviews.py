# Create your views here.

from django.shortcuts import render


def testview1(request):

    return render(request,
                  'appGuide/testview1_1.html',
                  {})

def testview2(request):

    return render(request,
                  'appGuide/testview2_1.html',
                  {})

def testview3(request):

    return render(request,
                  'appGuide/testview3_1.html',
                  {})

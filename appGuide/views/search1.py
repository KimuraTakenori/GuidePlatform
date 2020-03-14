
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import ListView

from appGuide.models import *
from appGuide.forms import SearchGuideForm


class GuideTimeListView(ListView):
    model = GuidableTime
    template_name = "appGuide/guidetime_list1.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        if "search_form" in vars(self):
            search_form = self.search_form
        else:
            search_form = SearchGuideForm()
        context[ "search_form" ] = search_form

        return context

    def get_queryset(self):

        queryset = self.model.objects.none()

        if "search_form" in vars(self) and self.search_form.is_valid():
            queryset = self.model.objects.all()

        return queryset

    def post(self, request, *args, **kwargs):

        self.search_form = SearchGuideForm(data = self.request.POST)
        return self.get(request, *args, **kwargs)




class GuideListView(ListView):
    model = Guide
    template_name = "appGuide/guide_list1.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        if "search_form" in vars(self):
            search_form = self.search_form
        else:
            search_form = SearchGuideForm()
        context[ "search_form" ] = search_form

        return context

    def get_queryset(self):

        queryset = self.model.objects.none()

        if "search_form" in vars(self) and self.search_form.is_valid():
            queryset = self.model.objects.all()

        return queryset

    def post(self, request, *args, **kwargs):

        self.search_form = SearchGuideForm(data = self.request.POST)
        return self.get(request, *args, **kwargs)



def search_guide(request):

    search_guide_form = SearchGuideForm()

    return render(request,
                  'appGuide/search_test1_2.html',
                  { "search_guide_form" : search_guide_form })
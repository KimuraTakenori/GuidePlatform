
from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from django.db.models import Q

from appGuide.models import *
from appGuide.forms.search_form import SearchGuideForm


class GuidableTimeListView(ListView):
    model = GuidableTime
    template_name = "appGuide/guidetime_list1_3.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        if "search_form" in vars(self):
            search_form = self.search_form
        else:
            search_form = SearchGuideForm()
        context[ "search_form" ] = search_form

        # print(search_form.place_choices, type(search_form.place_choices), dir(search_form.place_choices))
        # print(vars(search_form))
        # print(vars(SearchGuideForm)) # .place_choices)

        return context

    def get_queryset(self):

        queryset = self.model.objects.none()

        if "search_form" in vars(self) and self.search_form.is_valid():
            queryset = search_guidable_times(self.search_form.cleaned_data)
            # pprint(self.search_form.cleaned_data)
        # else:
            # print("Invalid!")
            # print("search_form" in vars(self))

        return queryset

    def post(self, request, *args, **kwargs):

        # pprint(self.request.POST)
        # pprint(self.request.POST.getlist("place_choices"))
        self.search_form = SearchGuideForm(data = self.request.POST)
        return self.get(request, *args, **kwargs)


def search_guidable_times(iform_input):

    # pprint(iform_input)

    queryset1 = GuidableTime.objects.filter(
        Q(guidable_time_from__gte = iform_input[ "req_time_from" ],
          guidable_time_from__lt  = iform_input[ "req_time_to"],
          guide__guidablespot__spot__in = iform_input[ "place_choices" ],) |
        Q(guidable_time_to__gte   = iform_input[ "req_time_from" ],
          guidable_time_to__lt    = iform_input[ "req_time_to" ],
          guide__guidablespot__spot__in = iform_input[ "place_choices" ])).distinct()

    return queryset1


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
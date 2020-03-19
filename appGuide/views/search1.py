
# The following may be used for extracting portion of available time frames:
# pip install portion
# https://github.com/AlexandreDecan/portion


from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, TemplateView
from django.db.models import Q

from django.utils.timezone import localtime

from appGuide.models import *
from appGuide.forms.search_form import SearchGuideForm

from ..modules.search_guidable_time_intervals1_1 import  extract_guidable_time_intervals

from pprint import pprint

class GuidableTimeIntervalView(TemplateView):
    model = GuidableTime
    template_name = "appGuide/guidetime_interval1_1.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        if "search_form" in vars(self):
            search_form = self.search_form
        else:
            search_form = SearchGuideForm()
        context[ "search_form" ] = search_form

        if "cand_time_intvals" in vars(self):
            cand_time_intvals = self.cand_time_intvals
        else:
            cand_time_intvals = None
        context[ "cand_time_intvals" ] = cand_time_intvals

        return context

    def post(self, request, *args, **kwargs):

        self.search_form = SearchGuideForm(data = self.request.POST)

        """ Checking double-booking of a tourist not implemented yet. """

        if "search_form" in vars(self) and self.search_form.is_valid():
            guidable_times = search_guidable_times(self.search_form.cleaned_data)
            req_time_from  = self.search_form.cleaned_data[ "req_time_from" ]
            req_time_to    = self.search_form.cleaned_data[ "req_time_to"   ]
            # self.request.session[ "Request time" ] = {
            #     "from" : req_time_from.strftime("%Y/%m/%d %H:%M"),
            #     "to"   : req_time_to.strftime("%Y/%m/%d %H:%M"),
            # }
            # self.request.session.modified = True

            self.cand_time_intvals = []
            for guidable_time in guidable_times:

                intervals_info = [
                    { "interval"     : interval,
                      "interval_str" :
                         localtime(interval.lower).strftime("%Y%m%d%H%M") + "_"
                         + localtime(interval.upper).strftime("%Y%m%d%H%M")
                     } for interval in extract_guidable_time_intervals(guidable_time,
                                                                       req_time_from,
                                                                       req_time_to) ]

                self.cand_time_intvals.append(
                    { "guidable_time" : guidable_time,
                      "intervals"     : intervals_info })

            # pprint(self.cand_time_intvals)

        return self.get(request, *args, **kwargs)


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
        """ CHECK FOR ALREADY RESERVED TIMEFRAMES!!! """

        queryset = self.model.objects.none()

        if "search_form" in vars(self) and self.search_form.is_valid():
            queryset = search_guidable_times(self.search_form.cleaned_data)
            self.request.session[ "Request time" ] = {
                "from" : self.search_form.cleaned_data[ "req_time_from" ].strftime("%Y/%m/%d %H:%M"),
                "to"   : self.search_form.cleaned_data[ "req_time_to"   ].strftime("%Y/%m/%d %H:%M"),
            }
            self.request.session.modified = True
            pprint(self.request.session[ "Request time" ])

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
    # for guidable_time in GuidableTime.objects.all():
    #     print(guidable_time.guidable_time_from, guidable_time.guidable_time_to)

    queryset1 = GuidableTime.objects.filter(
        Q(guidable_time_from__gte = iform_input[ "req_time_from" ],
          guidable_time_from__lt  = iform_input[ "req_time_to"],
          guide__guidablespot__spot__in = iform_input[ "place_choices" ],) |
        Q(guidable_time_to__gte   = iform_input[ "req_time_from" ],
          guidable_time_to__lt    = iform_input[ "req_time_to" ],
          guide__guidablespot__spot__in = iform_input[ "place_choices" ],) |
        Q(guidable_time_from__lt = iform_input["req_time_from"],
          guidable_time_to__gte  = iform_input["req_time_to"],
          guide__guidablespot__spot__in=iform_input["place_choices"], )).distinct()

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
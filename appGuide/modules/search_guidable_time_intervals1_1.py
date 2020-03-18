

import portion as Interval

from django.db.models import Q
from ..models import Guide, GuidableTime, Reservation

# class GuidabTimeIntval:

def extract_guidable_time_intervals(guidable_time_obj,
                                    request_time_from, request_time_to):

    already_reservs = Reservation.objects.filter(
        Q(guidable_time__guide       = guidable_time_obj.guide,
          reservation_time_from__gte = request_time_from,
          reservation_time_from__lt  = request_time_to,
          ) |
        Q(guidable_time__guide     = guidable_time_obj.guide,
          reservation_time_to__gte = request_time_from,
          reservation_time_to__lt  = request_time_to,
          )).distinct()

    guid_intval    = Interval.open(guidable_time_obj.guidable_time_from,
                                   guidable_time_obj.guidable_time_to)
    request_intval = Interval.open(request_time_from,
                                   request_time_to)
    cand_intvals = guid_intval & request_intval

    for already_reserv in already_reservs:
        already_reserv_intval = Interval.open(already_reserv.reservation_time_from,
                                              already_reserv.reservation_time_to)
        cand_intvals -= already_reserv_intval

    return cand_intvals


    # queryset1 = GuidableTime.objects.filter(
    #     Q(guidable_time_from__gte = iform_input[ "req_time_from" ],
    #       guidable_time_from__lt  = iform_input[ "req_time_to"],
    #       guide__guidablespot__spot__in = iform_input[ "place_choices" ],) |
    #     Q(guidable_time_to__gte   = iform_input[ "req_time_from" ],
    #       guidable_time_to__lt    = iform_input[ "req_time_to" ],
    #       guide__guidablespot__spot__in = iform_input[ "place_choices" ])).distinct()


import portion as Interval

from django.db.models import Q
from ..models import Guide, GuidableTime, Reservation

# class GuidabTimeIntval:

def prelim_cand_interval(guidable_time_obj,
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

    guide_intval   = Interval.open(guidable_time_obj.guidable_time_from,
                                   guidable_time_obj.guidable_time_to)
    request_intval = Interval.open(request_time_from,
                                   request_time_to)
    cand_intval    = guide_intval & request_intval

    return already_reservs, cand_intval

def extract_guidable_time_intervals(guidable_time_obj,
                                    request_time_from, request_time_to):

    already_reservs, cand_intvals  =  prelim_cand_interval(guidable_time_obj,
                                                           request_time_from,
                                                           request_time_to)

    for already_reserv in already_reservs:
        already_reserv_intval = Interval.open(already_reserv.reservation_time_from,
                                              already_reserv.reservation_time_to)
        cand_intvals -= already_reserv_intval

    if cand_intvals.empty:
        return []
    else:
        return list(cand_intvals)

def check_avail_full_interval(guidable_time_obj,
                              request_time_from, request_time_to):

    already_reservs, cand_intvals = prelim_cand_interval(guidable_time_obj,
                                                         request_time_from,
                                                         request_time_to)

    req_intval = Interval.open(request_time_from, request_time_to)

    remain_intval = req_intval

    for already_reserv in already_reservs:
        print(remain_intval, already_reserv)
        remain_intval -= Interval.open(already_reserv.reservation_time_from,
                                       already_reserv.reservation_time_to)
        print("--->", remain_intval)

    return remain_intval == req_intval


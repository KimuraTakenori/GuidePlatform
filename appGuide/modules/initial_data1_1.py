
from appGuide.models import *
from appGuide.modules.datetime_with_timezone1 import datetime_str_localize

Gender.objects.create(gender_name = "男性")
Gender.objects.create(gender_name = "女性")
Gender.objects.create(gender_name = "その他")

Tourist.objects.create(user_sei = "与謝野",
                       user_mei = "晶子",
                       user_seifuri = "よさの",
                       user_meifuri = "あきこ",
                       user_gender = Gender.objects.get(gender_name = "女性"),
                       user_seinen = "2020-02-02",
                       user_tel = "000-1111-2345",
                       user_email = "a@a.com",
                       user_pass = "aaaa",
                       user_post = "100-0000",
                       user_address1 = "東京都",
                       user_address2 = "千代田区")
                       
Guide.objects.create(guide_sei = "真田",
                     guide_mei = "幸村",
                     guide_seifuri = "さなだ",
                     guide_meifuri = "ゆきむら",
                     guide_gender = Gender.objects.get(gender_name = "男性"),
                     guide_seinen = "2019-02-02",
                     guide_tel = "999-1111-2345",
                     guide_email = "b@b.com",
                     guide_pass = "bbbb",
                     guide_post = "100-0000",
                     guide_address1 = "東京都",
                     guide_address2 = "千代田区")

PreTourSpot.objects.create(preplace_address1 ="山形県",
                           preplace_address2 = "鶴岡市",
                           preplace_name = "羽黒山")
PreTourSpot.objects.create(preplace_address1 ="山形県",
                           preplace_address2 = "上山市",
                           preplace_name = "上山城")
PreTourSpot.objects.create(preplace_address1 ="大阪府",
                           preplace_address2 = "大阪市",
                           preplace_name = "大阪城")

Spot.objects.create(place_address1 ="山形県",
                    place_address2 = "鶴岡市",
                    place_name = "庄内藩校致道館")
Spot.objects.create(place_address1 ="山形県",
                    place_address2 = "鶴岡市",
                    place_name = "致道博物館")
Spot.objects.create(place_address1 ="山形県",
                    place_address2 = "鶴岡市",
                    place_name = "致道館")
Spot.objects.create(place_address1 ="山形県",
                    place_address2 = "鶴岡市",
                    place_name = "鶴岡カトリック教会天主堂")
Spot.objects.create(place_address1 ="山形県",
                    place_address2 = "鶴岡市",
                    place_name = "丙申堂・釈迦堂")
Spot.objects.create(place_address1 ="山形県",
                    place_address2 = "鶴岡市",
                    place_name = "荘内神社宝物殿")
Spot.objects.create(place_address1 ="山形県",
                    place_address2 = "鶴岡市",
                    place_name = "大宝館")
Spot.objects.create(place_address1 ="山形県",
                    place_address2 = "鶴岡市",
                    place_name = "藤沢周平記念館")

GuidableTime.objects.create(guide = Guide.objects.get(guide_sei = "真田",
                                                      guide_mei = "幸村"),
                            guidable_time_from = datetime_str_localize("2020-03-17 10:00"),
                            guidable_time_to   = datetime_str_localize("2020-03-17 16:00"))

GuidableSpot.objects.create(guide = Guide.objects.get(guide_sei = "真田",
                                                      guide_mei = "幸村"),
                            spot  = Spot.objects.get(place_name = "致道博物館"))



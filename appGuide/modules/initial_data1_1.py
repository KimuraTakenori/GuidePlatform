
from appGuide.models import *

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
                       user_mail = "a@a.com",
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
                     guide_mail = "b@b.com",
                     guide_pass = "bbbb",
                     guide_post = "100-0000",
                     guide_address1 = "東京都",
                     guide_address2 = "千代田区")

Preplace.objects.create(preplace_address1 = "山形県",
                        preplace_address2 = "鶴岡市",
                        preplace_name = "羽黒山")
Preplace.objects.create(preplace_address1 = "山形県",
                        preplace_address2 = "上山市",
                        preplace_name = "上山城")
Preplace.objects.create(preplace_address1 = "大阪府",
                        preplace_address2 = "大阪市",
                        preplace_name = "大阪城")

Place.objects.create(place_address1 = "山形県",
                     place_address2 = "鶴岡市",
                     place_name = "庄内藩校致道館")
Place.objects.create(place_address1 = "山形県",
                     place_address2 = "鶴岡市",
                     place_name = "致道博物館")
Place.objects.create(place_address1 = "山形県",
                     place_address2 = "鶴岡市",
                     place_name = "致道館")
Place.objects.create(place_address1 = "山形県",
                     place_address2 = "鶴岡市",
                     place_name = "鶴岡カトリック教会天主堂")
Place.objects.create(place_address1 = "山形県",
                     place_address2 = "鶴岡市",
                     place_name = "丙申堂・釈迦堂")
Place.objects.create(place_address1 = "山形県",
                     place_address2 = "鶴岡市",
                     place_name = "荘内神社宝物殿")
Place.objects.create(place_address1 = "山形県",
                     place_address2 = "鶴岡市",
                     place_name = "大宝館")
Place.objects.create(place_address1 = "山形県",
                     place_address2 = "鶴岡市",
                     place_name = "藤沢周平記念館")

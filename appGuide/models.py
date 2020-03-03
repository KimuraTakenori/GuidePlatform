from django.db import models

# Create your models here.

#性別名データ
class Gender(models.Model):

    gender_name = models.CharField(max_length = 32,
                                   verbose_name = "性別名")

    def __str__(self):

        return self.gender_name

    class Meta:
        verbose_name        = "性別名データ"
        verbose_name_plural = "性別名データ"

#利用者データ
class Tourist(models.Model):

    user_sei = models.CharField(max_length = 32,
                                verbose_name = "利用者姓")
    user_mei = models.CharField(max_length = 32,
                                verbose_name = "利用者名")
    user_seifuri = models.CharField(max_length = 32,
                                    verbose_name = "利用者姓(ふりがな)")
    user_meifuri = models.CharField(max_length = 32,
                                    verbose_name = "利用者名(ふりがな)")
    user_gender = models.ForeignKey(Gender,
                                    on_delete=models.CASCADE,
                                    verbose_name = "性別")
    user_seinen = models.DateField(verbose_name = "生年月日")
    user_tel = models.SlugField(max_length = 13,
                                verbose_name = "電話番号")
    user_mail = models.EmailField(max_length = 50,
                                  verbose_name = "メールアドレス")
    user_pass = models.SlugField(max_length = 20,
                                 verbose_name = "パスワード")
    user_post = models.SlugField(max_length = 8,
                                 verbose_name = "郵便番号")
    user_address1 = models.CharField(max_length = 10,
                                     verbose_name = "都道府県")
    user_address2 = models.CharField(max_length = 32,
                                     verbose_name = "市区町村")
    user_address3 = models.CharField(max_length = 64, null = True, blank = True,
                                     verbose_name = "番地・建物")

    def __str__(self):

        return self.user_sei + " " + self.user_mei

    class Meta:
        verbose_name        = "利用者データ"
        verbose_name_plural = "利用者データ"

#ガイドデータ
class Guide(models.Model):

    guide_sei = models.CharField(max_length = 32,
                                verbose_name = "ガイド姓")
    guide_mei = models.CharField(max_length = 32,
                                verbose_name = "ガイド名")
    guide_seifuri = models.CharField(max_length = 32,
                                    verbose_name = "ガイド姓(ふりがな)")
    guide_meifuri = models.CharField(max_length = 32,
                                    verbose_name = "ガイド名(ふりがな)")
    guide_gender = models.ForeignKey(Gender,
                                    on_delete=models.CASCADE,
                                    verbose_name = "性別")
    guide_seinen = models.DateField(verbose_name = "生年月日")
    guide_tel = models.SlugField(max_length = 13,
                                verbose_name = "電話番号")
    guide_mail = models.EmailField(max_length = 50,
                                  verbose_name = "メールアドレス")
    guide_pass = models.SlugField(max_length = 20,
                                 verbose_name = "パスワード")
    guide_post = models.SlugField(max_length = 8,
                                 verbose_name = "郵便番号")
    guide_address1 = models.CharField(max_length = 10,
                                     verbose_name = "都道府県")
    guide_address2 = models.CharField(max_length = 32,
                                     verbose_name = "市区町村")
    guide_address3 = models.CharField(max_length = 64, null = True, blank = True,
                                     verbose_name = "番地・建物")
    guide_qual = models.CharField(max_length = 500, null = True, blank = True,
                                  verbose_name = "保有資格")
    guide_pr = models.CharField(max_length = 1000, null = True, blank = True,
                                verbose_name = "PR欄")

    def __str__(self):

        return self.guide_sei + " " + self.guide_mei

    class Meta:
        verbose_name        = "ガイドデータ"
        verbose_name_plural = "ガイドデータ"

#プレ観光地データ
class Preplace(models.Model):

    preplace_address1 = models.CharField(max_length = 10,
                                     verbose_name = "都道府県")
    preplace_address2 = models.CharField(max_length = 32,
                                     verbose_name = "市区町村")
    preplace_name = models.CharField(max_length = 64,
                                     verbose_name = "観光地名称")
    preplace_info = models.CharField(max_length = 500, null = True, blank = True,
                                     verbose_name = "観光地情報")

    def __str__(self):

        return self.preplace_address1 + " " + self.preplace_address2 + " " + self.preplace_name

    class Meta:
        verbose_name        = "プレ観光地データ"
        verbose_name_plural = "プレ観光地データ"

#観光地データ
class Place(models.Model):

    place_address1 = models.CharField(max_length = 10,
                                     verbose_name = "都道府県")
    place_address2 = models.CharField(max_length = 32,
                                     verbose_name = "市区町村")
    place_name = models.CharField(max_length = 64,
                                     verbose_name = "観光地名称")
    place_info = models.CharField(max_length = 500, null = True, blank = True,
                                     verbose_name = "観光地情報")

    def __str__(self):

        return self.place_address1 + " " + self.place_address2 + " " + self.place_name

    class Meta:
        verbose_name        = "観光地データ"
        verbose_name_plural = "観光地データ"

#手配データ
class Reservation(models.Model):

    reservation_name = models.ForeignKey(Tourist,
                                    on_delete=models.CASCADE,
                                    verbose_name = "利用者名")
    reservation_ymdt = models.DateTimeField(verbose_name = "予約日時")
    reservation_place = models.ForeignKey(Place,
                                    on_delete=models.CASCADE,
                                    verbose_name = "観光地")
    reservation_guide = models.ForeignKey(Guide,
                                    on_delete=models.CASCADE,
                                    verbose_name = "ガイド")

    class Meta:
        verbose_name        = "手配データ"
        verbose_name_plural = "手配データ"

#ガイド可能時間データ
class Guidetime(models.Model):

    guide_name = models.ForeignKey(Guide,
                                    on_delete=models.CASCADE,
                                    verbose_name = "ガイド名")
    guide_time_from = models.DateTimeField(null = True, blank = True, verbose_name = "ガイド可能時間帯開始時刻")
    guide_time_to = models.DateTimeField(null = True, blank = True, verbose_name = "ガイド可能時間帯終了時刻")

    class Meta:
        verbose_name        = "ガイド可能時間データ"
        verbose_name_plural = "ガイド可能時間データ"

#ガイド可能場所データ
class Guideplace(models.Model):

    guide_name = models.ForeignKey(Guide,
                                    on_delete=models.CASCADE,
                                    verbose_name = "ガイド名")
    guide_place1 = models.ForeignKey(Place,
                                    on_delete=models.CASCADE,
                                    null = True, blank = True, related_name = "guide_place1",
                                    verbose_name = "ガイド可能場所1")
    guide_place2 = models.ForeignKey(Place,
                                    on_delete=models.CASCADE,
                                    null = True, blank = True, related_name = "guide_place2",
                                    verbose_name = "ガイド可能場所2")
    guide_place3 = models.ForeignKey(Place,
                                    on_delete=models.CASCADE,
                                    null = True, blank = True, related_name = "guide_place3",
                                    verbose_name = "ガイド可能場所3")
    guide_place4 = models.ForeignKey(Place,
                                    on_delete=models.CASCADE,
                                    null = True, blank = True, related_name = "guide_place4",
                                    verbose_name = "ガイド可能場所4")
    guide_place5 = models.ForeignKey(Place,
                                    on_delete=models.CASCADE,
                                    null = True, blank = True, related_name = "guide_place5",
                                    verbose_name = "ガイド可能場所5")
    guide_place6 = models.ForeignKey(Place,
                                    on_delete=models.CASCADE,
                                    null = True, blank = True, related_name = "guide_place6",
                                    verbose_name = "ガイド可能場所6")
    guide_place7 = models.ForeignKey(Place,
                                    on_delete=models.CASCADE,
                                    null = True, blank = True, related_name = "guide_place7",
                                    verbose_name = "ガイド可能場所7")
    guide_place8 = models.ForeignKey(Place,
                                    on_delete=models.CASCADE,
                                    null = True, blank = True, related_name = "guide_place8",
                                    verbose_name = "ガイド可能場所8")
    guide_place9 = models.ForeignKey(Place,
                                    on_delete=models.CASCADE,
                                    null = True, blank = True, related_name = "guide_place19",
                                    verbose_name = "ガイド可能場所9")
    guide_place10 = models.ForeignKey(Place,
                                    on_delete=models.CASCADE,
                                    null = True, blank = True, related_name = "guide_place10",
                                    verbose_name = "ガイド可能場所10")

    class Meta:
        verbose_name        = "ガイド可能場所データ"
        verbose_name_plural = "ガイド可能場所データ"












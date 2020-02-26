from django.db import models

# Create your models here.

class Gender(models.Model):

    gender_name = models.CharField(max_length = 32, null = True, blank = True,
                                   verbose_name = "性別名")

    def __str__(self):

        return self.gender_name

class Tourist(models.Model):

    user_sei = models.CharField(max_length = 32, null = True, blank = True,
                                verbose_name = "利用者姓")
    user_mei = models.CharField(max_length = 32, null = True, blank = True,
                                verbose_name = "利用者名")
    user_seifuri = models.CharField(max_length = 32, null = True, blank = True,
                                    verbose_name = "利用者姓(ふりがな)")
    user_meifuri = models.CharField(max_length = 32, null = True, blank = True,
                                    verbose_name = "利用者名(ふりがな)")
    user_gender = models.ForeignKey(Gender,
                                    on_delete=models.CASCADE,
                                    null = True, blank = True,
                                    verbose_name = "性別")
    user_seinen = models.DateField(null = True, blank = True, verbose_name = "生年月日")
    user_tel = models.SlugField(max_length = 13, null = True, blank = True,
                                verbose_name = "電話番号")
    user_mail = models.EmailField(max_length = 50, null = True, blank = True,
                                  verbose_name = "メールアドレス")
    user_pass = models.SlugField(max_length = 20, null = True, blank = True,
                                 verbose_name = "パスワード")
    user_post = models.SlugField(max_length = 8, null = True, blank = True,
                                 verbose_name = "郵便番号")
    user_address1 = models.CharField(max_length = 10, null = True, blank = True,
                                     verbose_name = "都道府県")
    user_address2 = models.CharField(max_length = 32, null = True, blank = True,
                                     verbose_name = "市区町村")
    user_address3 = models.CharField(max_length = 64, null = True, blank = True,
                                     verbose_name = "番地・建物")

    def __str__(self):

        return self.user_sei + " " + self.user_mei


class Guide(models.Model):

    guide_sei = models.CharField(max_length = 32, null = True, blank = True,
                                verbose_name = "ガイド姓")
    guide_mei = models.CharField(max_length = 32, null = True, blank = True,
                                verbose_name = "ガイド名")
    guide_seifuri = models.CharField(max_length = 32, null = True, blank = True,
                                    verbose_name = "ガイド姓(ふりがな)")
    guide_meifuri = models.CharField(max_length = 32, null = True, blank = True,
                                    verbose_name = "ガイド名(ふりがな)")
    guide_gender = models.ForeignKey(Gender,
                                    on_delete=models.CASCADE,
                                    null = True, blank = True,
                                    verbose_name = "性別")
    guide_seinen = models.DateField(null = True, blank = True, verbose_name = "生年月日")
    guide_tel = models.SlugField(max_length = 13, null = True, blank = True,
                                verbose_name = "電話番号")
    guide_mail = models.EmailField(max_length = 50, null = True, blank = True,
                                  verbose_name = "メールアドレス")
    guide_pass = models.SlugField(max_length = 20, null = True, blank = True,
                                 verbose_name = "パスワード")
    guide_post = models.SlugField(max_length = 8, null = True, blank = True,
                                 verbose_name = "郵便番号")
    guide_address1 = models.CharField(max_length = 10, null = True, blank = True,
                                     verbose_name = "都道府県")
    guide_address2 = models.CharField(max_length = 32, null = True, blank = True,
                                     verbose_name = "市区町村")
    guide_address3 = models.CharField(max_length = 64, null = True, blank = True,
                                     verbose_name = "番地・建物")
    guide_qual = models.CharField(max_length = 500, null = True, blank = True,
                                  verbose_name = "保有資格")
    guide_pr = models.CharField(max_length = 1000, null = True, blank = True,
                                verbose_name = "PR欄")


    def __str__(self):

        return self.guide_sei + " " + self.guide_mei

from django.db import models


class Provinces(models.Model):
    fa_name = models.CharField(max_length=255, verbose_name='نام استان به فارسی')
    en_name = models.CharField(max_length=255, verbose_name='نام استان به انگلیسی')

    def __str__(self):
        return self.fa_name

    class Meta:
        verbose_name = 'استان'
        verbose_name_plural = 'استان ها'


class Cities(models.Model):
    province = models.ForeignKey(Provinces, on_delete=models.CASCADE, verbose_name='استان')
    fa_name = models.CharField(max_length=255, verbose_name='نام شهر به فارسی')
    en_name = models.CharField(max_length=255, verbose_name='نام شهر به انگلیسی')

    def __str__(self):
        return self.fa_name

    class Meta:
        verbose_name = 'شهر'
        verbose_name_plural = 'شهر ها'


class WeightPrice(models.Model):
    price_0_to_half = models.PositiveBigIntegerField(verbose_name='قیمت 0 تا 0.5 کیلو')
    price_half_to_1 = models.PositiveBigIntegerField(verbose_name='قیمت 0.5 تا 1 کیلو')
    price_1_to_2 = models.PositiveBigIntegerField(verbose_name='قیمت 1 تا 2 کیلو')
    price_2_to_3 = models.PositiveBigIntegerField(verbose_name='قیمت 2 تا 3 کیلو')
    price_3_to_4 = models.PositiveBigIntegerField(verbose_name='قیمت 3 تا 4 کیلو')
    price_4_to_5 = models.PositiveBigIntegerField(verbose_name='قیمت 4 تا 5 کبلو')
    price_5_to_6 = models.PositiveBigIntegerField(verbose_name='قیمت 5 تا 6 کیلو')
    price_6_to_7 = models.PositiveBigIntegerField(verbose_name='قیمت 6 تا 7 کیلو')
    price_7_to_8 = models.PositiveBigIntegerField(verbose_name='قیمت 7 تا 8 کیلو')
    price_8_to_9 = models.PositiveBigIntegerField(verbose_name='قیمت 8 تا 9 کیلو')
    price_9_to_10 = models.PositiveBigIntegerField(verbose_name='قیمت 9 تا 10 کیلو')
    price_10_to_11 = models.PositiveBigIntegerField(verbose_name='قیمت 10 تا 11 کیلو')
    price_11_to_12 = models.PositiveBigIntegerField(verbose_name='قیمت 11 تا 12 کیلو')
    price_12_to_13 = models.PositiveBigIntegerField(verbose_name='قیمت 12 تا 13 کیلو')
    price_13_to_14 = models.PositiveBigIntegerField(verbose_name='قیمت 13 تا 14 کیلو')
    price_14_to_15 = models.PositiveBigIntegerField(verbose_name='قیمت 14 تا 15 کیلو')
    price_15_to_16 = models.PositiveBigIntegerField(verbose_name='قیمت 15 تا 16 کیلو')
    price_16_to_17 = models.PositiveBigIntegerField(verbose_name='قیمت 16 تا 17 کیلو')
    price_17_to_18 = models.PositiveBigIntegerField(verbose_name='قیمت 17 تا 18 کیلو')
    price_18_to_19 = models.PositiveBigIntegerField(verbose_name='قیمت 18 تا 19 کیلو')
    price_19_to_20 = models.PositiveBigIntegerField(verbose_name='قیمت 19 تا 20 کیلو')
    price_20_to_21 = models.PositiveBigIntegerField(verbose_name='قیمت 20 تا 21 کیلو')
    price_21_to_22 = models.PositiveBigIntegerField(verbose_name='قیمت 21 تا 22 کیلو')
    price_22_to_23 = models.PositiveBigIntegerField(verbose_name='قیمت 22 تا 23 کیلو')
    price_23_to_24 = models.PositiveBigIntegerField(verbose_name='قیمت 23 تا 24 کیلو')
    price_24_to_25 = models.PositiveBigIntegerField(verbose_name='قیمت 24 تا 25 کیلو')
    price_25_to_26 = models.PositiveBigIntegerField(verbose_name='قیمت 25 تا 26 کیلو')
    price_26_to_27 = models.PositiveBigIntegerField(verbose_name='قیمت 26 تا 27 کیلو')
    price_27_to_28 = models.PositiveBigIntegerField(verbose_name='قیمت 27 تا 28 کیلو')
    price_28_to_29 = models.PositiveBigIntegerField(verbose_name='قیمت 28 تا 29 کیلو')
    price_29_to_30 = models.PositiveBigIntegerField(verbose_name='قیمت 29 تا 30 کیلو')
    price_30_to_higher = models.PositiveBigIntegerField(verbose_name='قیمت بیشتر از 30 کیلو')

    def __str__(self):
        return f'{self.price_0_to_half}'

    class Meta:
        verbose_name = 'قیمت وزن'
        verbose_name_plural = 'قیمت وزن ها'

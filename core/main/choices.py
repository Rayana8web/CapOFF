from django.db import models



class BannerLocationEnum(models.TextChoices):
    INDEX_HEAD = ('index_head', 'сверху главной страницы')
    INDEX_MIDDLE = ('index_middle', 'середина главной страницы')
    CATALOG_HEAD = ('catalog_head', 'сверху каталога')
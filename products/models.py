from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('parent'), blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    describtion = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(-('avatar'), blank=True, upload_to='categories')
    is_enable = models.BooleanField(-('is_enable'), default=True)
    created_time = models.DateTimeField(-('created time'), auto_created=True)
    updated_time= models.DateTimeField(-('updated time'), auto_created=True)
    class Meta:
        db_table = 'catogories'
        verbose_name = _('Category')
        verbose_name_plural= -('Categories')
class Product(models.Model):
    pass
class File(models.Model):
    pass
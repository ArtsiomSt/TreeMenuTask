from django.db import models
from django.urls import reverse


class Menu(models.Model):
    menu_name = models.CharField(
        max_length=80,
        verbose_name="Menu name",
        unique=True
    )

    def __str__(self):
        return self.menu_name

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'


class SubMenu(models.Model):
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name='Title')
    parent = models.ForeignKey('self', blank=True, on_delete=models.CASCADE, null=True, help_text="If this field is blank, so this is the first layer of submenus")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('menuitems', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Sub Menu'
        verbose_name_plural = 'Sub Menus'

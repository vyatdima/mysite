from django.db import models


class People(models.Model):
    fam = models.CharField(max_length=40, verbose_name='Фамилия')
    nam = models.CharField(max_length=40, verbose_name='Имя', blank=True)
    ptr = models.CharField(max_length=40, verbose_name='Отчество', blank=True)
    brd = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    pol = models.CharField(max_length=1, verbose_name='Пол', blank=True)
    gorod = models.CharField(max_length=100, verbose_name='Населенный пункт', blank=True)
    telefon = models.CharField(max_length=30, verbose_name='Номер телефона', blank=True)
    email = models.EmailField(blank=True, verbose_name='Адрес электронной почты')
    photo = models.ImageField(upload_to='peoples_images', blank=True, verbose_name='Фото')


    def __str__(self):
        return f'{self.fam} {self.nam} {self.ptr} {self.pk}'

    class Meta:
        ordering = ['fam', 'nam', 'ptr']
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')

    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Event(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    info = models.TextField(blank=True, null=True, verbose_name='Информация')
    logo_img = models.ImageField(upload_to='events_images', blank=True, verbose_name='Логотип')
    suvenir_img = models.ImageField(upload_to='events_images', blank=True, verbose_name='Сувенир')
    date_sorev = models.DateField(blank=True, verbose_name='Дата проведения')
    is_no_view = models.BooleanField(default=False, verbose_name='Не показывать')
    url_in_internet = models.CharField(blank=True, max_length=100, verbose_name='Подробная информация')
    id_in_iorient = models.IntegerField(blank=True, default=0, verbose_name='Id на iorient.ru')
    num_people = models.IntegerField(blank=True, default=0, verbose_name='Количество участников')
    num_com = models.IntegerField(blank=True, default=0, verbose_name='Количество команд')
    num_slot = models.IntegerField(blank=True, default=0, verbose_name='Количество слотов')
    abs_people = models.ForeignKey('People', on_delete=models.PROTECT, null=True, default=1)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'{self.pk} {self.name}'

    class Meta:
        ordering = ['-date_sorev']
        verbose_name = 'Соревнование'
        verbose_name_plural = 'Соревнования'

class PeopleEvent(models.Model):
    event = models.ForeignKey('Event', on_delete=models.PROTECT, null=True, default=1)
    people = models.ForeignKey('People', on_delete=models.PROTECT, null=True, default=1)
    mesto = models.IntegerField(blank=True, default=0)
    reiting = models.FloatField(blank=True, default=0, verbose_name='Рейтинг')
    zoloto = models.BooleanField(default=False)
    serebro = models.BooleanField(default=False)
    bronza = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Участник соревнования'
        verbose_name_plural = 'Участники соревнований'

    def __str__(self):
        return f'{self.event}|{self.people}'

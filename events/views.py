# from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from events.models import Event, People, PeopleEvent
import random
from random import choice
import csv
import datetime


def index(request):
    context = {
        'title': 'Главная',
        }
    return render(request, 'events/index.html', context)

def peoples(request, id_param=None):
    if id_param:
        peoples_data = People.objects.get(id=id_param)
        events_people = PeopleEvent.objects.filter(people=id_param).order_by('event')
        context = {
            'title': 'Инфо об участнике',
            'peoples': peoples_data,
            'events_people':  events_people,
            }
        template_file = 'events/people.html'
    else:
        peoples_data = People.objects.all()
        template_file = 'events/peoples.html'
        context = {
            'title': 'Участники',
            'peoples': peoples_data,
            }
    return render(request,  template_file, context)


def events(request, id_param=None):
    if id_param:
        events_data = Event.objects.get(id=id_param)
        event_peoples_data = PeopleEvent.objects.filter(event=id_param).order_by('people')
        cnt_people_event = len(event_peoples_data)
        template_file = 'events/event.html'

        context = {
            'title': 'Инфо о мероприятии',
            'events': events_data,
            'event_peoples': event_peoples_data,
            'cnt_people_event': cnt_people_event,
        }
    else:
        events_data = Event.objects.all()
        template_file = 'events/events.html'
        context = {
            'title': 'Мероприятия',
            'events': events_data,
            }
    return render(request, template_file, context)


def procedures(request):
    return render(request, 'events/procedures.html', {'title': 'Процедуры', })


def PasswordCreate(request):
    charasters_str = 'abcdifghijklnmopqrstuvw'
    charasters = list(charasters_str)
    if request.GET.get('uppercase'):
        charasters.extend(list(charasters_str.upper()))
    if request.GET.get('numbers'):
        charasters.extend(list('0123456789'))
    if request.GET.get('specials'):
        charasters.extend(list('_'))
    password = ''
    for i in range(int(request.GET.get('lenght', 3))):
        password += random.choice(charasters)
    return render(request, 'events/password.html', {'password': password, 'title': 'Результат генерации'})

def LoadFromFile(request):
    load_protokol = ['Протокол загрузки из файла']
    s1 = request.GET.get('file_for_load')
    if s1:
        load_protokol.append(f'Файл: {s1}')
        with open(f'D:\{s1}', 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                cbrd = row[9].strip()
                cfam = row[5].strip()
                cnam = row[6].strip()
                cptr = row[7].strip()
                cgorod = row[10].strip()
                cemail = row[12].strip()
                date_obj = datetime.datetime.strptime(cbrd, '%d.%m.%Y')
                dbrd = date_obj.date()
                yes_people = People.objects.filter(fam=cfam, nam=cnam, brd=dbrd).exists()
                if not yes_people:
                    zapis = People.objects.create(fam=cfam, nam=cnam, ptr=cptr, brd=dbrd, pol=row[8], gorod=cgorod, telefon=row[11], email=cemail)
                    load_protokol.append(f'+ {cfam} {cnam} {cptr} {cbrd}')
                yes_people = People.objects.filter(fam=cfam, nam=cnam, brd=dbrd).exists()
                if yes_people:
                    sp_people = People.objects.filter(fam=cfam, nam=cnam, brd=dbrd)
                    for item in sp_people:
                        yes_people_in_event = PeopleEvent.objects.filter(event=int(row[0]), people=item.pk).exists()
                        if not yes_people_in_event:
                            zapis = PeopleEvent.objects.create(event_id=int(row[0]), people_id=item.pk)
                            load_protokol.append(f'{cfam} {cnam} {cptr} {cbrd} ({row[0]})')
                else:
                    load_protokol.append(f'- {cfam} {cnam} {cptr} {cbrd}')
        for item in load_protokol:
            print(item)
    return render(request, 'events/load_from_file.html', {'title': 'Результат загрузки', 'massiv': load_protokol})

def ExportToFile(request):
    export_data = []
    if request.GET.get('people'):
        qs = People.objects.all()
        for item in qs:
            strr = f'{item.pk}|{item.fam}|{item.nam}|{item.ptr}|{item.brd}|{item.gorod}|{item.telefon}|{item.email}'
            export_data.append(strr)
        with open(f'D:\people.txt', 'w', newline='') as file:
            for item in export_data:
                file.write(f'{item}\n')
    return render(request, 'events/load_from_file.html', {'title': 'Результат выгрузки', 'massiv': export_data})


def StripPeople(request):
    qs = People.objects.all()
    for item in qs:
        sss = People.objects.get(pk=item.pk)
        lfam = sss.fam.strip()
        lnam = sss.nam.strip()
        lptr = sss.ptr.strip()
        lgorod = sss.gorod.strip()
        ltelefon = sss.telefon.strip()
        lemail = sss.email.strip()
        sss.fam = lfam
        sss.nam = lnam
        sss.ptr = lptr
        sss.gorod = lgorod
        sss.telefon = ltelefon
        sss.email = lemail
        sss.save()
    load_protokol = ['Удаление пробелов']
    return render(request, 'events/load_from_file.html', {'title': 'Удаление пробелов', 'load_protokol': load_protokol})

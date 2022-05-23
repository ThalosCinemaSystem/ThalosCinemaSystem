from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.dateparse import parse_datetime
from .models import *
import datetime
from django.contrib.auth.decorators import login_required


def main_page(request, pk=Cinema.objects.first(), pk2=None, pk3='ALL', pk4=1):
    if pk2 is None:
        pk2 = datetime.date.today().strftime('%Y-%m-%d')

    projection = Projection.objects.filter(room__cinema__name=pk)
    projection = projection.filter(start_date_time__contains=pk2)
    if pk3 != 'ALL':
        projection = projection.filter(movie__title__contains=Genre.objects.filter(name=pk3).values('movie_id__title'))
    weekend = ["NIEDZ", "PON", "WT", "ŚR", "CZW", "PT", "SOB"]
    Date = {}
    Date[0] = {}
    Date[0]['Day'] = datetime.date.today().strftime('%Y-%m-%d')
    Date[0]['Name'] = "Dziś"
    for i in range(3):
        Date[i + 1] = {}
        Date[i + 1]['Day'] = (datetime.date.today() + datetime.timedelta(days=i + 1)).strftime('%Y-%m-%d')
        Date[i + 1]['Name'] = weekend[int((datetime.date.today() + datetime.timedelta(days=i + 1)).strftime('%w'))]
    projections = {}
    id = 0
    for i in projection:
        if i.movie.title not in projections.keys():
            projections[i.movie.title] = {}
            projections[i.movie.title]['id'] = id
            projections[i.movie.title]['title'] = i.movie.title
            projections[i.movie.title]['during'] = i.movie.during
            projections[i.movie.title]['Thumbnail'] = i.movie.thumbnail.url
            projections[i.movie.title]['start_date_time'] = []
            projections[i.movie.title]['Genre'] = Genre.objects.filter(movie__title=i.movie.title)
            projections[i.movie.title]['projection_id'] = i.pk
            id = id + 1

        projections[i.movie.title]['start_date_time'].append(i.start_date_time)
    pages = id // 5 + 1
    if pk4 < 3:
        min = 1
        max = 6
    else:
        min = pk4 - 2
        max = pk4 + 3

    if pages < 5:
        max = pages + 1

    pages = range(min, max)
    for x, y in dict(projections).items():
        if y['id'] not in range(pk4 * 5 - 5, pk4 * 5):
            del projections[x]
    cinemas = Cinema.objects.all()
    context = {'cinemas': cinemas, 'projections': projections, "Date": Date, "pk": pk, 'pk2': pk2, 'pk3': pk3,
               'pk4': pk4, 'pages': pages}
    return render(request, 'website/main.html', context=context)


def marathons(request):
    marathon = Marathon.objects.first()
    projections = Projection.objects.filter(marathon=marathon).all()

    context = {'marathon': marathon,
               'projections': projections}

    return render(request, 'website/marathons.html', context=context)


def schools(request):
    context = {}

    return render(request, 'website/schools.html', context=context)


def account(request):
    context = {}

    return render(request, 'website/account.html', context=context)


def events_and_promotions(request):
    context = {}

    return render(request, 'website/events_and_promotions.html', context=context)


def repertoire(request):
    context = {}

    return render(request, 'website/repertoire.html', context=context)


def error_404(request, exception):
    data = {"error_http": "Błąd 404"}
    return render(request, 'website/error_http.html', context=data)


def error_500(request):
    data = {"error_http": "Błąd 500"}
    return render(request, 'website/error_http.html', context=data)


def logoutUser(request):
    logout(request)
    return redirect(main_page)


def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                return redirect('change_password')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'website/change_password.html', {
            'form': form
        })
    else:
        return redirect(main_page)


def book_movie(request, projection_pk):
    projection = Projection.objects.get(pk=projection_pk)
    seats = Seat.objects.filter(room=projection.room).all()
    divided_seats = [seats[i:i + 10] for i in range(0, 100) if i % 10 == 0]

    context = {'projection': projection,
               'room': projection.room,
               'divided_seats': divided_seats}

    if request.method == "POST":
        seats = request.POST.get('seats')

    if not request.COOKIES.get('projection_choice_id'):
        if request.META.get('HTTP_REFERER') == request.build_absolute_uri():
            return render(request, 'website/projection_to_reservation.html', context=context)

        elif request.GET.get('movie') == 'selected':
            response = render(request, 'website/choice_seat.html', context=context)
            response.set_cookie(key='projection_choice_id', value=projection_pk)
            return response

        return render(request, 'website/projection_to_reservation.html', context=context)

    if request.GET.get('reservation') == 'intterup':
        if request.COOKIES.get('projection_choice_id'):
            response = redirect('main_page')
            response.delete_cookie('projection_choice_id')

            return response

    return render(request, 'website/choice_seat.html', context=context)

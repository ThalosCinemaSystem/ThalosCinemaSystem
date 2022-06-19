from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import *
import datetime
from django.contrib.auth.decorators import login_required


def main_page(request, pk=Cinema.objects.first(), pk2=None, pk3=None, pk4=1):
    if pk2 is None:
        pk2 = datetime.date.today().strftime('%Y-%m-%d')

    projection = Projection.objects.filter(room__cinema__name=pk)
    projection = projection.filter(start_date_time__contains=pk2)
    if pk3 is not None and pk3 != 'None':
        projection = projection.filter(movie_id__genre__name=pk3)
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
            projections[i.movie.title]['projection_movie_id'] = i.movie.id
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
    genres = Genre.objects.all()
    releases = Projection.objects.filter(start_date_time__gte=datetime.date.today() + datetime.timedelta(days=7)).values('movie_id','movie_id__title','movie_id__thumbnail', 'movie_id__description').distinct()[:3]
    context = {'cinemas': cinemas, 'projections': projections, "Date": Date, "pk": pk, 'pk2': pk2, 'pk3': pk3,
               'pk4': pk4, 'pages': pages, 'releases':releases,'genres':genres}

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


@login_required(login_url='main_page')
def logout_user(request):
    logout(request)
    return redirect(main_page)


@login_required(login_url='main_page')
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


def book_movie(request, movie_pk, date):
    projections = Projection.objects.filter(movie_id=movie_pk).filter(start_date_time__contains=date)

    context = {'projections': projections}

    return render(request, 'website/projection_to_reservation.html', context=context)


def book_movie_projection(request, movie_pk, date, projection_pk):
    reservations = Reservation.objects.filter(projection_id=projection_pk)
    seats_are_reservated = [reservation.seat for reservation in reservations]

    seats = Seat.objects.filter(room__projection=projection_pk)
    seats_sorted = sorted(seats, key=lambda seat: seat.seat_number)
    divided_seats = [seats_sorted[i:i + 10] for i in range(0, 100) if i % 10 == 0]

    if request.method == 'POST':
        seat_pk = request.POST.get('seat')
        seat_obj = Seat.objects.get(pk=seat_pk)
        if not seat_obj.is_reservated or (seat_obj.is_reservated and (seat_obj not in seats_are_reservated)):
            seat_obj.is_durning_reservation = True
            seat_obj.save()
            request.session['projection_id_reserving'] = projection_pk
            request.session['seat_id_reserving'] = seat_obj.pk

            return redirect('reservation_summary')

    if request.session.get('projection_id_reserving', False) and request.session.get('seat_id_reserving', False):
        return redirect('reservation_summary')

    context = {'divided_seats': divided_seats, 'seats_are_reservated': seats_are_reservated}
    return render(request, 'website/choice_seat.html', context=context)


@login_required(login_url='main_page')
def reservation_summary(request):
    projection_id = request.session.get('projection_id_reserving', False)
    seat_id = request.session.get('seat_id_reserving', False)

    if projection_id and seat_id:
        projection = Projection.objects.get(pk=projection_id)
        seat = Seat.objects.get(pk=seat_id)

        if request.GET.get('reservation') == 'done':
            reservation = Reservation(user=request.user, seat=seat, projection=projection)
            reservation.save()
            del request.session['projection_id_reserving']
            del request.session['seat_id_reserving']
            seat.is_durning_reservation = False
            seat.save()

            return redirect('main_page')

        elif request.GET.get('reservation') == 'interrupt':
            del request.session['projection_id_reserving']
            del request.session['seat_id_reserving']
            seat.is_durning_reservation = False
            seat.save()

            return redirect('main_page')

        context = {'projection': projection,
                   'seat': seat}

        return render(request, 'website/summary_reservation.html', context=context)

    return redirect(main_page)

from django.shortcuts import render 
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse

monthly_challenges = {
    'january': 'Eat no meat for the entire month!',
    'february': 'Walk for at least 20 minutes every day!',
    'march': 'Learn Piano for at least 20 minutes every day!',
    'april': 'Learn French for at least 20 minutes every day!',
    'may': 'Learn Hula Hoop for at least 20 minutes every day!',
    'june': 'Learn Karate for at least 20 minutes every day!',
    'july': 'Learn Django for at least 20 minutes every day!',
    'august': 'Learn salsa dancing for at least 20 minutes every day!',
    'september': 'Learn sculpting for at least 20 minutes every day!',
    'october': 'Learn cooking for at least 20 minutes every day!',
    'november': 'Go running for at least 20 minutes every day!',
    'december': None
}

# Create your views here.

def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('monthly-challenge', args=[month])

    return render(request, 'challenges/index.html', {'months': months})

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('Invalid month!')
    redirect_month = months[month - 1]
    redirect_path = reverse('monthly-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
        'text': challenge_text,
        'month_name': month,
        })
    except: 
        raise Http404()



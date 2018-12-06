from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django import forms

from .forms import SignupForm
from signup.models import Email

def index(request):
    """
    :param request:
    :return: form context
    """
    context = {
        'form': SignupForm()
    }
    return render(request, 'index.html', context)


def ajax_email(request):
    """
    :param request:
    :return: JsonResponse with a done or not done status and errors to display.
    """

    email = request.POST.get('email')

    try:
        qs = Email.objects.get(email=email)
    except ObjectDoesNotExist:
        qs = None

    if qs:
        context = {
            'status': 'not_done',
            'errors': 'taken'
        }
    else:
        if email:
            e = Email(email=email)
            e.save()
        context = {
            'status': 'done',
            'errors': ''
        }
    print(context)
    return JsonResponse(context)



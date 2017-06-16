from django.shortcuts import render

# Create your views here.


def landing_pad(request):
    """

    :param request:
    :return:
    """

    return render(request, 'landing_pad.html')
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm




"""
Formally known as 'template views', this issues no DB querysets
"""

# Create your views here.


def about(request):
    """

    :param request:
    :return:
    """

    return render(request, 'about.html')


def contact(request):
    """

    :param request:
    :return:
    """

    return render(request, 'contact.html')


def help(request):
    """

    :param request:
    :return:
    """

    return render(request, 'help.html')


def sitemap(request):
    """

    :param request:
    :return:
    """

    return render(request, 'sitemap.html')


def terms(request):
    """

    :param request:
    :return:
    """

    return render(request, 'terms.html')


def index(request):
    """

    :param request:
    :return:
    """

    form = AuthenticationForm()

    context = {'form': form}

    return render(request, 'index.html', context)


def handler404(request):
    """

    :param request:
    :return:
    """
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    """

    :param request:
    :return:
    """
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response

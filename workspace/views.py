from django.shortcuts import render
from .forms import CreateRoBitForm

# Create your views here.


def create(request):
    """

    :return:
    """

    form = CreateRoBitForm()

    context = {'form': form}

    return render(request, 'create.html', context)


def delete(request):
    """

    :return:
    """
    return render(request, 'delete.html')


def edit(request):
    """

    :return:
    """
    return render(request, 'edit.html')


def history(request):
    """

    :return:
    """
    return render(request, 'history.html')


def launch(request):
    """

    :return:
    """
    return render(request, 'launch.html')


def workspace(request):
    """

    :return:
    """
    return render(request, 'workspace.html')

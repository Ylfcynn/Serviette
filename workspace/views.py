from django.shortcuts import render

# Create your views here.


def create(request):
    """

    :return:
    """
    return render(request, 'create.html')


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


def workspace(request):
    """

    :return:
    """
    return render(request, 'workspace.html')

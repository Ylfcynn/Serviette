from django.shortcuts import render

# Create your views here.


def workspace(request):
    """

    :return:
    """
    return render(request, 'workspace.html')
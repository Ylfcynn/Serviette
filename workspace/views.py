from django.shortcuts import render, redirect
from .forms import CreateRoBitForm
from .models import RoBit

# Create your views here.


def create(request):
    """

    :return:
    """

    if request.method == 'GET':

        form = CreateRoBitForm()

    elif request.method == 'POST':

        form = CreateRoBitForm(data=request.POST)

        if form.is_valid():
            robit = form.save(commit=False)
            # modify robit at the last minute!
            robit.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'create.html', context)


def delete(request):
    """

    :return:
    """
    return render(request, 'delete.html')


def edit(request, pk):
    """

    :return:
    """

    robit = RoBit.objects.get(id=pk)

    if request.method == 'GET':

        form = CreateRoBitForm(instance=robit)

    elif request.method == 'POST':

        form = CreateRoBitForm(data=request.POST, instance=robit)

        if form.is_valid():
            robit = form.save(commit=False)
            # modify robit at the last minute!
            robit.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'edit.html', context)


def my_robits(request):
    """

    :return:
    """
    return render(request, 'my_robits.html')


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

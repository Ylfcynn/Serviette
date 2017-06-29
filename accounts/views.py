from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail

from .forms import CustomUserCreationForm
from .forms import CustomUserUpdateForm

"""
Formally known as 'template views', this issue no DB querysets
"""



def login(request):
    """

    :return:
    """

    if request.method == 'GET':
        form = AuthenticationForm()

    elif request.method == 'POST':
        form = AuthenticationForm(data=sign_up) #TODO: Is this correct?

        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)

            if user is not None:    #See https://docs.djangoproject.com/en/1.11/ref/contrib/messages/

                django_login(request, user)
                messages.success(request, f'Logged in as {username}')
                return redirect(reverse('my_account'))

            else:
                messages.warning(request, 'Danger! Hacking attempt detected! Run for your life!')

    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def logout(request):
    """

    :return:
    """
    django_logout(request)
    return redirect('/')


def my_account(request):
    """

    :return:
    """
    return render(request, 'accounts/profile.html')


def sign_up(request):
    """

    :return:
    """

    if request.method == 'GET':
        form = CustomUserCreationForm()

    elif request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Make any last second change to the User here...
            user.save()

            subject = 'Welcome to Serviette.'
            message = 'Congratulations! You now awesome. Go forth and conquer.'
            from_email = 'dforcemega@gmail.com'        #TODO: Change this!
            recipient_list = ['dforcemega@gmail.com']    #TODO: Change this too!

            send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None,
                      auth_password=None, connection=None, html_message=None)

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            django_login(request, user)

            return redirect('accounts/my_account.html')

    context = {'form': form}
    return render(request, 'accounts/sign_up.html', context)

@login_required(login_url='accounts/login.html')
def profile(request):
    """

    :return:
    """

    form = CustomUserUpdateForm(instance=request.user)
    password_form = PasswordChangeForm(user=request.user)

    context = {'form': form, 'password_form': password_form}

    return render(request, 'accounts/profile.html', context)    # A preceding '/' makes a path absolute

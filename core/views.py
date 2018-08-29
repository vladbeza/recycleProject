from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, UserUpdateForm
from .tokens import account_activation_token

@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            user.refresh_from_db()
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your Kosatka Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode("utf-8"),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('core:account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('core:home')
    else:
        return render(request, 'account_activation_invalid.html')


@login_required
def profile(request):
    user = request.user
    return render(request, "user_profile.html", {"user": user})


@login_required
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            user.email = form.cleaned_data.get("email", user.email)
            user.first_name = form.cleaned_data.get("first_name", user.first_name)
            user.last_name = form.cleaned_data.get("last_name", user.last_name)
            user.profile.birth_date = form.cleaned_data.get("birth_date", user.profile.birth_date)
            if form.cleaned_data.get("password") is not None:
                user.set_password(form.cleaned_data.get("password"))
            return redirect('core:profile')
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'profile_edit.html', {'form': form})


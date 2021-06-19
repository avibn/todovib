from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views import View


class SignupView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            context = {
                "form": kwargs.get("form") if "form" in kwargs else UserCreationForm
            }

            return render(request, "auth/signup.html", context)
        return redirect(reverse("Home:index"))

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"],
            )
            login(request, user)

            return redirect(reverse("Home:index"))
        return self.get(request, form=form)

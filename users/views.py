from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, DetailView, UpdateView
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from . import forms
from . import models


class LoginView(FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("qnaboard:index")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


def log_out(request):
    logout(request)
    return redirect(reverse("qnaboard:index"))


class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("qnaboard:index")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class UserProfileView(DetailView):
    model = models.User
    context_object_name = "user_obj"


class UpdateProfileView(UpdateView):
    model = models.User
    template_name = "users/update_profile.html"
    fields = (
        "first_name",
        "avatar",
        "hp",
        "birthdate",
        "takencourse"
    )

    def get_object(self, queryset=None):
        return self.request.user

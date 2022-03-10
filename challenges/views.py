from django.shortcuts import render
from django.views.generic import FormView, DetailView
from . import models


class ChallengeView(DetailView):
    model = models.Challenge
    context_object_name = "challenge_obj"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class CreateChallengeView(FormView):
    pass

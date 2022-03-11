from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import FormView, DetailView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from . import models
from . import forms


class CreateChallengeView(FormView):
    challenge = models.Challenge
    template_name = "challenges/challenge_create.html"
    form_class = forms.CreateChallengeForm

    challenge.date_start = datetime.now()
    challenge.date_finish = datetime.now() + timedelta(weeks=1)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ChallengeDetailView(DetailView):
    challenge = models.Challenge
    template_name = "challenges/challenge_detail.html"
    form_class = forms.ChallengeDetailForm


def ChallengeList(request):
    page = request.GET.get('page', '1')
    challenge_list = models.Challenge.objects.all()
    paginator = Paginator(challenge_list, 10)
    page_obj = paginator.get_page(page)
    print(vars(page_obj.paginator))
    context = {"challenge_list": page_obj}
    return render(request, "challenges/challenge_list.html", context)


@login_required(login_url='users:login')
def ChallengeJoin(request, challenge_id):
    challenge = get_object_or_404(models.Challenge, pk=challenge_id)
    if request.challenger in challenge.challenger.all():
        challenge.challenger.remove(request.user)
    else:
        challenge.challenger.add(request.user)
    return redirect('qnaboard:detail', question_id=challenge.id)

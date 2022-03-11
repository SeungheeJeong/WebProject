from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import FormView, DetailView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from . import models
from . import forms


@login_required(login_url='users:login')  # 로그인을 어노테이션 - 로그인 상태에서 작동되게
def Challenge_create(request):
    """
    챌린지 게시하기
    """
    if request.method == 'POST':
        form = forms.CreateChallengeForm(request.POST)
        if form.is_valid():
            # 데이터베이스에 저장하기 전에 commit=False는 임시저장, date를 생성하기 위해 잠시 기다리는 중
            Challenge = form.save(commit=False)
            Challenge.host = request.user
            Challenge.save()
            # 저장이 끝나면 index(질문목록) 화면으로 돌아간다.
            return redirect('challenges:list')
    else:
        form = forms.CreateChallengeForm()
    context = {'form': form}
    return render(request, 'challenges/challenge_create.html', context)
# class CreateChallengeView(FormView):
#     challenge = models.Challenge
#     template_name = "challenges/challenge_create.html"
#     form_class = forms.CreateChallengeForm

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


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

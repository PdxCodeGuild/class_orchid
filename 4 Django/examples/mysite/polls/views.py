from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.core import serializers

from .models import Choice, Question

# Create your views here.


def all_results_view(request):
    questions = serializers.serialize('json', Question.objects.all())
    choices = serializers.serialize('json', Choice.objects.all())
    context = {
        'questions': questions,
        'choices': choices,
        'results_list': Question.objects.all()
    }
    return render(request, 'polls/all_results.html', context)


# These are like API endpoints, they serve JSON data at the specified URL
def get_questions(request):
    questions = serializers.serialize('json', Question.objects.all())
    return JsonResponse(questions, safe=False)


def get_choices(request):
    choices = serializers.serialize('json', Choice.objects.all())
    return JsonResponse(choices, safe=False)


# class AllResultsView(generic.ListView):
#     template_name = 'polls/all_results.html'
#     context_object_name = 'results_list'

#     def get_queryset(self):
#         return Question.objects.all


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     return render(request, 'polls/index.html', context)


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def add(request):
    print(request)
    q_text = request.POST.get('new_q')
    # new_q = Question(question_text=q_text, pub_date=timezone.now())
    # new_q.save()
    question = Question.objects.create(
        question_text=q_text, pub_date=timezone.now())

    choice1 = request.POST.get('choice1')
    if choice1:
        Choice.objects.create(question=question, choice_text=choice1)

    choice2 = request.POST.get('choice2')
    if choice2:
        Choice.objects.create(
            question=question, choice_text=choice2, is_correct='yes')

    choice3 = request.POST.get('choice3')
    if choice3:
        Choice.objects.create(question=question, choice_text=choice3)

    return HttpResponseRedirect(reverse('polls:index'))


def delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()

    return HttpResponseRedirect(reverse('polls:index'))

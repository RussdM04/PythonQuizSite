"""
Name: Russell, Abhinav, Arda
Student ID: C0927696, C0926240, C0923184
Date: August 14, 2025
Assignment: CSD 4523 Term Project - Toronto & GTA History Quiz
"""

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Max, Min
from .models import Question, QuizAttempt, Response
from django.contrib.auth import logout

def home(request):
    # Renders the landing page
    return render(request, 'home.html')

def register(request):
    # Simple user registration
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_now(request):
    logout(request)
    return redirect('/')

@login_required
def start_quiz(request):
    # GET: show 5 random questions
    if request.method == 'GET':
        questions = list(Question.objects.order_by('?')[:5])
        request.session['quiz_qids'] = [q.id for q in questions]
        return render(request, 'quiz.html', {'questions': questions})

    # POST: grade and save attempt
    qids = request.session.pop('quiz_qids', [])
    attempt = QuizAttempt.objects.create(user=request.user, total=len(qids))
    score = 0
    for qid in qids:
        q = Question.objects.get(id=qid)
        sel = request.POST.get(f'q_{qid}', '')
        correct = (sel == q.correct_option)
        if correct:
            score += 1
        Response.objects.create(
            attempt=attempt, question=q,
            selected_option=sel or '', is_correct=correct
        )
    attempt.score = score
    attempt.save()

    if score <= 2:
        msg = "Please try again!"
    elif score == 3:
        msg = "Good job!"
    elif score == 4:
        msg = "Excellent work!"
    else:
        msg = "You are a genius!"

    return render(request, 'result.html', {
        'attempt': attempt,
        'message': msg,
        'can_retake': score <= 2,  # allow retake if < 50%
    })

@login_required
def history(request):
    attempts = request.user.attempts.order_by('-created_at')
    stats = attempts.aggregate(avg=Avg('score'), high=Max('score'), low=Min('score'))
    return render(request, 'history.html', {
        'attempts': attempts,
        'avg': stats['avg'],
        'high': stats['high'],
        'low': stats['low'],
    })

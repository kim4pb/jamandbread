from django.shortcuts import render
from .models import Post

def main_page(request):
    return render(request, 'blog/main_page.html', {})

def question1(request):
    question1 = Post.objects.get(index=1)
    return render(request, 'blog/question1.html', {'question1':question1})

def question2(request):
    question2 = Post.objects.get(index=2)
    return render(request, 'blog/question2.html', {'question2':question2})

def question3(request):
    question3 = Post.objects.get(index=3)
    return render(request, 'blog/question3.html', {'question3':question3})

def question4(request):
    question4 = Post.objects.get(index=4)
    return render(request, 'blog/question4.html', {'question4':question4})

def result(request):
    result = Post.objects.get(index=11)
    return render(request, 'blog/result.html', {'result':result})

def info_detail(request):
    info_detail = Post.objects.get(index=101)
    return render(request, 'blog/info_detail.html', {'info_detail':info_detail})
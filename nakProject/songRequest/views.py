# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import PostModelForm
from .models import sPost
from django.contrib import messages

# Create your views here.
def songRequest(request):
    posts = sPost.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 5)
    pagnum = request.GET.get('page')
    posts = paginator.get_page(pagnum)
    return render(request, 'songRequest.html', {'posts':posts})

def create_s(request):
    if not request.user.is_authenticated:
        messages.error(request, '로그인이 필요합니다.')
        return redirect('accounts')
    
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user
            unfinished.save()
            form.save()
            return redirect('songRequest')
    else:
        form = PostModelForm()
    return render(request, 'form_create_s.html', {'form':form})


def post_detail_s(request, id): # 글 들어가서 자세히 보는 거
    post = get_object_or_404(sPost, pk=id)
    context={
        'sPost':post
    }
    return render(request, 'post_detail_s.html', context)

def post_update_s(request, id): # 수정하기
    post = get_object_or_404(sPost, pk=id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post) #instance는 기존내용 가져오기
        if form.is_valid():
            form.save()
            return redirect('songRequest')
    else:
        form = PostModelForm(instance=post)
        return render(request, 'form_create_s.html',{'form':form, 'id':id})
    
    
def post_delete_s(request, id): # 삭제하기
    post = sPost.objects.get(pk=id)
    post.delete()
    return redirect('songRequest')
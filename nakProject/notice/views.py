from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostModelForm
from .models import noticePost
from django.contrib import messages
# Create your views here.

def notice(request):
    posts = noticePost.objects.all().order_by('-created_at')
    return render(request, 'notice.html', {'posts':posts})

def create_n(request):
    if not request.user.is_authenticated:  # 사용자가 인증되지 않은 경우
        messages.error(request, '로그인이 필요합니다.')  # 오류 메시지 설정
        return redirect('accounts')
    
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user
            unfinished.save()
            form.save()
            return redirect('notice')
    else:
        form = PostModelForm()
    return render(request, 'form_create_n.html', {'form':form})


def post_detail_n(request, id): # 글 들어가서 자세히 보는 거
    post = get_object_or_404(noticePost, pk=id)
    context={
        'noticePost':post
    }
    return render(request, 'post_detail_n.html', context)

def post_update_n(request, id): # 수정하기
    post = get_object_or_404(noticePost, pk=id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post) #instance는 기존내용 가져오기
        if form.is_valid():
            form.save()
            return redirect('notice')
    else:
        form = PostModelForm(instance=post)
        return render(request, 'form_create_n.html',{'form':form, 'id':id})
    
    
def post_delete_n(request, id): # 삭제하기
    post = noticePost.objects.get(pk=id)
    post.delete()
    return redirect('notice')
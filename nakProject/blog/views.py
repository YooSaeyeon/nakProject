from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import PostModelForm, CommentForm
from .models import blogPost, blogComment

# Create your views here.
def blog(request):
    posts = blogPost.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 5)
    pagnum = request.GET.get('page')
    posts = paginator.get_page(pagnum)
    return render(request, 'blog.html', {'posts':posts})

def create_b(request):
    if not request.user.is_authenticated:  # 사용자가 인증되지 않은 경우
        messages.error(request, '로그인이 필요합니다.')  # 오류 메시지 설정
        return redirect('accounts')
    
    if request.method == 'POST' or request.method == 'FILES':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user
            unfinished.save()
            form.save()
            return redirect('blog')
    else:
        form = PostModelForm()
    return render(request, 'form_create_b.html', {'form':form})


def post_detail_b(request, id): # 글 들어가서 자세히 보는 거
    post = get_object_or_404(blogPost, pk=id)
    comment_form = CommentForm()
    context={
        'blogPost':post,
        'comment_form': comment_form
    }
    return render(request, 'post_detail_b.html', context)

def post_update_b(request, id): # 수정하기
    post = get_object_or_404(blogPost, pk=id)
    if request.method == 'POST' or request.method == 'FILES':
        form = PostModelForm(request.POST, request.FILES, instance=post) #instance는 기존내용 가져오기
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = PostModelForm(instance=post)
        return render(request, 'form_create_b.html',{'form':form, 'id':id})
    
    
def post_delete_b(request, id): # 삭제하기
    post = blogPost.objects.get(pk=id)
    post.delete()
    return redirect('blog')


def create_comment_b(request, id):
    filled_form = CommentForm(request.POST)
    
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.article = get_object_or_404(blogPost, pk=id)
        finished_form.author = request.user
        finished_form.save()
    return redirect('post_detail_b', id)


def update_comment_b(request, blogPost_id, com_id):
    my_com = blogComment.objects.get(id=com_id)
    comment_form = CommentForm(instance=my_com)
    if request.method == "POST":
        update_form = CommentForm(request.POST, instance=my_com)
        if update_form.is_valid():
            update_form.save()
            return redirect('post_detail_b', blogPost_id)
    else:
        return render(request, 'comment_update_b.html', {'comment_form' : comment_form})
    
    
def delete_comment_b(request, blogPost_id, com_id):
    my_com = blogComment.objects.get(id=com_id)
    my_com.delete()
    
    return redirect('post_detail_b', blogPost_id)
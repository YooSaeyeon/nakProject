from django import forms
from .models import blogPost, blogComment

class PostModelForm(forms.ModelForm):
    class Meta:
        model = blogPost
        #어떤 필드를 입력 받을지 서주기
        fields = ['title', 'photo', 'body'] #필드가 많을 때는 __all__이라고 적으면
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = blogComment
        fields = ['comment']
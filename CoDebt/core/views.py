from django.shortcuts import render, get_object_or_404
from .forms import UserComment
from .models import CustomUser, Debtor


# Create your views here.

def index(request):
    return render(request, 'core/index.html')


def register(request):
    return render(request, 'core/register.html')


def make_comment(request):
    comment_form = UserComment(request.POST or None)
    user_commenting = request.user
    post_commenting_on = get_object_or_404(Debtor)
    if request.method == 'POST':
        print(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user_commenting = user_commenting
            new_comment.posted_on = post_commenting_on
            new_comment.save()
    context = {
        'comment_form': comment_form,
        'commenter': user_commenting,
        'commenting_on': post_commenting_on
    }
    return render(request, 'core/comment.html', context)

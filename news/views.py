from django.shortcuts import render, get_object_or_404
from .models import NewPost, Comment
from .forms import CommentForm


def posts_list(request):
    posts = NewPost.objects.all()
    return render(request, "news/posts_list.html", {"posts": posts})


def post_details(request, blog_id):
    post = get_object_or_404(NewPost, pk=blog_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            comment_text = form.cleaned_data["text"]
            comment = Comment(post=post, title=title, author=request.user.username, text=comment_text)
            comment.save()
    form = CommentForm()
    return render(request, "news/post_detail.html", {"post": post, "form": form})
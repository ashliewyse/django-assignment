from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ContactForm

def home(request):
    return render(request, "main/home.html")

def about(request):
    return render(request, "main/about.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # for now we won't email; we just show success
            return render(request, "main/contact_success.html", {"data": form.cleaned_data})
    else:
        form = ContactForm()

    return render(request, "main/contact.html", {"form": form})
@login_required
def dashboard(request):
    return render(request, "main/dashboard.html")

from .forms import CommentForm
from .models import Comment
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def comments(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if request.user.is_authenticated:
                comment.user = request.user
            comment.save()
            return redirect("comments")
    else:
        form = CommentForm()

    all_comments = Comment.objects.order_by("-created_at")

    return render(request, "main/comments.html", {
        "form": form,
        "comments": all_comments
    })

from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, "main/profile.html")

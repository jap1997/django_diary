from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Page
@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def list_pages(request, pid=None):
    if pid is None:
        user_diary_pages = Page.objects.filter(author__username=request.user)
        return render(request, 'list.html', {'pages': user_diary_pages})
    return render(request, 'page.html')
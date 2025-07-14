from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from .models import Page
@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def list_pages(request, pid=None):
    if pid is None:
        user_diary_pages = Page.objects.filter(author__username=request.user)
        return render(request, 'list.html', {'pages': user_diary_pages})
    else:
        pages = Page.objects.filter(id=pid)
        if not pages.count():
            return HttpResponse(status=404)
        return render(request, 'page.html', { 'page': pages.first() })

@login_required
def create_page(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if not title or not content:
            return HttpResponse('Title and content missing', status=400)
        else:
            Page.objects.create(author=request.user, title = title, content = content)
            return redirect('list')
    return render(request, 'create.html')
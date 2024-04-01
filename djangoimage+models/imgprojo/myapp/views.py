from django.shortcuts import render
from .forms import MediaForm
from .models import Media

def media_upload(request):
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = MediaForm()
    return render(request, 'upload_media.html', {'form': form})

def display_media(request):
    media = Media.objects.all()
    return render(request, 'display_media.html', {'media': media})

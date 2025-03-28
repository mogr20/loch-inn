from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Music_Embed, Local_List


# Create your views here.
class HomePage(TemplateView):
    """
    """
    template_name = 'jukebox/index.html'


@login_required
def add_to_local_list(request, embed_id):
    # Get the song (Music_Embed) by its ID
    song = get_object_or_404(Music_Embed, id=embed_id)

    # Check if the song is already in the user's local list
    if Local_List.objects.filter(embed_id=song, user_id=request.user).exists():
        messages.warning(request, "This song is already in your local list.")
    else:
        # Add the song to the local list
        Local_List.objects.create(embed_id=song, user_id=request.user)
        messages.success(request, "Song added to your local list!")

    # Redirect back to the index page
    return redirect('index')  # Replace 'index' with the name of your indexview


def index():
    # Get all songs from the Music_Embed model
    songs = Music_Embed.objects.all()
    return render(request, 'jukebox/index.html')


def search(request, query=None):
    """"
    """
    # Get the search query from the URL
    print("Request is: ", request)
    for item in request.GET.items():
        print("Item is: ", item)

    if query:
        # Filter songs based on the search query (case-insensitive search)
        songs = Music_Embed.objects.filter(song_name__icontains=query)
    else:
        songs = Music_Embed.objects.all()

    if songs.count() == 0:
        # If no songs match the query, show a message
        messages.info(request, "No songs found matching your search.")
        # If no query, show all songs
        songs = Music_Embed.objects.all()

    # Pass the songs and the query back to the template
    return render(request, 'jukebox/index.html', {'songs': songs})
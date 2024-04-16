from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse


# Create your views here.
def index(request):
  # return HttpResponse('My fave movies')
  context = {
      'first_name': 'Kassandra',
      'films': ["princess Bride", "Barbie", "On The basis of Sex"]
  }
  return render(request, 'movies/index.html', context)
  # return HttpResponseRedirect(request, reverse("home", kwargs=context))


def about(request):
  return render(request, 'movies/about.html')

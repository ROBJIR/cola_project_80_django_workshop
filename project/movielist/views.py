from movielist.models import Movie
from movielist.serializers import MovieSerializer
from rest_framework import generics
from django.views import View
from django.shortcuts import render

class MovieHomeView(View):
    def __init__(self):
        self.webpageattributes = {
                                      "application_name": "Workshop Django Rest API Framework"
                                    , "application_ligth_name": "Workshop Django Rest API"
                                  }
        self.webdata = {
                            "datamain": ""
                        }
    def get(self, request):
        return render(request, "main.html", context={"WebPageAttributes" : self.webpageattributes, "WebData" : self.webdata})

class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

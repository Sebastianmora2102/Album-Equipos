from django.urls import reverse_lazy 
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from album.models import Team, Player
from rest_framework import generics
from .serializers import TeamSerializer, PlayerSerializer

# Create your views here.

class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class TeamListView(ListView):
    model = Team

class TeamDetailView(DetailView):
    model = Team

class PlayerListView(ListView):
    model = Player

class PlayerDetailView(DetailView):
    model = Player

class PlayerUpdate(UpdateView):
    model = Player
    fields = '__all__' 

class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'

class PlayerDelete(DeleteView):
    model = Player
    success_url = reverse_lazy('player-list')

class TeamUpdate(UpdateView):
    model = Team
    fields = '__all__' 

class TeamCreate(CreateView):
    model = Team
    fields = '__all__'

class TeamDelete(DeleteView):
    model = Team
    success_url = reverse_lazy('team-list')
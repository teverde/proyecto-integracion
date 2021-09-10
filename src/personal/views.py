from django.shortcuts import render
import requests

url = "https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/560"

# Create your views here.
def home_screen_view(request):
  return render(request, "personal/home.html", {})

def users_index_view(request):
  content = []
  for i in range (1,9):
    response = requests.get(f'{url}/users?_page={i}')
    for user in response.json():
      content.append([f'{user["name"]} {user["lastName"]}',user["id"]])

  context = {
    'users': content,
  }
  return render(request, "personal/users_index.html", context)

def cities_index_view(request):
  content = []
  for i in range (1,9):
    response = requests.get(f'{url}/cities?_page={i}')
    for city in response.json():
      content.append([city["name"], city["id"]])

  context = {
    'cities': content
  }
  return render(request, "personal/cities_index.html", context)

def user_view(request):
  context ={

  }
  return render(request, "personal/user.html", context)

def city_view(request):
  context ={
    
  }
  return render(request, "personal/city.html", context)

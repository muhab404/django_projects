
from django.shortcuts import  render
import requests
# Create your views here.

def boards_list(request):
    backend_url = "http://127.0.0.1:8000/"
    headers = {'Content-Type':"application/json"}
    response =requests.get(backend_url, headers=headers)
    boards=response.json()
   
    
    return render(request,'home.html',{'boards':boards['Results']})

def board_topics(request,board_id):

    backend_url = "http://127.0.0.1:8000/boards/"+str(board_id)+"/"
    headers = {'Content-Type':"application/json"}
    response =requests.get(backend_url, headers=headers)
    board=response.json()
   
    
    return render(request,'topics.html',{'board':board['Results']})

import socket
from django.http.response import JsonResponse

def returnTestResponse(request):
    responseString = 'this response is from ' + str(socket.gethostbyname(socket.gethostname()))
    return JsonResponse({'msg':responseString}, status=200)
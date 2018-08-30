from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Create your views here.
def get_price(request):
    if request.method == 'GET':
        # logic goes here to look up pricing
        return HttpResponse("Hello, world.")
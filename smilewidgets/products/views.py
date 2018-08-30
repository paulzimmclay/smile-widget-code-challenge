import json
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product, ProductPrice


@csrf_exempt # For testing with Postman
def get_price(request):
    # get incoming parameters, save as dictionary/variables
    params = json.loads(request.body)
    code = params['code']
    date = params['date']

    # check code and date against changed prices
    

    new_price = model_to_dict(ProductPrice.objects.get(code=params['code']))
    # if match, return new price
    # else, return old price


    return HttpResponse(new_price['price'])
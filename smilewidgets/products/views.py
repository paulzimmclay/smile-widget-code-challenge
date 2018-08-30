import json
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product, ProductPrice


@csrf_exempt # For testing with Postman
def get_price(request):
    # Look up ProductPrice according to incoming data
    # new_price = model_to_dict(Product.objects.get(code=params['code']))

    params = json.loads(request.body) # Get incoming data, save as dict
    # given this, check against ProductPrice
    new_price = model_to_dict(ProductPrice.objects.get(code=params['code']))
    print(new_price['price'])



    return HttpResponse(new_price['price'])
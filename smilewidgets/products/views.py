import json
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product, ProductPrice


@csrf_exempt # For testing with Postman
def get_price(request):    
    # get incoming parameters as json, save as dictionary/variables
    params = json.loads(request.body)
    # check incoming keys to make sure they are correct
    # if they are, continue. else, notify user
    try:
        code = params['code']
        date = params['date']
    except KeyError:
        return HttpResponse('Incorrect keys! Make sure you are sending two keys, "dict" and "date"')
    
    # check code against product price models
    try:
        # Makes sure code is valid
        new_price = model_to_dict(ProductPrice.objects.get(code=code))
    except ProductPrice.DoesNotExist:
        # Notify user if code is incorrectly formatted
        return HttpResponse('The code you submitted is incorrect. Please try again')

    # check submitted date against calendar date
    # try:
    date_match = model_to_dict(ProductPrice.objects.filter(date_start=date).first())
    print('date', date_match['date_start'], date)
    # finally:
    return HttpResponse('That date didn\'t match!')
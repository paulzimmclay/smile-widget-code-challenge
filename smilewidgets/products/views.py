import json
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product, ProductPrice, GiftCard


@csrf_exempt # For testing with Postman
def get_price(request):    
    # get incoming parameters as json, save as dictionary/variables
    params = json.loads(request.body)
    # check incoming keys to make sure they are correct
    # if they are, continue. otherwise, notify user
    try:
        code = params['code']
        date = params['date']
    except KeyError:
        return HttpResponse('Incorrect keys. Make sure you are sending two keys, "code" and "date".')


    # check code against product price models
    # Makes sure code is valid
    if ProductPrice.objects.filter(code=code).exists():
        objects_with_code = ProductPrice.objects.filter(code=code).values()
        # print(type(objects_with_code))
    else:
        return HttpResponse('The code you submitted is incorrect. Please try again.')

    # get standard price
    price = model_to_dict(Product.objects.get(code=code))

    # if date range on price calendar includes date submitted, get new price
    for item in objects_with_code:
        # print(item['id'], item['date_start'], date, item['date_end'])
        print(str(item['date_start']), date, str(item['date_end']) )
        if str(item['date_start']) <= date and str(item['date_end']) >= date:
            price = item['price']
    
    



    return JsonResponse({'price': price})


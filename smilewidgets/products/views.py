import json, datetime
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product, ProductPrice, GiftCard


@csrf_exempt # For testing with Postman
def get_price(request):
    """for getting prices on proucts, considering a price calendar (found in ProductPrice)
    
    Arguments:
        request {
                "code" - the product code
                "date" - the current date
                "coupon" - (optional) a coupon code
                }
    
    Returns:
        {"price":"price accoridng to price calendar"}
    """


    # get incoming parameters as json, save as dictionary/variables
    params = json.loads(request.body)
    # check incoming keys to make sure they are correct
    # if they are, continue. otherwise, notify user
    try:
        code = params['code']
        date = params['date']
    except KeyError:
        return JsonResponse({'error':'Incorrect keys. Make sure you are sending at least two keys, "code" and "date".'}, status=400)
        

    # check for valid input date
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return JsonResponse({'error':'your date is incorrectly formatted'}, status=400)

    # check code against product price models
    # Makes sure code is valid
    if ProductPrice.objects.filter(code=code).exists():
        objects_with_code = ProductPrice.objects.filter(code=code).values()
        # print(type(objects_with_code))
    else:
        return JsonResponse({'error':'The code you submitted is incorrect. Please try again.'}, status=400)

    # get standard price
    price = model_to_dict(Product.objects.get(code=code))['price']

    # if date range on price calendar includes date submitted, get new price
    for item in objects_with_code:
        if str(item['date_start']) <= date and str(item['date_end']) >= date:
            price = item['price']
    
    # No coupon code (not present)
    try: 
        giftcard_code = params['giftcard']
    except KeyError:
        giftcard_code = None


    if GiftCard.objects.filter(code=giftcard_code).exists():
        # Correct coupon code (matches something in db)
        current_giftcard = model_to_dict(GiftCard.objects.get(code=giftcard_code))
        # Check to make sure giftcard is still valid
        # Check for giftcards that have start and end date
        if current_giftcard['date_start'] and current_giftcard['date_end']:
            if str(current_giftcard['date_start']) <= date and str(current_giftcard['date_end']) >= date:
                price = price - current_giftcard['amount']
            else:
                return JsonResponse({"error":"that giftcard code is expired"})
        # Check for giftcards that have only start date
        elif current_giftcard['date_start']:
            if str(current_giftcard['date_start']) <= date:
                price = price - current_giftcard['amount']
            else:
                return JsonResponse({"error":"that giftcard code is expired"})
        else:
            return JsonResponse({"error":"that giftcard code is expired"})
    else: 
        # Incorrect coupon code (does not match something in db)
        return JsonResponse({"error":"that giftcard code does not exist"})
        
    # convert from cents to dollars
    formatted_price = int(price / 100)
    
    # make sure price won't drop below zero:
    if formatted_price <= 0:
        formatted_price = 0

    return JsonResponse({'price': formatted_price})


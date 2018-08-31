# New fork info:

Hi! Thanks for the opportunity to interview with Smile Direct Club! Any feedback is much appreciated!

The data I used to create the ProductPrice models is stored in products_productprice.json

The get_price function based view does this:
1. gets incoming parameters as json, saves it as a dictionary, then puts those values into single variables
1. checks incoming keys, throws error if they are incorrect
1. checks for valid input date, throws error if incoming date is incorrect
1. checks incoming code against ProductPrice models. if incorrect, throws error
1. checks incoming date range against date range of price calendar
1. checks to see if gift card code is present
1. if present, checks input date vs gift card code date, subtracts giftcard amount
1. makes sure output price won't drop below zero
1. returns price

# smile-widget-code-challenge

The Smile Widget Company currently sells two types of smile widgets: a Big Widget and a Small Widget.  We'd like to add more flexibility to our product pricing.

## Setup with Docker
1. Install Docker (https://docs.docker.com/install/)
2. Fork this repository.
3. `>>> docker-compose up --build`

## Setup without Docker
1. Install Python (>3.4)
2. Install postgres.  By default the Django app will connect to the database named 'postgres'.  See `settings.DATABASES`.
3. Fork this repository, then clone your repository locally.
4. Install requirements.
  * `>>> pip install -r requirements.txt`
5. Run migrations.
  * `>>> python manage.py migrate`
6. Load data from fixtures:
  * `>>> python manage.py loaddata 0001_fixtures.json`

### Technical Requirements
* We currently have two products with the following prices:
    * Big Widget - $1000
    * Small Widget - $99
* These products, along with existing gift cards are already setup in the database.  Study the existing models and initial data.
* Create a new ProductPrice model and setup the following price schedule:    
  * Black Friday Prices (November 23, 24, & 25)
    * Big Widget - $800
    * Small Widget - FREE!
  * 2019 Prices (starting January 1, 2019)
    * Big Widget - $1200
    * Small Widget - $125
* Build a JSON API endpoint that accepts a product code, date, and (optional) gift card and returns product price.
  * The endpoint should live at `api/get-price` and accept the following parameters:
    * `"productCode"`
    * `"date"`
    * `"giftCardCode"`
* Make all of your changes in a new feature branch and submit a pull request to _your own forked repo_.

### Additional Information
* Please use Django Rest Framework or a Python HTTP framework of your choice to create the endpoint.
* Just as a general guideline, we've designed this exercise to take less than 4 hours.

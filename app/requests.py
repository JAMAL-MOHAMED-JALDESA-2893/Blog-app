import urllib.request,json
from .models import Quotes



def configure_request(app):
    global base_url
    
    base_url = app.config['QUOTE_API_BASE_URL']


def get_quote():
    '''
    Function that gets the random quotes
    '''
    get_article_details_url = 'http://quotes.stormconsultancy.co.uk/random.json'.format()
    with urllib.request.urlopen(get_article_details_url) as url:
        quote_data = url.read()
        quote_data_response = json.loads(quote_data)
        
       
    return quote_data_response


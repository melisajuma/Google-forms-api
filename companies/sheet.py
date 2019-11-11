import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
from .models import someModel

# use creds to create a client to interact with the Google Drive API

def form_responses():
    '''
    returns the json response from the api
    '''
    
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    #authorize
    client = gspread.authorize(creds)
    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("General public response").sheet1
    pp = pprint.PrettyPrinter()

    # Extract and print all of the values
    print(sheet.get_all_records())
    json_results=None

    if sheet:
        '''
        checking if there is a response from the form api
        then you now call process response
        '''
        json_results=process_response

    return json_results



def process_response(json_response):
    '''
    this function creates the instances and saves to db
    and returns the data
    '''
    json_data=[]

    for res in json_response:
        '''
        looping the json response array
        '''
        name=res['write your name']
        Field_of_study=res['what is your field of study/employement']
        age_group=res['what is your age']
        crypto_knowledge=res['How much do you know about cryptocurrencies (Bitcoin,Etherium,etc)?']
        crypto_use=res['Have you used crypto before?']
        crypto_use_followup=res['Any challenges']
        crypto_discourage=res['what would discourage you']
        crypto_discourage_other=res['any other']
        crypto_encourage=res['what would encourage you']
        crypto_value=res['what is its perceived value']
	

        if name:
            '''
            making sure each response has a name attached to it
            '''
            application_object = someModel.objects.create(name=name,age_group=age_group,crypto_knowledge=crypto_knowledge,crypto_use=crypto_use,crypto_use_followup=crypto_use_followup,crypto_discourage=crypto_discourage,crypto_discourage_other=crypto_discourage_other,crypto_encourage=crypto_encourage,crypto_value=crypto_value)
            application_object.save()
            json_data.apppend(application_object)

    return json_data      
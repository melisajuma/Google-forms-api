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
    # print(sheet.get_all_records())
    processed_data=sheet.get_all_records()
    json_results=None

    if sheet:
        '''
        checking if there is a response from the form api
        then you now call process response
        '''
        json_results=processed_data

    return json_results



def process_response():
    '''
    this function creates the instances and saves to db
    and returns the data
    '''
    json_response= form_responses()
    json_data=[]
    print('**************************************************')
    for res in json_response:
        '''
        looping the json response array
        '''
        # name=res['write your name']
        field_of_study=res['What is your field of Study/ Employment?']
        age_group=res['Which one of these is your age group?']
        crypto_knowledge=res['How much do you know about cryptocurrencies( Bitcoin, Ethereum, etc.)?']
        crypto_use=res['Have you ever used cryptocurrencies in transactions?']
        crypto_use_followup=res["If the answer above is 'yes', are there any challenges you might have faced in the process?"]
        crypto_discourage=res['What would discourage you from using cryptocurrencies?']
        crypto_discourage_other=res["If your answer is 'other', kindly state any other reason:"]
        crypto_encourage=res['If you were to use cryptocurrencies, what would encourage you to use them?']
        crypto_encourage_other=res["If your answer is 'other', kindly state any other reason:"]
        crypto_value=res['Cryptocurrencies have no tangible form. Do you think that diminishes their perceived value?']
       
        
        # print('name*************************************')

        if age_group:
            '''
            making sure each response has a name attached to it
            '''
            application_object = someModel.objects.create(
                            age_group=age_group,crypto_knowledge=crypto_knowledge,
                            crypto_use=crypto_use,crypto_use_followup=crypto_use_followup,
                            crypto_discourage=crypto_discourage,crypto_discourage_other=crypto_discourage_other,
                            crypto_encourage=crypto_encourage,crypto_value=crypto_value,
                            crypto_encourage_other=crypto_encourage_other,field_of_study=field_of_study)
            application_object.save()
            json_data.append(application_object)

    return json_data      
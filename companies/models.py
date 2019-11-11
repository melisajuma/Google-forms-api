from django.db import models


class someModel(models.Model):
    '''
        example model to use...
        so like the questions unaeza ongeza kwa the model fied
        ndio someone else reading your fields anaeza elewa
		
        exmaple
        crypto_knowledge=models.CharField(help_text='How much do you know about cryptocurrencies (Bitcoin,Etherium,etc)?')
	
    '''
    name=models.CharField(max_length=250)
    age_group=models.CharField(max_length=50)
    crypto_knowledge=models.CharField(max_length=250)
    crypto_use_followup=models.TextField(max_length=250)
    crypto_discourage=models.CharField(max_length=250)
    crypto_discourage_other=models.TextField(max_length=250)
    crypto_encourage=models.TextField(max_length=250)
    crypto_value=models.CharField(max_length=250)

    
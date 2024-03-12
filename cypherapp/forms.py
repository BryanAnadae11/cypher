from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class ContactForm(forms.Form):
	name= forms.CharField(max_length=45)
	email= forms.EmailField()
	country= forms.CharField(max_length=30)
	message= forms.CharField(widget=forms.Textarea)

class RequestForm(forms.Form):
    email = forms.EmailField(required=True)
    amount = forms.FloatField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class BonusForm(ModelForm):
	class Meta:
		model= Bonus
		fields= '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class ClientForm(ModelForm):
	class Meta:
		model= Client
		fields= '__all__'
		exclude= ['user','code', 'recommended_by', 'deposit', 'balance', 'withdrawal', 'profit','roi', 'running_days']


class cybersecurityDepositForm(forms.Form):
	amount= forms.FloatField(required= True)

class cryptographyDepositForm(forms.Form):
	amount= forms.FloatField(required= True)

class NftDepositForm(forms.Form):
	amount= forms.FloatField(required= True)

class BlockchaindevelopmentDepositForm(forms.Form):
	amount= forms.FloatField(required= True)

class DaoDepositForm(forms.Form):
	amount= forms.FloatField(required= True)

class smartcontractDepositForm(forms.Form):
	amount= forms.FloatField(required= True)

class DefiDepositForm(forms.Form):
	amount= forms.FloatField(required= True)



'''
class SeedsDepositForm(forms.Form):

	CHOICES= ( ('0.011112#Seeds / Cocoa#30', '0.011112#Seeds / Cocoa#30'),
		('0.011112#Seeds / Cotton#30', '0.011112#Seeds / Cotton#30'), )

	CURRENCY= ( ('USDTTRC20', 'USDTTRC20'),
		('btc', 'btc'),
		('eth', 'eth'),
		('doge', 'doge'),
		('trx', 'trx'),
		('sol', 'sol'),
		('ltc', 'ltc'),
		('dot', 'dot'),
		('XLM', 'XLM'),
		('ADA', 'ADA'),
		('axs', 'axs'),
		('floki', 'floki'),
		('busderc20', 'busderc20'),
		('dash', 'dash'),
		('etc', 'etc'),
		('xmr', 'xmr'),
		('bnbbsc', 'bnbbsc'),
		('shib', 'shib'),
		('bch', 'bch'),
		('xrp', 'xrp'), )

	investment_plan= forms.ChoiceField(choices=CHOICES, required=True)
	amount= forms.FloatField(required= True)
	pay_currency= forms.ChoiceField(choices=CURRENCY, required=True)

class LivestockDepositForm(forms.Form):

	CHOICES= ( ('0.0083333#livestock / Cattles#30', '0.0083333#livestock / Cattles#30'),
		('0.0017534#livestock / fishery #30', '0.0017534#livestock / fishery #30'),
		('0.0017534#livestock / poultry #30', '0.0017534#livestock / poultry #30'),
		('0.0017534#livestock / Bee farming #30', '0.0017534#livestock / Bee farming #30'),
		('0.0017534#livestock / Piggery #30', '0.0017534#livestock / Piggery #30'),
		#('0.0017534#Staking / Doge#365', '0.021333#Staking / Doge #365'),
		#('0.0017534#Staking / ADA#365', '0.021333#Staking / ADA#365'),
		#('0.0017534#Staking / Ripple#365', '0.021333#Staking / Ripple#365'),
		)

	CURRENCY= ( ('USDTTRC20', 'USDTTRC20'),
		('btc', 'btc'),
		('eth', 'eth'),
		('doge', 'doge'),
		('trx', 'trx'),
		('sol', 'sol'),
		('ltc', 'ltc'),
		('dot', 'dot'),
		('XLM', 'XLM'),
		('ADA', 'ADA'),
		('axs', 'axs'),
		('floki', 'floki'),
		('busderc20', 'busderc20'),
		('dash', 'dash'),
		('etc', 'etc'),
		('xmr', 'xmr'),
		('bnbbsc', 'bnbbsc'),
		('shib', 'shib'),
		('bch', 'bch'),
		('xrp', 'xrp'), )
	investment_plan= forms.ChoiceField(choices=CHOICES, required=True)
	amount= forms.FloatField(required= True)
	pay_currency= forms.ChoiceField(choices=CURRENCY, required=True)

class RawresourceDepositForm(forms.Form):

	CHOICES= ( ('0.019#Raw resources / hides,and skin#30', '0.019#Raw resources / hides,and skin#30'),
		('0.019#Raw resources / flour#30', '0.019#Raw resources / flour#30'),
		('0.019#Raw resources / horns#30', '0.019#Raw resources / horns#30')
		)

	CURRENCY= ( ('USDTTRC20', 'USDTTRC20'),
		('btc', 'btc'),
		('eth', 'eth'),
		('doge', 'doge'),
		('trx', 'trx'),
		('sol', 'sol'),
		('ltc', 'ltc'),
		('dot', 'dot'),
		('XLM', 'XLM'),
		('ADA', 'ADA'),
		('axs', 'axs'),
		('floki', 'floki'),
		('busderc20', 'busderc20'),
		('dash', 'dash'),
		('etc', 'etc'),
		('xmr', 'xmr'),
		('bnbbsc', 'bnbbsc'),
		('shib', 'shib'),
		('bch', 'bch'),
		('xrp', 'xrp'), )

	investment_plan= forms.ChoiceField(choices=CHOICES, required=True)
	amount= forms.FloatField(required= True)
	pay_currency= forms.ChoiceField(choices=CURRENCY, required=True)

class PortfolioDepositForm(forms.Form):

	CHOICES= ( ('0.005#Portfolio management/ Starter package#30', '0.005#Portfolio management/ Starter package#30'),
		('0.004#Portfolio management/ Standard package#30', '0.004#Portfolio management/ Standard package#30'),
		('0.01167#Portfolio management/ Premium package#30', '0.01167#Portfolio management/ Premium package#30'),
		('0.0067#Portfolio management/ Gold package#30', '0.0067#Portfolio management/ Gold package#30'),
		('0.033#Portfolio management/ Executive package/ NFP#90', '0.033#Portfolio management/ Executive package/ NFP#90'),
		('0.067#Portfolio management/ Executive package/ MMA#30', '0.067#Portfolio management/ Executive package/ MMA#30'),
		('0.00556#Portfolio management/ Executive package/ FOMC#180', '0.00556#Portfolio management/ Executive package/ FOMC#180'),
		)

	CURRENCY= ( ('USDTTRC20', 'USDTTRC20'),
		('btc', 'btc'),
		('eth', 'eth'),
		('doge', 'doge'),
		('trx', 'trx'),
		('sol', 'sol'),
		('ltc', 'ltc'),
		('dot', 'dot'),
		('XLM', 'XLM'),
		('ADA', 'ADA'),
		('axs', 'axs'),
		('floki', 'floki'),
		('busderc20', 'busderc20'),
		('dash', 'dash'),
		('etc', 'etc'),
		('xmr', 'xmr'),
		('bnbbsc', 'bnbbsc'),
		('shib', 'shib'),
		('bch', 'bch'),
		('xrp', 'xrp'), )

	investment_plan= forms.ChoiceField(choices=CHOICES, required=True)
	amount= forms.FloatField(required= True)
	pay_currency= forms.ChoiceField(choices=CURRENCY, required=True)
'''





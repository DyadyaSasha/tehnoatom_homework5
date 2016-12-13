from django import forms
from datetime import date
import re
from .models import Acount, Charge

class AcountForm(forms.ModelForm):
    
    class Meta:
        model = Acount
        fields = ('name', 'number')

    def clean(self):
        #CREDIT_CARD_VALID = r'^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\\d{3})\d{11})$'
        number = self.cleaned_data.get('number')
        #number = number.replace(' ', '').replace('-', '')
        number = number.replace(' ', '')
        #if not re.match(CREDIT_CARD_VALID, number):
        if len(number) != 16:    
            self.add_error(
                'number', "Card number you specified is not valid.")
        self.cleaned_data['number'] = number
        return self.cleaned_data

class ChargeForm(forms.ModelForm):

    class Meta:
        model = Charge
        fields = ('transaction', 'dat')    
    def clean(self):
        cleaned_data = super(ChargeForm, self).clean()
        transaction = cleaned_data.get('transaction')
        dat = cleaned_data.get('dat')
        if transaction == 0 or transaction is None:
            self.add_error('transaction', "Transaction can't equal zero")
        if transaction < 0 and dat > date.today():
            self.add_error('transaction', "Invalid transaction")
        return cleaned_data
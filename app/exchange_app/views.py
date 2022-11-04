from django.shortcuts import render
import requests

def exchange(request):

    response = requests.get(url='https://www.cbr-xml-daily.ru/daily_json.js').json()
    currencies = response.get('Valute')

    if request.method == 'POST':
        from_amount = float(request.POST.get('amount'))
        from_curr = request.POST.get('from_curr')
        to_curr = request.POST.get('to_curr')

        converted_amount = round((currencies[to_curr]['Value'] / currencies[from_curr]['Value']) * float(from_amount), 2)

        context = {
            'currencies': currencies,
            'converted_amount': converted_amount,
            'amount': from_amount,
            'from_curr': from_curr,
            'to_curr': to_curr
        }
    else:
        context = {
            'currencies': currencies
        }

    return render(request=request, template_name='exchange_app/index.html', context=context)

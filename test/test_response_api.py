response = {'costOfNew': 5.55,
 'costTotal': 110.97,
 'countEmpty': False,
 'msg': '',
 'passedSeconds': 4,
 'quantity': '2',
 'service': 'full',
 'status': 'success',
 'values': {'0': {'accepted': '1',
                  'cost': 0,
                  'date': '2022-12-01 12:02:11',
                  'passedSeconds': 0,
                  'phoneFrom': 'YandexGo',
                  'service': 'full',
                  'text': 'Your confirmation code: 582651.\nMOoS+UjeNYR',
                  'type': 'sms'},
            '1': {'accepted': '1',
                  'cost': 0,
                  'date': '2022-12-01 11:53:28',
                  'passedSeconds': 0,
                  'phoneFrom': 'Uber',
                  'service': 'full',
                  'text': 'Your confirmation code is 483237. Please enter it '
                          'in the text field.',
                  'type': 'sms'}}}

is_uber = True

if is_uber:
    for i in response['values']:
        if 'Yandex' in response['values'][i]['phoneFrom']:
            confirmation_code = response['values'][i]['text'].replace('.', ' ').replace('\n', ' ').split()
            print(confirmation_code)
            for code in confirmation_code:
                if code.isdigit():
                    print(code)

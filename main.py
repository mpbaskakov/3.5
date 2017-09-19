from pprint import pprint

import osa


def tempconverter(file):
    client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
    with open(file, 'r') as f:
        temp = [f for f in f.read().split() if f != 'F']
        for t in temp:
            t = client.service.ConvertTemp(t, 'degreeFahrenheit', 'degreeCelsius')
            print(round(t, 1), 'градусов Цельсия')


def currencyconverter(file):
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    with open(file, 'r') as f:
        money = f.read().split()
        for m in money[1::3]:
            money[money.index(m)] = client.service.ConvertToNum('', money[money.index(m) + 1], 'RUB', m, 'true')
        for m in money[2::3]:
            money[money.index(m)] = 'RUB'
        pprint(money)


def lengthconverter(file):
    client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
    with open(file, 'r') as f:
        temp = f.read().split()
        for t in temp:
            if t == 'mi':
                temp[temp.index(t)] = 'km'
            try:
                temp[temp.index(t)] = float(client.service.ChangeLengthUnit(t, 'Miles', 'Kilometers'))
            except ValueError:
                pass
        pprint(temp)


def main():
    func = int(input('Какую операцию вы хотите произвести? Конвертацию температуры(1), валюты(2) или расстояний(3)?'))
    file = input('Введите путь к файлу:')
    if func == 1:
        tempconverter(file)
    elif func ==2:
        currencyconverter(file)
    elif func == 3:
        lengthconverter(file)
    else:
        print('Введите корректный номер операции!')

while True:
     main()


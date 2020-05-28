"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
from datetime import datetime, date, time
import json, os

def load_file_json(file_name, mode):
    data = {}
    if os.path.exists(file_name):
        with open(file_name, mode, encoding='utf-8') as f:
            data = json.load(f)
    else:
        print('файл не существует')
    return (data)

def load_txt(file_name, mode):
    if os.path.exists(file_name):
        with open(file_name, mode, encoding='utf-8') as f:
            data = f.read()
    else:
        data = 0
    return (data)

def save_json(file_name, mode, data):
    with open(file_name, mode, encoding='utf-8') as f:
        json.dump(data, f)
    return ()

def save_txt(file_name, mode, data):
    with open(file_name, mode, encoding='utf-8') as f:
        f.write(data)
    return (f)

# 1. пополнение счета
def refuel():
    plus = int(input('Введите сумму: '))
    wallet.append(plus)
    return (wallet)

# 2. покупка
def buy():
    purchases = []
    cost = int(input('Введите сумму покупки: '))
    if sum(wallet) >= cost:
        item = input('введите название покупки: ')
        wallet.append(-cost)
        if history.get(datetime.today().strftime("%d/%m/%Y")) != None:
            purchases = history.get(datetime.today().strftime("%d/%m/%Y"))
        purchases.append((item, cost))
        history.update({datetime.today().strftime("%d/%m/%Y"): purchases})
    else:
        print('не хватает средств')
        pass
    return ()

# 3. история покупок
def buy_history():
    return
if __name__=='__main__':
    wallet = []
    wallet.append(int(load_txt('wallet.txt', 'r')))
    history = load_file_json('history.json', 'r')
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            refuel()
            print('на вашем счету: ', sum(wallet))
        elif choice == '2':
            buy()
            print('на вашем счету: ', sum(wallet))
        elif choice == '3':
            print('история покупок: ', history)
        elif choice == '4':
            save_json('history.json', 'w', history)
            save_txt('wallet.txt', 'w', str(sum(wallet)))
            break
        else:
            print('Неверный пункт меню')

balance = int(input('Введіть поточний баланс карти'))
while balance > 0 and input('Хочете зробити покупку (так/ні)?') == 'так':
    price = int(input('Введіть ціну'))
    if balance - price < 0:
        print('Недостатньо коштів!')
    else:
        balance -= price
        print('Сума', price, 'грн. списана з рахунку.')
print('Доступна сума:', balance, 'грн.')
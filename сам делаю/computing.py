def mathematics():
    lst = []
    operations = {
        1: lambda x, y: x + y,
        2: lambda x, y: x / y,
        3: lambda x, y: x ** y,
        4: lambda x, y: x % y,
        5: lambda x, y: x - y
    }

    while True:
        try:
            question = int(input(
                '1 - сложение; 2 - деление; 3 - возведение в степень; 4 - остаток от деления; 5 - вычитание; 6 - сумма всех ранее выбранных значений; 7 - выход из программы. Выбирайте: '))

            if question == 7:
                print('Выход из программы')
                break

            if question == 6:
                print(sum(lst))
                continue

            figure1 = int(input('Введите первую цифру: '))
            figure2 = int(input('Введите вторую цифру: '))

            if question == 2 and figure2 == 0:
                print('Вы не можете делить на 0')
                continue

            if question in operations:
                result = operations[question](figure1, figure2)
                print(result)
                lst.append(result)
            else:
                print('Некорректный выбор операции')

        except ValueError:
            print('Вы ввели не число')


# Запуск функции
mathematics()

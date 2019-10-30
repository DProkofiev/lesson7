import os, shutil, platform, pwd, sys
while True:
    print('1. создать папку')
    print('2. удалить(файл / папку)')
    print('3. копировать(файл / папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        new_folder_name = input('введите название папки, которую хотите создать:')
        if not os.path.exists(new_folder_name):
            os.mkdir(new_folder_name)

    elif choice == '2':
        object_name = input('введите название файла или папки, который хотите удалить:')
        if os.path.exists(object_name):
            if os.path.isfile(object_name):
                os.remove(object_name)
            elif os.path.isdir(object_name):
                os.rmdir(object_name)

    elif choice == '3':
        source_name = input('введите название копируемого файла / папки:')
        dest_name = input('введите название нового файла / папки:')
        if os.path.isfile(source_name):
            shutil.copyfile(source_name, dest_name)
        elif os.path.isdir(source_name):
            shutil.copytree(source_name, dest_name)

    elif choice == '4':
        print('объекты в рабочей папке:')
        for i in os.listdir():
            print(i)

    elif choice == '5':
        print('папки в рабочей папке:')
        for i in os.listdir():
            if os.path.isdir(i):
                print(i)

    elif choice == '6':
        print('файлы в рабочей папке:')
        for i in os.listdir():
            if os.path.isfile(i):
                print(i)

    elif choice == '7':
        print('ваша операционная система: ', os.name, '(', platform.system(), ')')

    elif choice == '8':
        file = sys.argv[0]
        print('имя создателя: ', pwd.getpwuid(os.stat(file).st_uid).pw_name)

    elif choice == '9':
        import victory

    elif choice == '10':
        import walett

    elif choice == '12':
        break

    else:
        print('Неверный пункт меню')
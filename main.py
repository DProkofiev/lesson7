import os, shutil, platform, pwd, sys
from wallet import save_txt

while True:
    print(f'1. создать папку\n'
          f'2. удалить(файл / папку)\n'
          f'3. копировать(файл / папку)\n'
          f'4. просмотр содержимого рабочей директории\n'
          f'5. сохранить содержание рабочей директории в файл\n'
          f'6. посмотреть только папки\n'
          f'7. посмотреть только файлы\n'
          f'8. просмотр информации об операционной системе\n'
          f'9. создатель программы\n'
          f'10. играть в викторину\n'
          f'11. мой банковский счет\n'
          f'12. смена рабочей директории\n'
          f'13. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        new_folder_name = input('введите название папки, которую хотите создать:')
        if not os.path.exists(new_folder_name):
            os.mkdir(new_folder_name)

    elif choice == '2':
        object_name = input('введите название файла или папки, который хотите удалить:')
        try:
            os.remove(object_name) if os.path.isfile(object_name) else os.rmdir(object_name)
        except FileNotFoundError:
            print('объект с таким именем не существует')

    elif choice == '3':
        source_name = input('введите название копируемого файла / папки:')
        dest_name = input('введите название нового файла / папки:')
        try:
            shutil.copyfile(source_name, dest_name) if os.path.isfile(source_name) else shutil.copytree(source_name, dest_name)
        except FileNotFoundError:
            print('объект с таким именем не существует')

    elif choice == '4':
        print('объекты в рабочей папке:','\n'.join(str(x) for x in os.listdir()))


    elif choice == '5':
        save_txt('listdir.txt', 'w', f'files:{[i for i in os.listdir() if os.path.isfile(i)]}\ndirs: {[i for i in os.listdir() if os.path.isfile(i) is False]}')
        print('содержание рабочей директории сохранено в файле listdir.txt:')

    elif choice == '6':
       # print('папки в рабочей папке:')
        print('папки в рабочей папке:','\n'.join(str(x) for x in os.listdir() if os.path.isdir(x)))

    elif choice == '7':
        print('файлы в рабочей папке:','\n'.join(str(x) for x in os.listdir() if os.path.isfile(x)))

    elif choice == '8':
        print('ваша операционная система: ', os.name, '(', platform.system(), ')')

    elif choice == '9':
        file = sys.argv[0]
        print('имя создателя: ', pwd.getpwuid(os.stat(file).st_uid).pw_name)

    elif choice == '10':
        import victory

    elif choice == '11':
        import wallet

    elif choice == '12':
        home_path = (os.environ['HOME'])
        new_path = input(
        'введите путь, например: /Users/dprokofiev/PycharmProjects/lesson05/ или:  /PycharmProjects/lesson04/')
        try:
            if home_path in new_path:
                os.chdir(new_path)
            else:
                os.chdir(home_path + new_path)
        except FileNotFoundError:
            print('путь не существует, повторите ввод')

    elif choice == '13':
        break

    else:
        print('Неверный пункт меню')

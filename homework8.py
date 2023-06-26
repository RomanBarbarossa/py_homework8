phonebook = 'file.txt'


def phonebook_read():
    with open(phonebook, encoding='UTF-8') as file:
        print(file.read())
    

def contact_add():
    in_fio = input('Введите Фамилию, Имя, Отчество через пробел ')
    in_ph = input('Введите телефон ')
    with open(phonebook, 'a', encoding='UTF-8') as file:
        file.write(f'{in_fio} | {in_ph}\n')


def contact_search():
    with open(phonebook, encoding='UTF-8') as file:
        search = input('Введите ФИО или телефон для поиска ')
        file_search = file.read().split('\n')
        searched_contacts_index = list()
        flag = True
        for i in file_search:
            if search.lower() in i.lower():
                searched_contacts_index.append(file_search.index(i))
                print(f'{file_search.index(i)} {i}')
                flag = False
        if flag:
            print('Ничего не найдено!')
        return searched_contacts_index
# Поиск индекса контакта для замены или удаления


def find_contact():
    searched_contacts = contact_search()
    changed_index = searched_contacts[0]
    if len(searched_contacts) != 1:
        print("Укажите номер контакта из списка выше, для продолждения работы")
        changed_index = int(input())
    return changed_index

# Редактирование контакта


def change_contact():
    changed_index = find_contact()
    with open(phonebook, 'r', encoding='UTF-8') as file:
        file_search = file.read().split('\n')
        contact_as_list = file_search[changed_index].split()
    while True:
        print('Введите 0 для замены фамилии, 1 - имени, 2 - отчества,4- тел,\n'
              '5 - всё ок, сохранить')
        mode = int(input())
        if mode == 0:
            contact_as_list[mode] = input('Фамилия: ')
        elif mode == 1:
            contact_as_list[mode] = input('Имя: ')
        elif mode == 2:
            contact_as_list[mode] = input('Отчество: ')
        elif mode == 4:
            contact_as_list[mode] = input('Тел: ')
        elif mode == 5:
            break
    file_search[changed_index] = ''
    for i in contact_as_list:
        file_search[changed_index] += f'{i} '
    rewrite_phonebook(file_search)


# удаление контакта
def delete_contact():
    changed_index = find_contact()
    with open(phonebook, 'r', encoding='UTF-8') as file:
        file_search = file.read().split('\n')
    file_search.pop(changed_index)
    rewrite_phonebook(file_search)
    print('Контакт удален')

# Перезапись файла


def rewrite_phonebook(contacts: list):
    contacts_txt = ''
    for i in range(len(contacts)-1):
        contacts_txt += f'{contacts[i]}\n'
    with open(phonebook, 'w', encoding='UTF-8') as file:
        file.write(contacts_txt)


def main():
    while True:
        print('Введите название команды для справочника \n'
              'add - для добавления контакта в справочник\n'
              'read - для чтения справочника\n'
              'search - для поиска в справочнике\n'
              'change - для редактирования контактов\n'
              'delete - для удаления контакта\n'
              'stop - для завершения работы')
        mode = input()
        if mode == 'add':
            contact_add()
        elif mode == 'read':
            phonebook_read()
        elif mode == 'search':
            contact_search()
        elif mode == 'change':
            change_contact()
        elif mode == 'delete':
            delete_contact()
        elif mode == 'stop':
            break


if __name__ == '__main__': 
    main()
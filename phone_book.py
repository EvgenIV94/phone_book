
filename_work = "phone.txt"


def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phone.txt')

    while (choice!=7):
        if choice==1:
            print_result(phone_book)

        elif choice==2:
            last_name=input('Фамилия: ')
            print(find_by_lastname(phone_book,last_name))

        elif choice==3:
            number= input('Телефон: ')
            print(find_by_number(phone_book, number))

        elif choice==4:
            user_data = input("Введите Фамилию, Имя, Номер телефона и Описание пользователя через запятую: ")
            print(add_user(phone_book, user_data))
	    	
        elif choice==5:
            lastname=input('Фамилия пользователя для удаления: ')
            print(delete_by_lastname(phone_book,lastname))

        elif choice==6:
            # user_data=input('new data ')
            # add_user(phone_book,user_data)
            # write_txt('phonebook.txt',phone_book)
            break
        choice=show_menu()


def show_menu():
    print("\nВыберете необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Удалить пользователя\n"
          "6. Закончить работу")
    choice = int(input())
    return choice


def read_txt(filename): 
    phone_book=[]
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
           record = dict(zip(fields, line.split(',')))
        phone_book.append(record)	
    return phone_book


def write_txt(filename_work , phone_book):
    with open(filename_work,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')


# КНОПКИ
def print_result(phone_book):       # 1. Отобразить весь справочник
    data = open('phone.txt', 'r')
    for line in data:
        print(line)
    data.close()

def find_by_lastname(phone_book, last_name):        # 2. Поиск по фамилии
    for i in range(len(phone_book)):
        if phone_book[i]['Фамилия'] == last_name:
            return phone_book[i]
    return "Не найден"

def find_by_number(phone_book, number):         # 3. Поиск по номеру
    for i in range(len(phone_book)):
        if phone_book[i]['Телефон'] == number:
            return phone_book[i]
        return "Не найден"

def add_user(phone_book, user_data):      # 4. Добавляем пользователя
    with open('phone.txt', 'a') as data:
        data.writelines(f"\n{user_data}")

def delete_by_lastname(phone_book, last_name):      # 5. Удаление пользователя
    for i in range(len(phone_book)):
        if phone_book[i] == last_name:
            del(i) 
        return "Не найден"
        



work_with_phonebook()
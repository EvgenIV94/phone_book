# НЕЙРОНКА!!! 

import json
import os

class PhoneBook:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        return []

    def save_contacts(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.contacts, file, ensure_ascii=False, indent=4)

    def display_all(self):
        if not self.contacts:
            print("Справочник пуст.")
        else:
            for contact in self.contacts:
                print(f"Фамилия: {contact['surname']}, Имя: {contact['name']}, Телефон: {contact['phone']}")

    def find_by_surname(self, surname):
        results = [contact for contact in self.contacts if contact['surname'].lower() == surname.lower()]
        if results:
            for contact in results:
                print(f"Фамилия: {contact['surname']}, Имя: {contact['name']}, Телефон: {contact['phone']}")
        else:
            print("Абонент не найден.")

    def find_by_phone(self, phone):
        results = [contact for contact in self.contacts if contact['phone'] == phone]
        if results:
            for contact in results:
                print(f"Фамилия: {contact['surname']}, Имя: {contact['name']}, Телефон: {contact['phone']}")
        else:
            print("Абонент не найден.")

    def add_contact(self, surname, name, phone):
        self.contacts.append({'surname': surname, 'name': name, 'phone': phone})
        self.save_contacts()
        print("Абонент добавлен.")

    def delete_contact(self, phone):
        initial_length = len(self.contacts)
        self.contacts = [contact for contact in self.contacts if contact['phone'] != phone]
        if len(self.contacts) < initial_length:
            self.save_contacts()
            print("Абонент удален.")
        else:
            print("Абонент не найден.")

    def run(self):
        while True:
            print("\nВыберите действие:")
            print("1. Отобразить весь справочник")
            print("2. Найти абонента по фамилии")
            print("3. Найти абонента по номеру телефона")
            print("4. Добавить абонента в справочник")
            print("5. Удалить абонента")
            print("6. Закончить работу")

            choice = input("Введите номер действия: ")

            if choice == '1':
                self.display_all()
            elif choice == '2':
                surname = input("Введите фамилию: ")
                self.find_by_surname(surname)
            elif choice == '3':
                phone = input("Введите номер телефона: ")
                self.find_by_phone(phone)
            elif choice == '4':
                surname = input("Введите фамилию: ")
                name = input("Введите имя: ")
                phone = input("Введите номер телефона: ")
                self.add_contact(surname, name, phone)
            elif choice == '5':
                phone = input("Введите номер телефона абонента, которого хотите удалить: ")
                self.delete_contact(phone)
            elif choice == '6':
                print("Работа завершена.")
                break
            else:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    phone_book = PhoneBook()
    phone_book.run()
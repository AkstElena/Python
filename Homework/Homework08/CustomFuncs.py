import os


def show_contacts(file_name):
    os.system("CLS")
    with open(file_name, "r", encoding="utf-8") as file:
        data = file.readlines()

        for contact in data:
            print(contact, end="")

    input("\nНажмите любую клавишу")


def add_contact(file_name):
    os.system("CLS")
    with open(file_name, "a", encoding="utf-8") as file:
        res = ""
        res += input("Введите фамилию контакта: ") + " "
        res += input("Введите имя контакта: ") + " "
        res += input("Введите номер контакта: ") + " "

        file.write("\n" + res)

    input("Контакт добавлен. Нажмите любую клавишу")


def search_contact(file_name):
    os.system("CLS")
    target = input("Введите имя или фамилию для поиска номера телефона: ").lower()

    with open(file_name, "r", encoding="utf-8") as file:
        contacts = file.readlines()

        for contact in contacts:
            if target in contact.lower():
                print(contact)
                break
        else:
            print("Такого контакта нет")

    input("Нажмите любую клавишу")


def update_contact(file_name):
    os.system("CLS")
    target = input("Введите имя или фамилию для обновления контакта: ").lower()

    with open(file_name, "r", encoding="utf-8") as file:
        contacts = file.readlines()
        for item in list(enumerate(contacts)):
            if target in item[1].lower():
                print(f"Найден контакт: {item[1]}")
                res = input("Введите фамилию контакта для обновления: ") + " "
                res += input("Введите имя контакта для обновления: ") + " "
                res += input("Введите номер контакта для обновления: ")
                print(f"\nОбновленный контакт: {res}")
                contacts[item[0]] = res + "\n"
                with open(file_name, "w") as file:
                    file.writelines(contacts)
                break
        else:
            print("Такого контакта нет")
    input("Нажмите любую клавишу")


def delete_contact(file_name):
    os.system("CLS")
    target = input("Введите имя или фамилию для удаления контакта: ").lower()

    with open(file_name, "r", encoding="utf-8") as file:
        contacts = file.readlines()
        for item in list(enumerate(contacts)):
            if target in item[1].lower():
                print(f"Найден контакт: {item[1]}")
                pos = item[0]
                for i in range(pos, len(contacts) - 1):
                    contacts[i] = contacts[i + 1]
                contacts.pop()
                with open(file_name, "w") as file:
                    file.writelines(contacts)
                break
        else:
            print("Такого контакта нет")
    input("Контакт удален. Нажмите любую клавишу")


def drawing():
    print("1 - show contacts")
    print("2 - add contacts")
    print("3 - search contacts")
    print("4 - update contacts")
    print("5 - delete contacts")
    print("6 - exit")


def main(file_name):
    while True:
        os.system("CLS")
        drawing()
        user_choice = int(input("Введите число от 1 до 6: "))

        if user_choice == 1:
            show_contacts(file_name)
        elif user_choice == 2:
            add_contact(file_name)
        elif user_choice == 3:
            search_contact(file_name)
        elif user_choice == 4:
            update_contact(file_name)
        elif user_choice == 5:
            delete_contact(file_name)
        elif user_choice == 6:
            print("До свидания")
            return

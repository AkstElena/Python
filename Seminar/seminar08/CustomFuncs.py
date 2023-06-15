import os


def show_contacts(file_name):
    os.system("CLS")
    with open(file_name, "r") as file:
        data = file.readlines()

        for contact in data:
            print(contact, end="")

    input("\nНажмите любую клавишу")


def add_contact(file_name):
    os.system("CLS")
    with open(file_name, "a") as file:
        res = ""
        res += input("Введите фамилию контакта: ") + " "
        res += input("Введите имя контакта: ") + " "
        res += input("Введите номер контакта: ") + " "

        file.write("\n" + res)

    input("Контакт добавлен. Нажмите любую клавишу")


def search_contact(file_name):
    os.system("CLS")
    target = input("Введите имя или фамилию для поиска номера телефона: ")

    with open(file_name, "r") as file:
        contacts = file.readlines()

        for contact in contacts:
            if target in contact:
                print(contact)
                break
        else:
            print("Такого контакта нет")

    input("Нажмите любую клавишу")


def drawing():
    print("1 - show contacts")
    print("2 - add contacts")
    print("3 - search contacts")
    print("4 - exit")


def main(file_name):
    while True:
        os.system("CLS")
        drawing()
        user_choice = int(input("Введите число от 1 до 4: "))

        if user_choice == 1:
            show_contacts(file_name)
        elif user_choice == 2:
            add_contact(file_name)
        elif user_choice == 3:
            search_contact(file_name)
        elif user_choice == 4:
            print("До свидания")
            return

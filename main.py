import PySimpleGUI as sg
import json

def save_passwords(passwords, file_path):
    with open(file_path, "w") as file:
        json.dump(passwords, file)

def load_passwords(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def main():
    file_path = "passwords.json"  # Вы можете указать путь к файлу, который вы хотите использовать
    # Определение макета интерфейса
    layout = [
        [sg.Text("Сервис:"), sg.InputText(key='-SERVICE-')],
        [sg.Text("Логин:"), sg.InputText(key='-USERNAME-')],
        [sg.Text("Пароль:"), sg.InputText(key='-PASSWORD-')],
        [sg.Button("Добавить пароль"), sg.Button("Показать пароли")],
        [sg.Multiline("", size=(40, 10), key='-PASSWORD_LIST-')],
    ]

    # Создание окна
    window = sg.Window("Менеджер паролей", layout)

    passwords = load_passwords(file_path)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            save_passwords(passwords, file_path)
            break

        if event == "Добавить пароль":
            service = values['-SERVICE-']
            username = values['-USERNAME-']
            password = values['-PASSWORD-']
            if service and username and password:
                passwords.append({"service": service, "username": username, "password": password})
                sg.popup(f"Пароль для сервиса {service} добавлен.")
                window['-SERVICE-'].update('')
                window['-USERNAME-'].update('')
                window['-PASSWORD-'].update('')

        if event == "Показать пароли":
            if passwords:
                password_list = "\n".join([f"Сервис: {entry['service']}, Логин: {entry['username']}, Пароль: {entry['password']}" for entry in passwords])
                window['-PASSWORD_LIST-'].update(password_list)
            else:
                sg.popup("Список паролей пуст.")

    window.close()

if __name__ == "__main__":
    main()

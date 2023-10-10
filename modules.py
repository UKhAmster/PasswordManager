import json


def add_user_to_file(user_name, servies_name):
    with open('passwords.json', 'r', encoding='utf8') as file:
        servieses = json.load(file)
        safe_base = [i['servies_names'] for i in servieses]
        if servies_name not in safe_base:
            servieses['servies'].append(
                {
                    'firstname': user_name,
                    'id': user_id,
                    'status': 'low_user'
                }
            )
        with open('users.json', 'w', encoding='utf8') as outfile:
            json.dump(users, outfile, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    add_user_to_file('asdasdasd', 123123)
    add_user_to_file('asdasdasd', 123123)
    add_user_to_file('asd', 123)

def show_data():
    with open("data.txt", "r", encoding="utf-8") as fd:
        print(fd.read())


def add_data():
    fio = input("Введите ФИО:")
    tel = input("Введите номер телефона:")
    with open("data.txt", "a", encoding="utf-8") as f:
        f.write("\n{} | {}".format(fio, tel))


def find_data():
    data = input("какие данные ищем?:")
    with open("data.txt", "r", encoding="utf-8") as fd:
         all_data = fd.read()
    print("Результаты поиска:")
    print(search(all_data, data))


def search(a_data: list, data: str) -> str:
    a_data = a_data.split("\n")
    rez = "".join(i for i in a_data if data in i)
    return rez


def edit_data():
    with open("data.txt", "r", encoding="utf-8") as fd:
        all_data = fd.read()
        all_data = all_data.split("\n")
        for elem in list(enumerate(all_data)):
            print(f"{elem[0]} {elem[1]}")
        num_line = int(input("Какую строку хотите изменить?:"))
        all_data[num_line] = edited(all_data[num_line])
        print(all_data[num_line])
        rewrite_file("\n".join(all_data))


def rewrite_file(data: str):
    with open("data.txt", "w", encoding="utf-8") as fd:
        fd.write(data)


def edited(text: str) -> str:
    fio = input("Введите фамилию:")
    tel = input("Введите телефон:")
    if len(fio) == 0:
        fio = text.split(" | ")[0]
    if len(tel) == 0:
        tel = text.split(" | ")[1]
    return f"{fio} | {tel}"


def delete_data():
    with open("data.txt", "r", encoding="utf-8") as fd:
        all_data = fd.read()
        all_data = all_data.split("\n")
        for elem in list(enumerate(all_data)):
            print(f"{elem[0]} {elem[1]}")
        num_line = int(input("Какую строку хотите удалить?:"))
        print(f'удаление строки: {all_data[num_line]}')
        del all_data[num_line]
        rewrite_file("\n".join(all_data))

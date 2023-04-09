import functions

while True:
    print("1. показать, 2. добавить, 3. найти, 4. изменить, 5. удалить")
    mode = int(input())
    if mode == 1:
        functions.show_data()
    elif mode == 2:
        functions.add_data()
    elif mode == 3:
        functions.find_data()
    elif mode == 4:
        functions.edit_data()
    elif mode == 5:
        functions.delete_data()
    else:
        break

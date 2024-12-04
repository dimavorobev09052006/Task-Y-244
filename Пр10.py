# имя файла
FILENAME = "Воробьёв Дмитрий Алексеевич_У-244_Vvod.txt"
 
# запись строки в файл
def write():
    message = input("Введите строку: ")
    with open(FILENAME, "a") as file:
        file.write(message + "\n")
 
# чтение файла файл
def read():
    with open(FILENAME, "r") as file:
        for message in file:
            print(message, end="")
    print() # перевод строки для разделения меню и вывода
             
while(True):
    selection = int(input("1.Запись в файл\t\t2.Чтение файла\t\t3.Выход\nВыберите действие: "))
    match selection:
        case 1: write()
        case 2: read()
        case 3: break
        case _: print("Некорректный ввод")
     
print("Программа завершена")
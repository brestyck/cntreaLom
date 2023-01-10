import os, platform, sys

n = "\033[39m"
r = "\033[91m"
g = "\033[92m"
o = "\033[93m"
b = "\033[94m"
m = "\033[95m"

def cls():
    os.system("cls")
    if platform.system == "Linux":
        os.system("clear")

logo = r'''

    ▄█▄       ▄      ▄▄▄▄▀ █▄▄▄▄ ▄███▄   ██   █     ████▄ █▀▄▀█ 
    █▀ ▀▄      █  ▀▀▀ █    █  ▄▀ █▀   ▀  █ █  █     █   █ █ █ █ 
    █   ▀  ██   █     █    █▀▀▌  ██▄▄    █▄▄█ █     █   █ █ ▄ █ 
    █▄  ▄▀ █ █  █    █     █  █  █▄   ▄▀ █  █ ███▄  ▀████ █   █ 
    ▀███▀  █  █ █   ▀        █   ▀███▀      █     ▀          █     версия 1
        █   ██           ▀              █                ▀   
                                        ▀                           
'''

instructions = f'''
    Чтобы получить зачет в Цнтрее, Golom использует 2 файла.

    Если вы работаете на Python, выберите сначала пункт {g}Python (1 файл){n}
    Golom создаст файл {b}first.py{n}, который нужно загрузить на Цнтрею.

    Затем, выберите пункт {g}Python (2 файл){n} и в появившееся поле для ввода вставьте {o}детализацию результатов из Цнтреи{n}
    Golom создаст файл {b}exploit.py{n}, который нужно загрузить в то же задание в Цнтрее для получения зачета за задание.

    Абсолютно аналогично Golom работает для языка Golang.

    Приятного использования!
    Нажмите Enter, чтобы продолжить
'''

menu = f'''
    [{m}1{n}] Инструкция
    [{b}2{n}] Python (1 файл)  
    [{b}3{n}] Python (2 файл)
    [{b}4{n}] Golang (1 файл)
    [{b}5{n}] Golang (2 файл)
    [{r}6{n}] Выйти
'''

# EXPLOITS SOURCE CODE

init_py = "print(\"ilovecntrea\")"
init_go = '''
package main

import "fmt"

func main() {
    fmt.Println("ilovecntrea")
}
'''
# Compiling cntrea logs
def complile_logs(data, lang):
    data = data.replace("\"", "")
    data = data.split()
    compiled = []
    for i in range(len(data)):
        if data[i] == "Expected":
            print(f"[{g}*{n}] Compiled answer entity {b}{data[i+1]}{n}")
            compiled.append(data[i+1])
    compiled_string = ""
    for j in compiled:
        compiled_string += ("\""+j+"\",\n")
    if lang == "py":
        compiled_string = compiled_string[:-2]
    return compiled_string


while True:
    cls()
    print(o, logo, n)
    print(menu)
    command = input(">>> ")

    if command == "1":
        cls()
        print(r, logo, n)
        print(instructions)
        input()
    if command == "2":
        with open("first.py", "w") as first_file:
            first_file.write(init_py)
        cls()
        print(r, logo, n)
        print(o, "Первый файл был сохранен под именем first.py (Нажмите Enter, чтобы продолжить)", n)
        input()
    if command == "3":
        cls()
        print(r, logo, n)
        print(f"Вставьте {g}детализацию результатов{n} из Цнтреи (чтобы закончить ввод нажмите {r}Ctrl+Z{n} на Windows, или {r}Ctrl+D{n} на Linux) >>>")
        data = sys.stdin.read()
        compiled = complile_logs(data, "py")
    
        python_exploit = f'''
import os

answers = [
{compiled}
]


def read_attempt():
    with open("top_secret", "r") as h:
        return h.read()


def write_attempt(attempt):
    with open("top_secret", "w") as h:
        h.write(attempt)


if not os.path.exists("top_secret"):
    write_attempt("1")
    print(answers[0])
    exit()
else:
    i = int(read_attempt())
    write_attempt(str(i+1))
    print(answers[i])
    exit()
'''
        with open("exploit.py", "w") as exploit_file:
            exploit_file.write(python_exploit)
        cls()
        print(r, logo, n)
        print(o, "Главный файл был сохранен под именем exploit.py (Нажмите Enter, чтобы продолжить)", n)
        input()
    if command == "4":
        with open("first.go", "w") as first_file:
            first_file.write(init_go)
        cls()
        print(r, logo, n)
        print(o, "Первый файл был сохранен под именем first.go (Нажмите Enter, чтобы продолжить)", n)
        input()
    if command == "5":
        cls()
        print(r, logo, n)
        print(f"Вставьте {g}детализацию результатов{n} из Цнтреи (чтобы закончить ввод нажмите {r}Ctrl+Z{n} на Windows, или {r}Ctrl+D{n} на Linux) >>>")
        data = sys.stdin.read()
        compiled = complile_logs(data, "go")

        golang_exploit = '''
package main

import (
	"fmt"
	"os"
	"strconv"
)

func write_attempt(attempt int) {
	os.Mkdir(fmt.Sprint(attempt), os.ModeAppend)
}

func read_attempt() int {
	path, _ := os.Getwd()
	files, _ := os.ReadDir(path)
	maxima := -1
	for _, j := range files {
		if i, err := strconv.Atoi(j.Name()); err == nil {
			if i > maxima {
				maxima = i
			}
		}
	}
	return maxima
}

func main() {
	answers := []any{
		'''+compiled+'''
	}
	if read_attempt() == -1 {
		write_attempt(0)
		fmt.Println(answers[0])
	} else {
		x := read_attempt()
		if x >= len(answers)-1 {
			fmt.Println(answers[len(answers)-1])
		} else {
			write_attempt(x + 1)
			fmt.Println(answers[x+1])
		}
	}
}'''

        with open("exploit.go", "w") as exploit_file:
            exploit_file.write(golang_exploit)
        cls()
        print(r, logo, n)
        print(o, "Главный файл был сохранен под именем exploit.go (Нажмите Enter, чтобы продолжить)", n)
        input()
    if command == "6":
        cls()
        print(m, "Спасибо за использование!", n)
        exit()


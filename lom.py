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

    ▄████▄   ███▄    █ ▄▄▄█████▓ ██▀███  ▓█████ ▄▄▄       ██▓     ▒█████   ███▄ ▄███▓
    ▒██▀ ▀█   ██ ▀█   █ ▓  ██▒ ▓▒▓██ ▒ ██▒▓█   ▀▒████▄    ▓██▒    ▒██▒  ██▒▓██▒▀█▀ ██▒
    ▒▓█    ▄ ▓██  ▀█ ██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒███  ▒██  ▀█▄  ▒██░    ▒██░  ██▒▓██    ▓██░
    ▒▓▓▄ ▄██▒▓██▒  ▐▌██▒░ ▓██▓ ░ ▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██ ▒██░    ▒██   ██░▒██    ▒██ 
    ▒ ▓███▀ ░▒██░   ▓██░  ▒██▒ ░ ░██▓ ▒██▒░▒████▒▓█   ▓██▒░██████▒░ ████▓▒░▒██▒   ░██▒      версия 3.1 (обход блокировки)
    ░ ░▒ ▒  ░░ ▒░   ▒ ▒   ▒ ░░   ░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░   ░  ░
    ░  ▒   ░ ░░   ░ ▒░    ░      ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░░ ░ ▒  ░  ░ ▒ ▒░ ░  ░      ░
    ░           ░   ░ ░   ░        ░░   ░    ░    ░   ▒     ░ ░   ░ ░ ░ ▒  ░      ░   
    ░ ░               ░             ░        ░  ░     ░  ░    ░  ░    ░ ░         ░   
    ░                                                                                 

'''

instructions = f'''
    Чтобы получить зачет в Цнтрее, CntreaLom использует 2 файла.

    Если вы работаете на Python, выберите сначала пункт {g}Python (1 файл){n}
    CntreaLom создаст файл {b}first.py{n}, который нужно загрузить на Цнтрею.

    Затем, выберите пункт {g}Python (2 файл){n} и в появившееся поле для ввода вставьте {o}детализацию результатов из Цнтреи{n}
    CntreaLom создаст файл {b}exploit.py{n}, который нужно загрузить в то же задание в Цнтрее для получения зачета за задание.

    Абсолютно аналогично CntreaLom работает для языка Golang.

    Приятного использования!
    Нажмите Enter, чтобы продолжить
'''

menu = f'''
    [{m}1{n}] Инструкция
    [{b}2{n}] Python 1 файл
    [{b}3{n}] Python 2 файл
    [{b}4{n}] Golang 1 файл
    [{b}5{n}] Golang 2 файл
    [{o}6{n}] Golang (вывод пробелов)
    [{r}E{n}] Выйти
'''

# EXPLOITS SOURCE CODE
inits = {
    "py": "print(\"ilovecntrea\")",
    "go": '''
package main

import "fmt"

func main() {
    fmt.Println("ilovecntrea")
}
'''
}

def get_raw_exploit(answers_string, lang):
    exploits = {
# PYTHON Exploit Source ==============================
    "py": f'''
import os

answers = [
{answers_string}
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
''',
# GOLANG Exploit Source ==============================
"go": '''
package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
)

func write_attempt(attempt int) {
	fo, err := os.Create("datainfo")
	defer fo.Close()
	_, err = fo.Write([]byte(fmt.Sprint(attempt)))
	if err != nil {
		log.Fatal(err)
	}
}

func read_attempt() int {
	maxima := -1
	if _, err := os.Stat("datainfo"); err == nil {
		data, err := os.ReadFile("datainfo")
		maxima, err = strconv.Atoi(string(data))
		if err != nil {
			log.Fatal(err)
		}
	} else {
		os.Create("datainfo")
	}
	return maxima
}

func main() {
	answers := []any{
		'''+answers_string+'''
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
}
'''
}
    return exploits[lang]

# Compiling cntrea logs
def split_logs(data, keyword):
    data = data.replace("\"", "")
    data = data.split()
    compiled = []
    for i in range(len(data)):
        if data[i] == keyword:
            print(f"[{g}*{n}] Найден ответ: {b}{data[i+1]}{n}")
            compiled.append(data[i+1])
    return compiled

def compile_logs(data, lang):
    compiled = split_logs(data, "Expected")
    compiled_string = ""
    for j in compiled:
        compiled_string += ("\""+j+"\",\n")
    if lang == "py":
        compiled_string = compiled_string[:-2]
    print(f"[{m}+{n}] Нажмите {b}Enter{n}, чтобы продолжить")
    input()
    return compiled_string

# Whole actions
def default_exploit(lang):
    cls()
    print(r, logo, n)
    print(f"Вставьте {g}детализацию результатов{n} из Цнтреи (чтобы закончить ввод нажмите {r}Ctrl+Z{n} на Windows, или {r}Ctrl+D{n} на Linux) >>>")
    data = sys.stdin.read()
    compiled = compile_logs(data, lang)

    golang_exploit = get_raw_exploit(compiled, lang)

    with open(f"exploit.{lang}", "w") as exploit_file:
        exploit_file.write(golang_exploit)
    cls()
    print(r, logo, n)
    print(o, f"Главный файл был сохранен под именем exploit.{lang} (Нажмите Enter, чтобы продолжить)", n)
    input()

def create_initial_file(lang):
    with open(f"first.{lang}", "w") as first_file:
        first_file.write(inits[lang])
    cls()
    print(r, logo, n)
    print(o, f"Первый файл был сохранен под именем first.{lang} (Нажмите Enter, чтобы продолжить)", n)
    input()

# Main menu
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
        create_initial_file("py")
    if command == "3":
        default_exploit("py")
    if command == "4":
        create_initial_file("go")
    if command == "5":
        default_exploit("go")
    if command == "6":
        cls()
        print(o, logo, n)
        print("")
        input()
    if command.lower() == "e":
        cls()
        print(m, "Спасибо за использование!", n)
        exit()

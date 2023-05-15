def start():

    print("Enter a bracket expression:")
    input_str = input()
    input_str += '#'
    i = 0
    sym = 'a'
    return input_str, sym, i

letters = "abcdefghijklmnopqrstuvwxyz"
signs = "+-/*"


def Letter(sym):
    if sym in letters:
        return 1
    else:
        return 0


def Sign(sym):
    if sym in signs:
        return 1
    else:
        return 0

class ParseError(Exception):
    def __init__(self):
        print('error')


def error():
    raise ParseError()


def read():
    global sym, i
    i += 1
    sym = input_str[i]


class MainClass():

    #Формула
    def formula(self):
        self.expression_0()
        if (sym == '#'):
            return
        error()


    #Выражение
    def expression_0(self):
        if (sym == '('):
            self.expression_round_0()
        elif (sym == '['):
            self.expression_square_0()
        elif Letter(sym):
            self.alphabet_0()

    #Выражение в круглых скобках 0
    def expression_round_0(self):
        if (sym == '('):
            read()
            self.expression_2()
            if (sym == ')'):
                read()
            else:
                print("Скобка не закрыта")
                error()
            self.expression_round_1()

    # Выражение в круглых скобках 1
    def expression_round_1(self):
        if Sign(sym):
            read()
            self.expression_round_2()
        elif (sym == '[') or Letter(sym):
            self.expression_round_2()


    # Выражение в круглых скобках 2
    def expression_round_2(self):
        if (sym == '['):
            self.expression_square_0()
        elif Letter(sym):
            self.alphabet_0()
        else:
            error()


    def alphabet_0(self):
        read()
        self.alphabet_1()


    def alphabet_1(self):
        if Sign(sym):
            read()
            self.expression_0()
        elif (sym == '(') or (sym == '[') or Letter(sym):
            self.expression_0()


    def alphabet_2(self):
        read()
        self.alphabet_3()


    def alphabet_3(self):
        if Sign(sym):
            read()
            self.expression_0()
        elif (sym == '(') or (sym == '[') or Letter(sym):
            self.expression_0()
        else: error()


    def expression_2(self):
        if (sym == '('):
            self.expression_round_0()
        elif (sym == '['):
            self.expression_square_0()
        elif Letter(sym):
            self.alphabet_2()
        else:
            error()


    # Выражение в квадратных скобках
    def expression_square_0(self):
        if (sym == '['):
            read()
            self.expression_2()
            if (sym == ']'):
                read()
            else:
                print("Скобка не закрыта")
                error()
            self.expression_square_1()


    # Выражение в квадратных скобках
    def expression_square_1(self):
        if Sign(sym):
            read()
            self.expression_square_2()
        elif (sym == '(') or Letter(sym):
            self.expression_square_2()


    # Выражение в квадратных скобках
    def expression_square_2(self):
        if (sym == '('):
            self.expression_round_0()
        elif Letter(sym):
            self.alphabet_0()
        else:
            error()


def main():
    global sym
    sym = input_str[0]
    m = MainClass()
    try:
        m.formula()
    except ParseError:
        print('false')
        return
    print('true')

print("Условие задания:")
print(" Правильная скобочная запись арифметических выражений с двумя видами скобок. ", " \n",
      "После круглой скобки всегда должна стоять квадратная, после квадратной - круглая. ", " \n",
      "Знак умножения не пишется и обозначается отсутствием знака. ", " \n",
      "Могут быть “лишние” скобки, но одна буква не может браться в скобки.")
print("Правильная запись: [ab((d+cd)[[a-b]])]/((a+b-c)[(c+d)])")
print("Неправильная запись [(a*c+b)([c-(d)]/([a+b-c](b-c)(d/e)))]")
print("В программе можно ввести с клавиатуры, можно выбрать из предложенных")
print("Для ввода с клавиатуры используется английская раскладка на первые четыре буквы алфавита a, b, c, d, "
      "два вида скобок (), [], символы /, +, -.")
print("\n")

print("if you want to start, enter 1")
print("if you want to exit, enter 2")
a2 = int(input())
while a2 != 2:
    if (a2 == 1):
        print("enter your example - 2")
        print("use the suggested example - 3")
        a1 = int(input())
        if (a1 == 2):
            input_str, sym, i = start()
            main()
        elif(a1 == 3):
            print("choose any of the examples below")
            print("№1 - [ab((d+cd)[[a-b]])]/((a+b-c)[(c+d)])")
            print("№2 - [(a*c+b)([c-(d)]/([a+b-c](b-c)(d/e)))]")
            print("№3 - ([a-bc](a+c))[b/c]-(ac)")
            print("№4 - [a(b[c(a+b)[a-c]])/b]")
            print("№5 - [((a/b))+c](b-c)")
            print("№6 - (abc+ab(b-c))[b-c]")
            print("№7 - [b/c-a/b](a(b+c))")
            print("№8 - [a-b][a-c](a+b)")
            print("№9 - [a*b]*(a/c)")
            print("№10 - (a)+[b-c]")
            print("№11 - [[a*c]+b(b-c)][a-c]")
            print("№12 - (((((a+b))))*c)(a-b)")
            a = int(input())
            if(0<a<13):
                if(a == 1):
                    input_str = "[ab((d+cd)[[a-b]])]/((a+b-c)[(c+d)])#"
                elif (a == 2):
                    input_str = "[(a*c+b)([c-(d)]/([a+b-c](b-c)(d/e)))]#"
                elif (a == 3):
                    input_str = "([a-bc](a+c))[b/c]-(ac)#"
                elif (a == 4):
                    input_str = "[a(b[c(a+b)[a-c]])/b]#"
                elif (a == 5):
                    input_str = "[((a/b))+c](b-c)#"
                elif (a == 6):
                    input_str = "(abc+ab(b-c))[b-c]#"
                elif (a == 7):
                    input_str = "[b/c-a/b](a(b+c))#"
                elif (a == 8):
                    input_str = "[a-b][a-c](a+b)#"
                elif (a == 9):
                    input_str = "[a*b]*(a/c)#"
                elif (a == 10):
                    input_str = "(a)+[b-c]#"
                elif (a == 11):
                    input_str = "[[a*c]+b(b-c)][a-c]#"
                elif (a == 12):
                    input_str = "(((((a+b))))*c)(a-b)#"
                i = 0
                sym = 'a'
                main()
            else:
                print("Введённого примера нет")

        print("if you want to continue, enter 1")
        print("if you want to exit, enter 2")
        a2 = int(input())
        if (a2 != 1):
            a2 = 2
print("bye")

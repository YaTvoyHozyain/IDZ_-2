def start():

    print("Enter a bracket expression:")
    input_str = input()
    input_str += '#'
    i = 0
    sym = 'a'
    return input_str, sym, i


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
        self.expression()
        if (sym == '#'):
            return
        error()


    #Выражение
    def expression(self):
        if (sym == '('):
            self.expression_round()
        elif (sym == '['):
            self.expression_square()
        elif (sym == 'a') or (sym == 'b') or (sym == 'c') or (sym == 'd'):
            self.alphabet()
        elif (sym == '+') or (sym == '-') or (sym == '/'):
            self.signs()


    #Выражение в круглых скобках
    def expression_round(self):
        if (sym == '('):
            read()
            if (sym == 'a') or (sym == 'b') or (sym == 'c') or (sym == 'd'):
                read()
                if (sym == ')'):
                    print("Буква в скобках")
                    error()
            self.expression()
            if (sym == ')'):
                read()
                if (sym == '('):
                    print("Нарушено правило чередования скобок")
                    error()
            elif (sym == '*'):
                print("Недопустимый символ")
                error()
            else:
                print("Скобка не закрыта")
                error()
            self.expression()


    # Выражение в квадратных скобках
    def expression_square(self):
        if (sym == '['):
            read()
            if (sym == 'a') or (sym == 'b') or (sym == 'c') or (sym == 'd'):
                read()
                if (sym == ']'):
                    print("Буква в скобках")
                    error()
            self.expression()
            if (sym == ']'):
                read()
                if (sym == '['):
                    print("Нарушено правило чередования скобок")
                    error()
            elif (sym == '*'):
                print("Недопустимый символ")
                error()
            else:
                print("Скобка не закрыта")
                error()
            self.expression()


    # Алфавит
    def alphabet(self):
        if (sym == 'a') or (sym == 'b') or (sym == 'c') or (sym == 'd'):
            read()
            self.expression()

    # Знаки
    def signs(self):
        if (sym == '+') or (sym == '-') or (sym == '/'):
            read()
            self.expression()


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

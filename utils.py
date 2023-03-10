import ast


def begin():
    string = input("Enter your code : ")
    string_list = string.split()
    parse_0(string_list[0:])


def verify_syntax(code):
    try:
        tree = ast.parse(code)
        return True
    except SyntaxError:
        return False


def check(string_list):
    if string_list[0].startswith(":"):
        return 1
    else:
        return 0


def get_condition(string_list):
    s = 0
    string = ''
    for s in range(len(string_list)):
        if string_list[s].endswith(':'):
            string = string + string_list[s][:-1]
            break
        string = string + string_list[s] + " "
    if not string_list[s].endswith(':'):
        if check(string_list[s:]):
            print("Need space after : ")
            exit(0)
        else:
            print('Need : after condition')
            exit(0)
    if string == '' or not string:
        print('Empty condition')
        exit(0)
    return string


def get_body(string_list):
    if len(string_list) == 0:
        print("Empty Body")
        exit(0)
    else:
        s = 0
        string = ""
        for s in range(len(string_list)):
            if string_list[s].startswith("else") or string_list[s].startswith("elif"):
                break
            string = string + string_list[s] + " "
    if string == '' or not string:
        print('Empty Body')
        exit(0)
    return string


def parse_0(string_list):
    if len(string_list) == 0:
        print("Write a condition")
        exit(0)
    else:
        if string_list[0] == "if":
            parse_1(string_list[1:])
        else:
            print("Code must start with if")
            exit(0)


def parse_1(string_list):
    if len(string_list) == 0:
        print('Complete your condition!')
        exit(0)
    else:
        string = get_condition(string_list)
        if not verify_syntax(string):
            print('Bad if condition!')
            exit(0)
        s = 0
        for s in range(len(string_list)):
            if string_list[s].endswith(':'):
                break
        parse_2(string_list[s + 1:])


def parse_2(string_list):
    if len(string_list) == 0 or string_list[0].startswith('else') or string_list[0].startswith('elif'):
        print('Empty body of if')
        exit(0)
    else:
        string = get_body(string_list)
        if not verify_syntax(string):
            print('Error body syntax')
            exit(0)
        else:
            s = 0
            for s in range(len(string_list)):
                if string_list[s].startswith("else") or string_list[s].startswith("elif"):
                    s = s - 1
                    break
            parse_3(string_list[s + 1:])


def parse_3(string_list):
    if len(string_list) == 0:
        print('Good condition')
        exit(0)
    else:
        parse_4(string_list)


def parse_4(string_list):
    if string_list[0] == 'else':
        parse_5(string_list[1:])
    elif string_list[0] == "else:":
        parse_5_1(string_list[1:])
    elif string_list[0] == 'elif':
        parse_7(string_list[1:])
    elif string_list[0].startswith('elif') and not string_list[0].endswith('elif'):
        print("Error, 'elif' should be followed by a space")
        exit(0)
    elif string_list[0].startswith('else') and not string_list[0].endswith('else'):
        print("Error, 'else' should be followed by a space")
        exit(0)


def parse_5(string_list):
    if len(string_list) == 0:
        print("Need : after else")
        exit(0)
    elif string_list[0].startswith(":"):
        parse_6(string_list[1:])
    else:
        print("Can't put a condition after else")
        exit(0)


def parse_5_1(string_list):
    if len(string_list) == 0:
        print("Empty body of else")
        exit(0)
    else:
        parse_6(string_list[0:])


def parse_6(string_list):
    if len(string_list) == 0:
        print('Complete your else')
        exit(0)
    else:
        string = get_body(string_list)
        if not verify_syntax(string):
            print('Error body syntax')
            exit(0)
        else:
            print('Good condition')
            exit(0)


def parse_7(string_list):
    if len(string_list) == 0:
        print("Complete your condition!")
        exit(0)
    else:
        string = get_condition(string_list)
        if not verify_syntax(string):
            print('Bad elif condition!')
            exit(0)
        else:
            s = 0
            for s in range(len(string_list)):
                if string_list[s].endswith(':'):
                    break
            parse_8(string_list[s + 1:])


def parse_8(string_list):
    if len(string_list) == 0 or string_list[0].startswith('else') or string_list[0].endswith('elif'):
        print("Empty body of elif")
        exit(0)
    else:
        string = get_body(string_list)
        if not verify_syntax(string):
            print("Error body syntax")
            exit(0)
        else:
            s = 0
            for s in range(len(string_list)):
                if string_list[s].startswith('else') or string_list[s].startswith("elif"):
                    s = s - 1
                    break
            parse_3(string_list[s + 1:])


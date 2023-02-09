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


def get_condition(string_list):
    if len(string_list) == 0:
        return 0
    else:
        s = 0
        string = ''
        for s in range(len(string_list)):
            if string_list[s].endswith(':') or string_list[s] == ':':
                if string_list[s].endswith(':'):
                    string = string + string_list[s][:-1]
                break
            string = string + string_list[s]
        if not string_list[s].endswith(':'):
            print('Need : after if')
            exit(0)
    if string == '':
        print('Empty condition')
        exit(0)
    return string


def get_body(string_list):
    if len(string_list) == 0:
        return 0
    else:
        s = 0
        string = ""
        for s in range(len(string_list)):
            if string_list[s].startswith("else") or string_list[s].startswith("elif"):
                break
            string = string + string_list[s]
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
        s = 0
        for s in range(len(string_list)):
            if string_list[s].endswith(':') or string_list[s] == ':':
                break
        if not verify_syntax(string):
            print('Bad if condition!')
            exit(0)
        parse_2(string_list[s + 1:])


def parse_2(string_list):
    if len(string_list) == 0 or string_list[0].startswith('else'):
        print('Empty body of if')
        exit(0)
    else:
        string = get_body(string_list)
        if not verify_syntax(string):
            print('Error body syntax')
            exit(0)
        else:
            parse_3(string_list[1:])


def parse_3(string_list):
    if len(string_list) == 0:
        print('Good condition')
        exit(0)
    else:
        parse_4(string_list)


def parse_4(string_list):
    if string_list[0].startswith('else'):
        parse_5(string_list[0:])
    elif string_list[0] == 'elif':
        parse_7(string_list[1:])


def parse_5(string_list):
    if len(string_list) == 0 or not string_list[0].endswith(':'):
        print('Need : after else')
    else:
        s = 0
        for s in range(len(string_list)):
            if string_list[s].endswith(':') or string_list[s] == ':':
                break
        parse_6(string_list[s + 1:])


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
            parse_3(string_list[1:])


def parse_7(string_list):
    if len(string_list) == 0:
        print("Complete your condition!")
        exit(0)
    else:
        string = get_condition(string_list)
        s = 0
        for s in range(len(string_list)):
            if string_list[s].endswith(":") or string_list[s] == ':':
                break
        if not verify_syntax(string):
            print('Bad if condition!')
            exit(0)
        parse_8(string_list[s + 1:])


def parse_8(string_list):
    if len(string_list) == 0 or string_list[0].startswith('else'):
        print("Empty body of elif")
        exit(0)
    else:
        string = get_body(string_list)
        if not verify_syntax(string):
            print('Error body syntax')
            exit(0)
        else:
            parse_3(string_list[1:])


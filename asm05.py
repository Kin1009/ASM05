import sys
import getpass
#Functions:
#lti reg, value            set reg <reg> to <value> (int)
#lts reg, value            set reg <reg> to  <value> (str)
#otr reg                   print reg <reg>
#ots hex                   print <hex> converted to string
#in reg                    set input to <reg> (let <reg> input)
#add regA, regB, regDist   add <regA> to <regB>, set result to <regDist> (let <regDist> result)
#sub regA, regB, regDist   sub <regA> to <regB>, set result to <regDist> (let <regDist> result)
#mul regA, regB, regDist   mul <regA> to <regB>, set result to <regDist> (let <regDist> result)
#div regA, regB, regDist   div <regA> to <regB>, set result to <regDist> (let <regDist> result)
#exp regA, regB, regDist   exp <regA> to <regB>, set result to <regDist> (let <regDist> result)
#and regA, regB, regDist   and <regA> and <regB>, set result to <regDist> (let <regDist> result)
#not regA, regDist         not <regA>, set result to <regDist> (let <regDist> result)
#nnd regA, regB, regDist   nand <regA> and <regB>, set result to <regDist> (let <regDist> result)
#or regA, regB, regDist    or <regA> and <regB>, set result to <regDist> (let <regDist> result)
#nor regA, regB, regDist   nor <regA> and <regB>, set result to <regDist> (let <regDist> result)
#xor regA, regB, regDist   xor <regA> and <regB>, set result to <regDist> (let <regDist> result)
#equ regA, regB, regDist   if <regA> == <regB>, set 1 to <regDist> (let <regDist> 1) else 0
#grt regA, regB, regDist   if <regA> > <regB>, set 1 to <regDist> (let <regDist> 1) else 0
#Lss regA, regB, regDist   if <regA> < <regB>, set 1 to <regDist> (let <regDist> 1) else 0
#jmp line                  jump to line <line>
#jif line, reg             jump to line <line> if <reg> == 1
#opn <reg>                 open reg <reg>
#bol regA, regDist         turn regA to boolean
#inc reg
#dec reg
def run(code=str, stopwhenerror=int|None, processcompletedialog=int|None):
    if not stopwhenerror:
        stopwhenerror = 1
    if type(processcompletedialog) != int:
        processcompletedialog = 1
    def error(type):
        error = ""
        match type:
            case "0": #regerror
                error = "RegError: "
            case "1":
                error = "TypeError: "
            case "2":
                error = "FuncError: "
            case "3":
                error = "ParamError: "
        error += "at line " + str(counter) + ", code: " + code[counter]
        print(error)
        if stopwhenerror == 1:
            sys.exit()
    RE = "0"
    TE = "1"
    FE = "2"
    PE = "3"
    counter = 0
    vars = {}
    hextable = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
    code = code.split("\n")
    while counter < len(code):
        command = code[counter]
        command = command.split(" ")
        if len(command):
            try:
                match command[0]:
                    case "var":
                        vars[command[1]] = "0"
                    case "sti":
                        if command[1] in vars:
                            int(command[2])
                            vars[command[1]] = command[2]
                        else:
                            error(RE)
                            if stopwhenerror == 0: break
                    case "sts":
                        string = command[2]
                        res = ""
                        for i in range(0, len(string), 2):
                            res += chr(hextable[string[i]] * 16 + hextable[string[i + 1]])
                        if command[1] in vars:
                            vars[command[1]] = res
                        else:
                            error(RE)
                            if stopwhenerror == 0: break
                    case "otv":
                        if command[1] in vars:
                            print(vars[command[1]])
                        else:
                            error(RE)
                            if stopwhenerror == 0: break
                    case "ots":
                        string = command[1]
                        res = ""
                        for i in range(0, len(string), 2):
                            try:
                                res += chr(hextable[string[i - 1]] * 16 + hextable[string[i]])
                            except:
                                error(TE)
                                if stopwhenerror == 0: break
                        print(res)
                    case "in":
                        if command[1] in vars:
                            vars[command[1]] = input(">>> ")
                        else:
                            error(RE)
                            if stopwhenerror == 0: break
                    case "apn":
                        command[1], command[2], command[3]
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        vars[command[3]] = vars[command[1]] + vars[command[2]]
                    case "add":
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE) 
                            if stopwhenerror == 0: break
                        try:
                            a, b = float(vars[command[1]]), float(vars[command[2]])
                            vars[command[3]] = str(a + b if (a + b) % 1 > 0 else int(a + b))
                        except:
                            error(TE)
                            if stopwhenerror == 0: break
                    case "sub":
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE) 
                            if stopwhenerror == 0: break
                        try:
                            a, b = float(vars[command[1]]), float(vars[command[2]])
                            vars[command[3]] = str(a - b if (a - b) % 1 > 0 else int(a - b))
                        except:
                            error(TE)
                            if stopwhenerror == 0: break
                    case "mul":
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        try:
                            a, b = float(vars[command[1]]), float(vars[command[2]])
                            vars[command[3]] = str(a * b if (a * b) % 1 > 0 else int(a * b))
                        except:
                            error(TE)
                            if stopwhenerror == 0: break
                    case "div":
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE) 
                            if stopwhenerror == 0: break
                        try:
                            a, b = float(vars[command[1]]), float(vars[command[2]])
                            vars[command[3]] = str(a / b if (a / b) % 1 > 0 else int(a / b))
                        except:
                            error(TE)
                            if stopwhenerror == 0: break
                    case "exp":
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break 
                        try:
                            a, b = float(vars[command[1]]), float(vars[command[2]])
                            vars[command[3]] = str(a ** b if (a ** b) % 1 > 0 else int(a ** b))
                        except:
                            error(TE)
                            if stopwhenerror == 0: break
                    case "bol":
                        try:
                            command[1], command[2]
                        except:
                            error(PE)
                            if stopwhenerror == 0: break
                        try:
                            a = bool(vars[command[1]])
                            vars[command[2]] = str(int(a))
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                    case "and":
                        try:
                            command[1], command[2], command[3]
                        except:
                            error(PE)
                            if stopwhenerror == 0: break
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        a, b = bool(vars[command[1]]), bool(vars[command[2]])
                        vars[command[3]] = str(int(a & b))
                    case "not":
                        try:
                            command[1], command[2]
                        except:
                            error(PE)
                            if stopwhenerror == 0: break
                        try:
                            vars[command[1]], vars[command[2]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        a = bool(vars[command[1]])
                        vars[command[2]] = str(int(not a))
                    case "nnd":
                        try:
                            command[1], command[2], command[3]
                        except:
                            error(PE)
                            if stopwhenerror == 0: break
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        a, b = bool(vars[command[1]]), bool(vars[command[2]])
                        vars[command[3]] = str(int(not (a & b)))
                    case "or":
                        try:
                            command[1], command[2], command[3]
                        except:
                            error(PE)
                            if stopwhenerror == 0: break
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        a, b = bool(vars[command[1]]), bool(vars[command[2]])
                        vars[command[3]] = str(int(a or b))
                    case "nor":
                        try:
                            command[1], command[2], command[3]
                        except:
                            error(PE)
                            if stopwhenerror == 0: break
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        a, b = bool(vars[command[1]]), bool(vars[command[2]])
                        vars[command[3]] = str(int(not (a or b)))
                    case "xor":
                        try:
                            command[1], command[2], command[3]
                        except:
                            error(PE)
                            if stopwhenerror == 0: break
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        a, b = bool(vars[command[1]]), bool(vars[command[2]])
                        vars[command[3]] = str(int(a ^ b))
                    case "equ":
                        try:
                            command[1], command[2], command[3]
                        except:
                            error(PE)
                            if stopwhenerror == 0: break
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        a, b = vars[command[1]], vars[command[2]]
                        vars[command[3]] = str(int(a == b))
                    case "grt":
                        try:
                            command[1], command[2], command[3]
                        except:
                            error(PE)
                            if stopwhenerror == 0: break
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        a, b = bool(vars[command[1]]), bool(vars[command[2]])
                        vars[command[3]] = str(int(a > b))
                    case "lss":
                        try:
                            command[1], command[2], command[3]
                        except:
                            error(PE)
                            if stopwhenerror == 0: break
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        a, b = bool(vars[command[1]]), bool(vars[command[2]])
                        vars[command[3]] = str(int(a < b))
                    case "jmp":
                        counter = int(command[1]) - 1
                    case "jif":
                        try:
                            vars[command[2]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        if vars[command[2]] == "1":
                            counter = int(command[1]) - 1
                    case "inc":
                        try:
                            vars[command[1]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        _ = vars[command[1]]
                        _ = float(_)
                        _ += 1
                        vars[command[1]] = str(_ if _ % 1 > 0 else int(_))
                    case "dec":
                        try:
                            vars[command[1]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        _ = vars[command[1]]
                        _ = float(_)
                        _ -= 1
                        vars[command[1]] = str(_ if _ % 1 > 0 else int(_))
                    case "mod":
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                            res = int(vars[command[1]]) % int(vars[command[2]])
                            vars[command[3]] = str(res)
                        except KeyError:
                            error(RE)
                        except TypeError:
                            error(TE)
                    case "flr":
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                            res = int(vars[command[1]]) // int(vars[command[2]])
                            vars[command[3]] = str(res)
                        except KeyError:
                            error(RE)
                        except TypeError:
                            error(TE)
                    case ";":
                        pass
            except:
                error(PE)
                if stopwhenerror == 0: break
            if command[0] not in ("sti", "sts", "otv", "ots", "in", "var", "apn", "add", "sub", "bol", "inc", "dec", "mul", "div", "exp", "equ", "grt", "lss", "jmp", "jif", "and", "not", "nnd", "or", "nor", "xor", ";", "mod", "flr", ""):
                error(FE)
                if stopwhenerror == 0: break
        counter += 1
    if stopwhenerror == 1 and processcompletedialog == 1:
        getpass.getpass("Press ENTER to close the window.")
        exit(0)
if __name__ == "__main__":
    args = sys.argv
    path = ""
    c = ""
    if len(args) > 1:
        path = args[1]
        c = open(path, "r").read()
        run(c, 1)
    else:
        print("ASM0.5 [Version 1.2]\nType \"help\" for help.\nThis is depecrated. Download from https://github.com/Kin1009/miniterm")
        while True:
            c = ""
            while True:
                inp = input("> ")
                match inp:
                    case "run":
                        run(c[:-1], 0)
                        break
                    case "exit":
                        exit(0)
                    case "help":
                        print("""
    ASM05 help:
    1. Functions:
    sti reg, value            set reg <reg> to <value> (int)
    sts reg, value            set reg <reg> to <value> (str) (hex)
    otv reg                   print reg <reg>
    ots hex                   print <hex> converted to string
    in reg                    set input to <reg> (let <reg> input)
    add regA, regB, regDist   add <regA> to <regB>, set result to <regDist>
    sub regA, regB, regDist   sub <regA> to <regB>, set result to <regDist>
    mul regA, regB, regDist   mul <regA> to <regB>, set result to <regDist>
    div regA, regB, regDist   div <regA> to <regB>, set result to <regDist>
    exp regA, regB, regDist   exp <regA> to <regB>, set result to <regDist>
    and regA, regB, regDist   and <regA> and <regB>, set result to <regDist>
    not regA, regDist         not <regA>, set result to <regDist>
    nnd regA, regB, regDist   nand <regA> and <regB>, set result to <regDist>
    or regA, regB, regDist    or <regA> and <regB>, set result to <regDist>
    nor regA, regB, regDist   nor <regA> and <regB>, set result to <regDist>
    xor regA, regB, regDist   xor <regA> and <regB>, set result to <regDist>
    equ regA, regB, regDist   if <regA> == <regB>, set 1 to <regDist> else 0
    grt regA, regB, regDist   if <regA> > <regB>, set 1 to <regDist> else 0
    lss regA, regB, regDist   if <regA> < <regB>, set 1 to <regDist> else 0
    jmp line                  jump to line <line>
    jif line, reg             jump to line <line> if <reg> == 1
    var <reg>                 make reg <reg>
    bol reg, regDist          turn <reg> to boolean, set result to <regDist> 
    apn regA regB regDist     <regDist> = <regA> + <regB>
    inc reg                   <reg> += 1
    dec reg                   <reg> -= 1
    mod regA regB regDist     <regA> % <regB> -> <regDist>
    flr regA regB regDist     <regA> % <regB> -> <regDist>
    ;                         comment

    2. Errors:
    RE         RegError (access a reg that doesn't exist)
    TE         TypeError (not the type it expected)
    FE         FuncError (invalid func)
    PE         ParamError (invalid params) 

    3. Console commands:
    run        run code
    exit       exit
    help       help""")
                    case _:
                        c += inp + "\n"
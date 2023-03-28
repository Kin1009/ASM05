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
def run(code, y):
    def error(type):
        error = ""
        if type == "0": #regerror
            error = "RegError: "
        elif type == "1":
            error = "TypeError: "
        elif type == "2":
            error = "FuncError: "
        elif type == "3":
            error = "ParamError: "
        error += "at line " + str(counter) + ", code: " + code[counter]
        if y == 1:
            sys.exit()
    RE = "0"
    TE = "1"
    FE = "2"
    PE = "3"
    counter = 0
    registers = {}
    hextable = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
    code = code.split("\n")
    while counter < len(code):
        command = code[counter]
        command = command.split(" ")
        if len(command) > 1:
            try:
                match command[0]:
                    case "var":
                        registers[command[1]] = "0"
                    case "sti":
                        if command[1] in registers:
                            int(command[2])
                            registers[command[1]] = command[2]
                        else:
                            error(RE)
                    case "sts":
                        string = command[2]
                        res = ""
                        for i in range(0, len(string), 2):
                            res += chr(hextable[string[i]] * 16 + hextable[string[i + 1]])
                        if command[1] in registers:
                            registers[command[1]] = res
                        else:
                            error(RE)
                    case "otv":
                        if command[1] in registers:
                            print(registers[command[1]])
                        else:
                            error(RE)
                    case "ots":
                        string = command[1]
                        res = ""
                        for i in range(0, len(string), 2):
                            try:
                                res += chr(hextable[string[i - 1]] * 16 + hextable[string[i]])
                            except:
                                error(TE)
                        print(res)
                    case "in":
                        if command[1] in registers:
                            registers[command[1]] = input(">>> ")
                        else:
                            error(RE)
                    case "apn":
                        command[1], command[2], command[3]
                        try:
                            registers[command[1]], registers[command[2]], registers[command[3]]
                        except:
                            error(RE)
                        registers[command[3]] = registers[command[1]] + registers[command[2]]
                    case "add":
                        try:
                            registers[command[1]], registers[command[2]], registers[command[3]]
                        except:
                            error(RE) 
                        try:
                            a, b = float(registers[command[1]]), float(registers[command[2]])
                            registers[command[3]] = str(a + b if (a + b) % 1 > 0 else int(a + b))
                        except:
                            error(TE)
                    case "sub":
                        try:
                            registers[command[1]], registers[command[2]], registers[command[3]]
                        except:
                            error(RE) 
                        try:
                            a, b = float(registers[command[1]]), float(registers[command[2]])
                            registers[command[3]] = str(a - b if (a - b) % 1 > 0 else int(a - b))
                        except:
                            error(TE)
                    case "mul":
                        try:
                            registers[command[1]], registers[command[2]], registers[command[3]]
                        except:
                            error(RE) 
                        try:
                            a, b = float(registers[command[1]]), float(registers[command[2]])
                            registers[command[3]] = str(a * b if (a * b) % 1 > 0 else int(a * b))
                        except:
                            error(TE)
                    case "div":
                        try:
                            registers[command[1]], registers[command[2]], registers[command[3]]
                        except:
                            error(RE) 
                        try:
                            a, b = float(registers[command[1]]), float(registers[command[2]])
                            registers[command[3]] = str(a / b if (a / b) % 1 > 0 else int(a / b))
                        except:
                            error(TE)
                    case "exp":
                        try:
                            registers[command[1]], registers[command[2]], registers[command[3]]
                        except:
                            error(RE) 
                        try:
                            a, b = float(registers[command[1]]), float(registers[command[2]])
                            registers[command[3]] = str(a ** b if (a ** b) % 1 > 0 else int(a ** b))
                        except:
                            error(TE)
                    case "bol":
                        try:
                            command[1], command[2]
                        except:
                            error(PE)
                        try:
                            a = bool(registers[command[1]])
                            registers[command[2]] = str(int(a))
                        except:
                            error(RE)
                    case "and":
                        try:
                            command[1], command[2], command[3]
                        except:
                            error(PE)
                        try:
                            registers[command[1]], registers[command[2]], registers[command[3]]
                        except:
                            error(RE)
                        a, b = bool(registers[command[1]]), bool(registers[command[2]])
                        registers[command[3]] = str(int(a & b))
                    case "not":
                        try:
                            command[1], command[2]
                        except:
                            error(PE)
                        try:
                            registers[command[1]], registers[command[2]]
                        except:
                            error(RE)
                        a = bool(registers[command[1]])
                        registers[command[2]] = str(int(not a))
                    case "nnd":
                        try:
                            command[1], command[2], command[3]
                        except:
                            error(PE)
                        try:
                            registers[command[1]], registers[command[2]], registers[command[3]]
                        except:
                            error(RE)
                        a, b = bool(registers[command[1]]), bool(registers[command[2]])
                        registers[command[3]] = str(int(not (a & b)))
                    case "or":
                        try:
                            command[1], command[2], command[3]
                        except:
                            error(PE)
                        try:
                            registers[command[1]], registers[command[2]], registers[command[3]]
                        except:
                            error(RE)
                        a, b = bool(registers[command[1]]), bool(registers[command[2]])
                        registers[command[3]] = str(int(a or b))
                    case "nor":
                        try:
                            command[1], command[2], command[3]
                        except:
                            error(PE)
                        try:
                            registers[command[1]], registers[command[2]], registers[command[3]]
                        except:
                            error(RE)
                        a, b = bool(registers[command[1]]), bool(registers[command[2]])
                        registers[command[3]] = str(int(not (a or b)))
                    case "xor":
                        try:
                            command[1], command[2], command[3]
                        except:
                            error(PE)
                        try:
                            registers[command[1]], registers[command[2]], registers[command[3]]
                        except:
                            error(RE)
                        a, b = bool(registers[command[1]]), bool(registers[command[2]])
                        registers[command[3]] = str(int(a ^ b))
                    case "equ":
                        try:
                            command[1], command[2], command[3]
                        except:
                            error(PE)
                        try:
                            registers[command[1]], registers[command[2]], registers[command[3]]
                        except:
                            error(RE)
                        a, b = registers[command[1]], registers[command[2]]
                        registers[command[3]] = str(int(a == b))
                    case "grt":
                        try:
                            command[1], command[2], command[3]
                        except:
                            error(PE)
                        try:
                            registers[command[1]], registers[command[2]], registers[command[3]]
                        except:
                            error(RE)
                        a, b = bool(registers[command[1]]), bool(registers[command[2]])
                        registers[command[3]] = str(int(a > b))
                    case "lss":
                        try:
                            command[1], command[2], command[3]
                        except:
                            error(PE)
                        try:
                            registers[command[1]], registers[command[2]], registers[command[3]]
                        except:
                            error(RE)
                        a, b = bool(registers[command[1]]), bool(registers[command[2]])
                        registers[command[3]] = str(int(a < b))
                    case "jmp":
                        counter = int(command[1]) - 1
                    case "jif":
                        try:
                            registers[command[2]]
                        except:
                            error(RE)
                        if registers[command[2]] == "1":
                            counter = int(command[1]) - 1
                    case "opn":
                        registers[command[1]] = "0"
                    case "inc":
                        try:
                            registers[command[1]]
                        except:
                            error(RE)
                        _ = registers[command[1]]
                        _ = float(_)
                        _ += 1
                        registers[command[1]] = str(_ if _ % 1 > 0 else int(_))
                    case "dec":
                        try:
                            registers[command[1]]
                        except:
                            error(RE)
                        _ = registers[command[1]]
                        _ = float(_)
                        _ -= 1
                        registers[command[1]] = str(_ if _ % 1 > 0 else int(_))
                    case ";":
                        pass
                    case _:
                        error(FE)
            except:
                error(PE)
        counter += 1
    if y == 1:
        getpass.getpass("Press ENTER to close the window...")
args = sys.argv
path = ""
c = ""
if len(args) > 1:
    path = args[1]
    c = open(path, "r").read()
    run(c, 1)
else:
    print("ASM0.5 [Version 1]\nType \"help\" for help.")
    while True:
        c = ""
        inp = input("> ")
        while inp not in ("run", "exit", "help"):
            c += inp + "\n"
            inp = input("> ")
        if inp == "run":
            run(c, 0)
            c = ""
        elif inp == "help":
            print("""
ASM05 help:
1. Functions:
sti reg, value            set reg <reg> to <value> (int)
sts reg, value            set reg <reg> to <value> (str) (hex)
otr reg                   print reg <reg>
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
Lss regA, regB, regDist   if <regA> < <regB>, set 1 to <regDist> else 0
jmp line                  jump to line <line>
jif line, reg             jump to line <line> if <reg> == 1
var <reg>                 make reg <reg>
bol reg, regDist          turn <reg> to boolean, set result to <regDist> 
inc reg                   <reg> += 1
dec reg                   <reg> -= 1

2. Errors:
RE         RegError (access a reg that doesn't exist)
TE         TypeError (not the type it expected)
FE         FuncError (invalid func)
PE         ParamError (invalid params) """)
        else:
            exit(0)
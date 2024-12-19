# Kernel for Procyon Command Line System

import sys
import os
import time
try:
    from blessed import Terminal
except:
    if sys.platform == "win32":
        os.system("pip install blessed")
    else:
        os.system("pip3 install blessed")

term = Terminal()


# Kernel APIs

def clrscr():
    print(term.clear)

def shutDown():
    print("Shutting down...")
    return sys.exit(0)

def reboot():
    print("Rebooting...")
    os.execv(sys.executable, ['python3', 'start.py'])

def getVersion():
    return "2.0.5"

def getBuild():
    return "2024.12.19.1303"

def getAuthor():
    return "Gautham Nair"

def getCompany():
    return "Procyonis Computing"

def getLicense():
    return "GNU GPL v3.0"

def getKernelName():
    return "Procyon Neo"

def getCodeName():
    return "Munnar"

def getReleaseName():
    return "ProcyonCLS 2025"

def getRelease():
    return "Developer Preview 12"

def printError(param, end="\n"):
    print(term.center(term.red(param)), end=end)

def printWarning(param, end="\n"):
    print(term.center(term.yellow(param)), end=end)

def printSuccess(param, end="\n"):
    print(term.center(term.green(param)), end=end)

def printInfo(param, end="\n"):
    print(term.center(term.blue(param)), end=end)

def println(param="", end="\n", flush=False):
    print(term.center(param), end=end, flush=flush)

def centered_input(term, prompt=""):
    width = term.width
    if prompt:
        println((prompt))
    input_width = 30
    center_pos = (width - input_width) // 2
    print('\r' + ' ' * center_pos, end='', flush=True)
    return input()

def bsod(error, msg):
    clrscr()
    print(term.bold_red("Kernel Panic : Bootloader error"))
    print("Technical Details : ")
    print(term.red(f" Error Code : {error}"))
    print(term.red(f" Error Description : {msg}"))
    time.sleep(5)
    sys.exit(1)

def printYellow(param):
    print(term.center(term.yellow(param)))

def printGreen(param):
    print(term.center(term.green(param)))

def printBlue(param):
    print(term.center(term.blue(param)))

def printCyan(param):
    print(term.center(term.cyan(param)))

def printMagenta(param):
    print(term.center(term.magenta(param)))

def printRed(param):
    print(term.center(term.red(param)))

def printWhite(param):
    print(term.center(term.white(param)))

def printBlack(param):
    print(term.center(term.black(param)))

def printBold(param):
    print(term.center(term.bold(param)))

def printUnderline(param):
    print(term.center(term.underline(param)))

def printInverted(param):
    print(term.center(term.reverse(param)))

def printStrikethrough(param):
    print(term.center(term.strikethrough(param)))

def printReset(param):
    print(term.center(term.normal(param)))

def printItalic(param):
    print(term.center(term.italic(param)))

def printOverline(param):
    print(term.center(term.overline(param)))

def printBlink(param):
    print(term.center(term.blink(param)))

def printDoubleUnderline(param):
    print(term.center(term.double_underline(param)))

def printDoubleStrikethrough(param):
    print(term.center(term.double_strikethrough(param)))

def printDoubleOverline(param):
    print(term.center(term.double_overline(param)))

def printDoubleBlink(param):
    print(term.center(term.double_blink(param)))

def printFramed(param):
    print(term.center(term.framed(param)))

def printEncircled(param):
    print(term.center(term.encircled(param)))

def printRainbow(param):
    print(term.center(term.color_rgb(255, 0, 0)(param)))

def callApplication(app, isAdmin=False):
    appResolved = f"python3 {app}.py 2.0.5 {isAdmin}"
    os.system(appResolved)

def callApplication3P(app, isAdmin=False):
    appResolved = f"python3 apps/{app}.py 2.0.5 {isAdmin}"
    os.system(appResolved)
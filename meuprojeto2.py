import pyautogui as at

def apertar_tab(qtd):
    for i in range(qtd):
        at.press("tab")
        at.sleep(0.01)


at.hotkey("win", "r")
at.write("chrome", 0.2)
at.press("enter")
at.write("www.instagram.com", 0.1)
at.press("enter")
at.sleep(5)
login = at.prompt("Digite seu login: ")
at.write(login, 0.1)
apertar_tab(1)
senha= at.prompt("Digite sua senha: ")
at.write(senha, 0.1)
at.press("enter")
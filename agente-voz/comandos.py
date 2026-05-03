import os
from voz import falar


def executar_comando(frase: str) -> bool:
    frase = frase.lower()

    if "abrir navegador" in frase or "chrome" in frase:
        falar("Abrindo navegador")
        os.system("start chrome.exe")
        return False
    
    elif "abrir youtube" in frase:
        falar("Abrindo YouTube")
        os.system("start https://www.youtube.com")
        return False

    elif "abrir excel" in frase:
        falar("Abrindo Excel")
        os.system("start excel")
        return False

    elif "abrir powerpoint" in frase:
        falar("Abrindo Powerpoint")
        os.system("start powerpnt")
        return False

    elif "abrir edge" in frase:
        falar("Abrindo Edge")
        os.system("start msedge")
        return False

    elif "abrir configurações" in frase:
        falar("Abrindo configurações")
        os.system("start ms-settings:")
        return False

    elif "fechar assistente" in frase or "sair" in frase:
        falar("Encerrando assistente...")
        return True

    return False
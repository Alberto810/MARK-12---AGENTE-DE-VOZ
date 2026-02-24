import os


def executar_comando(frase: str) -> bool:
    frase = frase.lower()

    if "abrir navegador" in frase or "chrome" in frase:
        os.system("start chrome")
        return False

    elif "abrir excel" in frase:
        os.system("start excel")
        return False

    elif "abrir powerpoint" in frase:
        os.system("start powerpnt")
        return False

    elif "abrir edge" in frase:
        os.system("start msedge")
        return False
    
    elif "abrir configurações" in frase:
        os.system("start ms-settings:")
        return False

    elif "fechar assistente" in frase or "sair" in frase:
        print("🛑 Encerrando assistente...")
        return True

    return False
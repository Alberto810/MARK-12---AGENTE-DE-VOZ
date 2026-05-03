def detectar_wake_word(frase: str):
    frase = frase.lower()

    if "jarvis" in frase:
        comando = frase.replace("jarvis", "").strip()

        if comando == "":
            return True, None  # só chamou o nome

        return True, comando

    return False, None
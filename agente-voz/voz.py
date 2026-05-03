import pyttsx3

def falar(texto: str):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 180)

        engine.say(texto)
        engine.runAndWait()
        engine.stop()

    except Exception as e:
        print(f"Erro na fala: {e}")
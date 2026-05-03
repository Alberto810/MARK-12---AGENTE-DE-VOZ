import speech_recognition as sr
import sounddevice as sd
import numpy as np

from comandos import executar_comando
from config import IDIOMA, TEMPO_AMBIENTE
from wakeword import detectar_wake_word

def gravar_audio(duracao=6.5, sample_rate=16000):
    print("🎤 Ouvindo...")
    audio = sd.rec(int(duracao * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype='int16')
    sd.wait()
    return audio.flatten(), sample_rate


def ouvir_microfone():
    recognizer = sr.Recognizer()

    try:
        audio_np, sample_rate = gravar_audio()

        audio_data = sr.AudioData(
            audio_np.tobytes(),
            sample_rate,
            2
        )

        frase = recognizer.recognize_google(audio_data, language=IDIOMA)

        print("🗣️ Você disse:", frase)
        
    except sr.UnknownValueError:
        print("Não entendi o áudio")
        return None

    ativado, comando = detectar_wake_word(frase)

    if ativado:
        print("🧠 Wake word detectada")

    if comando:
        return executar_comando(comando)
    else:
        print("🤖 Aguardando comando após 'Jarvis'...")
        return False


def main_loop():
    
    while True:
        if ouvir_microfone():
            break


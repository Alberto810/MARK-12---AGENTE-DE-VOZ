import speech_recognition as sr
import sounddevice as sd
import numpy as np

from comandos import executar_comando
from config import IDIOMA, TEMPO_AMBIENTE


def gravar_audio(duracao=5, sample_rate=16000):
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

        return executar_comando(frase)

    except sr.UnknownValueError:
        print("❌ Não entendi")
    except sr.RequestError as e:
        print(f"❌ Erro no serviço: {e}")
    except Exception as e:
        print(f"⚠️ Erro inesperado: {e}")

    return False


def main():
    print("🤖 Assistente iniciado...")

    while True:
        if ouvir_microfone():
            break


if __name__ == "__main__":
    main()
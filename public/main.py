import speech_recognition as sr

def recognize_speech_from_mic(recognizer, microphone):
    """Fonction pour reconnaître la voix à partir du micro."""
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Parle maintenant...")
        audio = recognizer.listen(source)
    
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Impossible de comprendre l'audio"
    except sr.RequestError:
        return "Erreur avec le service de reconnaissance"

if __name__ == "__main__":
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=2)

    print("✨ Jarvis en écoute continue... (dis 'stop' pour quitter)")

    while True:
        texte = recognize_speech_from_mic(r, mic)
        
        if texte.lower() == "stop":
            print("🛑 Arrêt de l'IA Jarvis.")
            break

        print(f"🎤 Vous avez dit : {texte}")

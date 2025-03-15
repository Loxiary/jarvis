import speech_recognition as sr

def DisplayAllMicrophonesAvailable():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

if __name__ == "__main__":
    r = sr.Recognizer()
    mic = sr.Microphone()
        
    # DisplayAllMicrophonesAvailable()
    mic.list_microphone_names()
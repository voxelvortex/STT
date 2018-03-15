import speech_recognition as sr

def getSpeech():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=48000,chunk_size=2048) as source:
        print("Say something!")
        audio = r.listen(source)
        print('Processing...')

    # recognize speech using Sphinx
    try:
        speechRec = str(r.recognize_google(audio))
        print("Detected: '" + speechRec + "'")
    except sr.UnknownValueError:
        print("Unable to tell what you were saying")
    except sr.RequestError as e:
        print("Error; {0}".format(e))
    return speechRec.split(' ')
import speech_recognition as sr
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Mendengarkan suara...")
    recognizer.adjust_for_ambient_noise(source) 
    audio = recognizer.listen(source, timeout=30, phrase_time_limit=30) 

    try:
        print("Mengubah suara menjadi teks...")
        text = recognizer.recognize_google(audio, language='id-ID')  
        print(f"Teks yang diucapkan: {text}")
    except sr.UnknownValueError:
        print(" tidak bisa memahami audio")
    except sr.RequestError as e:
        print(f"Permintaan  gagal; {e}")

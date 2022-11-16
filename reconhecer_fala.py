import speech_recognition as sr

rec = sr.Recognizer()
#print(sr.Microphone().list_microphone_names())
with sr.Microphone(0) as mic:
    rec.adjust_for_ambient_noise(mic) #ajusta o som ambiente
    print("Pode falar que eu vou gravar")
    audio = rec.listen(mic) #captando o audio
    texto = rec.recognize_google(audio, language="pt-BR") #reconhece o audio e transforma em texo
    print(texto)

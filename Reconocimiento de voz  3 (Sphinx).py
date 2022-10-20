#import the Speech Recognition library

import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:

	while True:

		audio = recognizer.listen(source)

		print(recognizer.recognize_sphinx(audio))
	
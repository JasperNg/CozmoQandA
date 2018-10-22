import sys
import os
os.chdir("/Users/dude/Desktop/Google")
import cozmo
from google import google

num_page = 1

#try:
#    from pynput.keyboard import Key, Listener
#    import speech_recognition as sr
#    import PyAudio
#except ImportError:
#    sys.exit('some packages are required, install them doing: `pip3 install --user termcolor SpeechRecognition PyAudio Pynput` to run this script.\nIf you are on linux do: `sudo apt-get install flac portaudio19-dev python-all-dev python3-all-dev && sudo pip3 install Pynput pyaudio`')

def Processing():
	if Text[0].lower() in("what","where"):
		question()

def question():
	if Text[1] == "is":
		question2()
	else:
		questionPlural()

def question2():
	if Text[2].lower() in("an","a","the","is"):
                #self.cozmo.say_text(Text[3]).wait_for_completed()
                cozmo.run_program(cozmo_program)
                #self.cozmo.say_text(search_results).wait_for_completed()
                #print (search_results[0])
                #break
	else:
		#self.cozmo.say_text(Text[2]).wait_for_completed()
		cozmo.run_program(cozmo_program1)
	    #if __name__ == "__Verax__":
                #SpeakUp.cozmo_program()
		#self.cozmo.say_text(search_results).wait_for_completed()
		#print (search_results[0])

		#break
        
def question3():
	if Text[2].lower() in("did","does"):
		#self.cozmo.say_text(Text[3]).wait_for_completed()
		#self.cozmo.say_text(Text[4]).wait_for_completed()
		cozmo.run_program(cozmo_program2)
	    #if __name__ == "__Verax__":
                #SpeakUp.cozmo_program()
		#self.cozmo.say_text(search_results).wait_for_completed()
		#print (search_results[0])
		#break
	else:
		#search up Text[2]
		#self.cozmo.say_text(Text[2]).wait_for_completed()
		cozmo.run_program(cozmo_program3)
	    #if __name__ == "__Verax__":
                #SpeakUp.cozmo_program()
		#self.cozmo.say_text(search_results).wait_for_completed()
		#print (search_results[0])

		#break

def questionPlural():
	if Text[1] == "are":
		
		#self.cozmo.say_text(Text[2]).wait_for_completed()
		cozmo.run_program(cozmo_program4)
	    #if __name__ == "__Verax__":
                #SpeakUp.cozmo_program()
		#self.cozmo.say_text(search_results).wait_for_completed()
		#robot.say_text(search_results).wait_for_completed()
		#print (search_results[0])
		
		#break
		
	else:
		#Processing()
                question3()
                
def cozmo_program(robot: cozmo.robot.Robot):
        search_results = google.search(Text[3], num_page)
        robot.say_text(str(search_results[0])).wait_for_completed()
        
def cozmo_program1(robot: cozmo.robot.Robot):
        search_results = google.search(Text[2], num_page)
        robot.say_text(str(search_results[0])).wait_for_completed()
        
def cozmo_program2(robot: cozmo.robot.Robot):
        search_results = google.search(Text[3] + Text[4], num_page)
        robot.say_text(str(search_results[0])).wait_for_completed()
        
def cozmo_program3(robot: cozmo.robot.Robot):
        search_results = google.search(Text[2], num_page)
        robot.say_text(str(search_results[0])).wait_for_completed()
        
def cozmo_program4(robot: cozmo.robot.Robot):
        search_results = google.search(Text[2], num_page)
        robot.say_text(str(search_results[0])).wait_for_completed()

#recognizer = sr.Recognizer()

#'''SETUP MIC'''
#with sr.Microphone() as source:

#        recognizer.pause_threshold = 0.8
#        recognizer.dynamic_energy_threshold = False #was True
#        recognizer.adjust_for_ambient_noise(source)
#        recognized = None
#try:
#            audio = recognizer.listen(source, timeout = 5)
#except sr.WaitTimeoutError:
#            cprint("Timeout...", "red")
#try:
#    recognized = recognizer.recognize_google(audio, key=None, language=lang_data['lang_ext']).lower() #GOOGLE
#            #recognized = recognizer.recognize_wit(audio, key=WIT_AI_KEY_EN) #WIT
#            #recognized = recognizer.recognize_sphinx(audio, language=lang_ext).lower() #SPINX
#            cprint("Speech Recognition service could not understand audio", "red")
#            prompt()
#except sr.RequestError as e:
#            cprint("Could not request results from Speech Recognition service, check your web connection; {0}".format(e), "red")
#            prompt()
            

Name = input("What is your name?")

print(" Hello "+Name)

Text = input("What do you want to ask? (Limited to What and Where questions)").split()

Processing()


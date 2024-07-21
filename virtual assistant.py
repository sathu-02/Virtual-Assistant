     
import pyttsx3
import datetime
import speechRecognition as sr

 


engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') 

engine.setProperty('voice', voice[0].id)

def speak(audio):

	engine.say(audio) 

	engine.runAndWait() 
def wishme():

	hour = int(datetime.datetime.now().hour)
def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")  

    except Exception as e:
        # print(e)    
        print("Say that again please...")   
        return "None" 
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


 


 

if __name__=="__main__" :

	speak("Hello, how may I assist you today?..")
	
    	wishMe()
    	while True:
    	# if 1:
        	query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        	if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            	speak('Searching Wikipedia...')
            	query = query.replace("wikipedia", "")
            	results = wikipedia.summary(query, sentences=2) 
            	speak("According to Wikipedia")
            	print(results)
            	speak(results)
		
		elif 'open youtube' in query:
            		webbrowser.open("youtube.com")
		elif 'open google' in query:
            		webbrowser.open("google.com")
		elif 'play music' in query:
            		music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            		songs = os.listdir(music_dir)
            		print(songs)    
            		os.startfile(os.path.join(music_dir, songs[0]))
	        elif 'the time' in query:
            		strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            		speak(f"Sir, the time is {strTime}")
		elif 'email to harshit' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harshitsutrave@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")    


		    



 

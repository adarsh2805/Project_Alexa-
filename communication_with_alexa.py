import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime
import pyjokes

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(command):
    engine.say(command)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        print('listening....')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
    return command

def listen():
  try:
   command=take_command()
   print(command)
   if 'alexa' in command:
       command = 'Hi dear how can i help you'
       speak(command)
       while True:
            try:
                command=take_command()
                print(command)
                if 'who is' in command:
                    command=command.replace('who is',"")
                    info=wikipedia.summary(command)
                    speak(info)
                elif 'time' in command:
                    time=datetime.datetime.today().strftime('%I %M')
                    speak('now time is '+ time)
                elif 'bye' in command :
                    command='Thank you good bye,have a nice day'
                    speak(command)
                    break
                elif 'joke' in command:
                    joke=pyjokes.get_joke()
                    print(joke)
                    speak(joke)
                    feedback=('nice','good','awesome','super')
                    speak('how is the joke dear')
                    feedback_joke=take_command()
                    if feedback_joke in feedback:
                        speak('Thank you dear')
                    elif 'dont understand' in feedback_joke:
                        speak('thats your problem hahaha')
                    else:
                        speak('Better luck next time hahaha')

                elif 'thank you alexa' in command:
                    speak('your welcome dear')

                else:
                    command='I didnt understand your command, could you please say it again'
                    speak(command)
            except:
                pass
   else:
       listen()
  except:
      pass

listen()
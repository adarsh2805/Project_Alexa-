import smtplib
from email.message import EmailMessage
import speech_recognition as sr
import  pyttsx3


def talk(message):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',160)
    engine.say(message)
    engine.runAndWait()


def listen():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('listening..')
            text=listener.listen(source)
            speech_text=listener.recognize_google(text)
            message=speech_text.lower()
            print(message)
        if message!=None:
            return message
        elif message==None:
            talk('please tell the information')
            listen()
    except:
        talk('i couldnt here your voice correctly please provide the details once again')
        listen()


def send_mail(reciver,subject,message):
    try:
        server=smtplib.SMTP('SMTP.gmail.com',587)
        server.starttls()
        server.login('adarshag2805@gmail.com','qwuggvajtfddqluc')
        email=EmailMessage()
        email['From']='Adarshag2805@gmail.com'
        email['To']=reciver
        email['Subject']=subject
        email.set_content(f'Hi Dear,''\n\n\t\t'+message+'\n\n\n\n\n\n'+'Thank You\n'+'Adarsh')
        server.send_message(email)
        talk('message sent')
    except:
        talk('email not sent')


def get_email(reciver):
    dict_email={
        'aadarsh':'adarshaag2805@gmail.com',
        'anvita':'anvitha020@gmail.com'
    }
    name=list(dict_email.keys())
    if reciver in name:
        return dict_email[reciver]
    else:
        return False


def get_reciver_address():
    talk('Please provide the name of the receiver ')
    reciver = listen()
    reciver_data=get_email(reciver)
    print(reciver_data)
    if reciver_data!=None:
        if reciver_data:
             reciver = reciver_data
             return reciver
        else:
            print(reciver)
            talk('reciver address is not available')
            get_reciver_address()
    else:
        talk('reciver address is shoudnt be none')
        get_reciver_address()


def get_subject():
    talk('please provide  the subject')
    subject = listen()
    return subject


def get_message():
    talk('please tell me the message that you intent send')
    message = listen()
    return message


def validate_det(reciver,subject,message,count=0):
    if count==0:
        count+=1
        talk('confirm your provided information is correct')
        talk(f'reciver is {reciver}')
        talk(f'subject is {subject}')
        talk(f'message is {message}')
    talk('is this correct')
    response = listen()
    try:
        if  response in ['yes','yeah',"it's correct","right"] :
            send_mail(reciver, subject, message)
            talk('do you want to continue again please respond yes or no ')
            con_responce=listen()
            return con_responce
        elif ['no','not','wrong',"it's not correct"]  in response:
            talk('what information need to change')
            feedback=listen()
            print(feedback)
            if 'receiver' in feedback:
                reciver=get_reciver_address()
                count=0
                validate_det(reciver,subject,message,count)
            elif 'subject' in feedback:
                subject=get_subject()
                count=0
                validate_det(reciver,subject,message,count)
            elif 'message' in feedback:
                message=get_message()
                count=0
                validate_det(reciver,subject,message,count)
            else:
                talk('response is invalid')
        else:
            talk('response is not correct')
    except:
        talk('please provide the response correctly')
        validate_det(reciver,subject,message,count=1)
    else:
        talk('sry for the inconvince coused i couldnt get the response properly')
        validate_det(reciver, subject, message,count=1)


def get_info():
        reciver=get_reciver_address()
        subject=get_subject()
        message=get_message()
        response=validate_det(reciver,subject,message)
        if 'yes' in response:
            get_info()
        elif 'no' in response:
            talk('thank you for using email voice process created by adarsh')
        else:
            get_info()


if __name__ == '__main__':
    talk('welcome to the mail service this side alexa, please provide the command properly to send the mail')
    get_info()





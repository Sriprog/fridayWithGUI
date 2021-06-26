import webbrowser as web
import time
import keyboard
import pywhatkit


def whatsapp(number,message,hr,min):
    num = '+91' +str(number)
    pywhatkit.sendwhatmsg(num,message,hr,min)



def Whatsapp_Grp(group_id,message):
    grp_id =  group_id
    pywhatkit.sendwhatmsg_to_group(grp_id,message)

def WhatsAppInstant(number,message):
    number = '+91' + str(number)
    pywhatkit.sendwhatmsg_instantly(number,message)

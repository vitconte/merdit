import sys
import time
import json
import telepot
from telepot.loop import MessageLoop
import merdit 
import responder

# funzione che viene eseguita ad ogni messaggio ricevuto
def handle(message):
    
    merdIt = merdit.Merdit()

    user_id = message["from"]["id"]
    if (message['text'] is not None):
        text = message['text']

        num_array = []
        for s in text.split(' '): 
            if s.isdigit():
                num_array.append(s)

        if (text.isdigit() or len(num_array) == 1):
            if text.isdigit():
                txt = text
            else:
                txt = num_array[0]

            t_state = merdIt.get_trainState(txt)

            if t_state is None:
                message = "Stai facendo il simpatico? Inserisci un numero treno valido"
            else:
                if t_state == 0:
                    message = "Treno in orario"
                else:
                    message = "Il treno ha %s min di ritardo" % t_state
        
        else:
           resp = responder.Responder()
           message = resp.get_message(text)

        bot.sendMessage(user_id, message)

if __name__ == '__main__':
    
    with open('config.json') as data_file:    
        data = json.load(data_file)

    if not data["token"]:
        print ("Insert token")
        exit(0) 

    # access token
    access_token = data["token"] 

    # set bot token
    bot = telepot.Bot(access_token)
    MessageLoop(bot, handle).run_as_thread()
    
    print ('Listening ...')

    # Keep the program running.
    while 1:
        time.sleep(10)
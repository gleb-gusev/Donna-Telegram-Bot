import telebot
from raven import Client
from telebot import types
from keyboard import Markup
from keyboard import Hack
import random

# Initialize Raven and Telegram API

client = Client('SENTRY')
bot = telebot.TeleBot("TOKEN")

# Set Updates Retrieving

updates = bot.get_updates(1234,100,40)

try:

    @bot.message_handler(commands=['start'])
    def send_introduce(message):
        Hack.flashback_is_active = False
        bot.send_message(message.chat.id, 'Hello, ' + message.chat.first_name +'.')
        bot.send_message(message.chat.id, "I'm Donatella Moss, you can chat with me whenver you want.")
        bot.send_message(message.chat.id, 'Anyway, I can be sometimes busy at work in the West Wing with Josh. So, you\'ll need to wait a little ;)')
        bot.send_message(message.chat.id, 'You can see with /help command, what we can do together')
        bot.send_message(message.chat.id, 'Looking forward to chat with you.')
        bot.send_message(message.chat.id, 'Donna.')


    @bot.message_handler(commands=['help'])
    def help_text(message):

        Hack.flashback_is_active = False
        txt = open('helpfile.txt')
        helptext = txt.read()
        bot.send_message(message.chat.id, helptext)





    # Intro Recreated from the Season 2 In the Shadow of Two Gunmen Part II

    @bot.message_handler(commands=['flashback'])

    @bot.message_handler(content_types=['text'])
    def process_message(message):

        if (message.text == '/flashback'):
            Hack.flashback_is_active = True

        if (Hack.flashback_is_active == True):
            answermarkup = types.ReplyKeyboardMarkup(row_width=1)

            if (message.text == '/flashback'):
                answermarkup = types.ReplyKeyboardMarkup(row_width=1)
                answermarkup.add(Markup.hibtn)
                bot.send_message(message.chat.id, "Choose option from keyboard to begin", reply_markup=answermarkup)

            elif (message.text == 'Hi!'):
                answermarkup.add(Markup.whoareyoubtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "Hi!", reply_markup=answermarkup)


            elif message.text == ('Who are you?') and (Hack.numberofcalls == 0):
                Hack.numberofcalls = Hack.numberofcalls + 1
                iambtn = types.KeyboardButton('I\'m' + ' ' + message.chat.first_name + ' ' + message.chat.last_name)
                answermarkup.add(iambtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "I'm Donna Moss, who are you?", reply_markup=answermarkup)



            elif message.text == ('I\'m' + ' ' + message.chat.first_name + ' ' + message.chat.last_name):
                answermarkup.add(Markup.yesbtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "Ah.", reply_markup=answermarkup)

            elif message.text == ('Yes.'):
                answermarkup.add(Markup.oldassistantbtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "I\'m your new assistant.", reply_markup=answermarkup)

            elif message.text == ('Did I have an old assistant?'):
                answermarkup.add(Markup.whoareyoubtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "Maybe not.", reply_markup=answermarkup)


            elif message.text == ('Who are you?') and (Hack.numberofcalls == 1):
                Hack.numberofcalls = Hack.numberofcalls + 1
                answermarkup.add(Markup.whichwomanbtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id,
                                 "I'm Donna Moss, I came here to volunteer and the woman assigned me to you.",
                                 reply_markup=answermarkup)


            elif message.text == ('Which woman?'):
                answermarkup.add(Markup.youmeanbtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "Becky.", reply_markup=answermarkup)

            elif message.text == ('You mean Margaret?'):
                answermarkup.add(Markup.whoareyoubtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "Yes.", reply_markup=answermarkup)

            elif message.text == ('Who are you?') and (Hack.numberofcalls == 2):
                Hack.numberofcalls = Hack.numberofcalls + 1
                answermarkup.add(Markup.goingtotalkbtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "I'm Donna Moss, I'll be working as your assistant.",
                                 reply_markup=answermarkup)


            elif message.text == ('I\'m going to talk to Margaret.'):
                answermarkup.add(Markup.yeahbtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "Actually, " + message.chat.first_name + '...', reply_markup=answermarkup)

            elif message.text == ('Yeah?') and (Hack.numberofcalls == 3):
                Hack.numberofcalls = Hack.numberofcalls + 1
                answermarkup.add(Markup.yeahbtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "When I said I was assigned to you?", reply_markup=answermarkup)

            elif message.text == ('Yeah?') and (Hack.numberofcalls == 4):
                Hack.numberofcalls = Hack.numberofcalls + 1
                answermarkup.add(Markup.whoareyoubtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "I may have been overstating it a little.", reply_markup=answermarkup)

            elif message.text == ('Who are you?') and (Hack.numberofcalls == 5):
                Hack.numberofcalls = Hack.numberofcalls + 1
                answermarkup.add(Markup.boyfriendbtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "I'm Donna Moss, I drove up here from Madison, Wisconsin?",
                                 reply_markup=answermarkup)

            elif message.text == ('When did your boyfriend break up with you?'):
                answermarkup.add(Markup.parentsjokebtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, 'What makes you think that my boyfriend broke up with me?',
                                 reply_markup=answermarkup)

            elif message.text == ('Well, you\'re too old for your parents to have kicked you out of the house.'):
                answermarkup.add(Markup.graduateqtnbtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id,
                                 "I'm here because I want to work for Bartlet. I'm a college graduate, with a degree in Political Science and Government",
                                 reply_markup=answermarkup)

            elif message.text == ('Where did you graduate?') and (Hack.numberofcalls == 6):
                Hack.numberofcalls = Hack.numberofcalls + 1
                answermarkup.add(Markup.graduateqtnbtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "Hmm?", reply_markup=answermarkup)

            elif message.text == ('Where did you graduate?') and (Hack.numberofcalls == 7):
                Hack.numberofcalls = Hack.numberofcalls + 1
                answermarkup.add(Markup.lookbtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "Okay, when I said I graduated, I may have been overstating a little?",
                                 reply_markup=answermarkup)

            elif message.text == ('Look...'):
                answermarkup.add(Markup.fromwherebtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "I was a couple of credits short.", reply_markup=answermarkup)

            elif message.text == ('From where?'):
                answermarkup.add(Markup.majoredqtnbtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "University of Wisconsin.", reply_markup=answermarkup)

            elif message.text == ('You majored in Political Science and Government?'):
                answermarkup.add(Markup.uhuhbtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "And, uh, Sociology and Psychology.", reply_markup=answermarkup)

            elif message.text == ('Uh-huh.'):
                answermarkup.add(Markup.okbtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "And biology for a while, with a minor in French?",
                                 reply_markup=answermarkup)

            elif message.text == ('Okay.'):
                answermarkup.add(Markup.majorsqtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "And, uh, drama?", reply_markup=answermarkup)

            elif message.text == ('You had five majors and two minors in four years?'):
                answermarkup.add(Markup.oklistenbtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "Two years.", reply_markup=answermarkup)

            elif message.text == ('Okay, listen...'):
                answermarkup.add(Markup.bfolderqtnbtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "I had to drop out. I had to drop out.", reply_markup=answermarkup)

            elif message.text == ('Your boyfriend was older than you?'):
                answermarkup.add(Markup.joshtirade)
                answermarkup.add(Markup.boyfriendolder)
                bot.send_message(message.chat.id, "I think that question is of a personal nature?",
                                 reply_markup=answermarkup)

            elif message.text == ('Your boyfriend was older?'):
                answermarkup.add(Markup.lawstudentbtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "Yes.", reply_markup=answermarkup)

            elif message.text == ('Law student?'):
                answermarkup.add(Markup.joshtirade2)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "Medical student.", reply_markup=answermarkup)

            elif message.text == (
            'And the idea was that you\'d drop out and pay the bills till he was done with his residency.'):
                answermarkup.add(Markup.whybrokeqtnbtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "Yes.", reply_markup=answermarkup)

            elif message.text == ('And why did Dr. Freeloader break up with you.'):
                answermarkup.add(Markup.joshtirade3)
                answermarkup.add(Markup.startover)
                bot.send_message(message.chat.id, "What makes you think he broke up with me?", reply_markup=answermarkup)

            elif message.text == ('This can\'t be a place where people come to find their confidence and start over.'):
                answermarkup.add(Markup.sorrybtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "Why not?", reply_markup=answermarkup)

            elif message.text == ('I\'m sorry?'):
                answermarkup.add(Markup.becausebtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "Why can't it be those things?", reply_markup=answermarkup)

            elif message.text == ('Because...'):
                answermarkup.add(Markup.joshtirade4)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "What, is it going to interfere with my typing?",
                                 reply_markup=answermarkup)

            elif message.text == (
            'Donna, we\'re picking up today and going to South Carolina. If you want to stay in the Manchester office'):
                answermarkup.add(Markup.cantcarrybtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "I want to come to Charleston.", reply_markup=answermarkup)

            elif message.text == ('I can\'t carry you, Donna! I got a lot of guys out there not making the trip.'):
                answermarkup.add(Markup.withwhat)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id, "I'll pay my own way.", reply_markup=answermarkup)

            elif message.text == ('With what?'):
                answermarkup.add(Markup.donnabtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id,
                                 "I'll sleep on the floor, I'll sell my car. Eventually, you're going to put me on salary.",
                                 reply_markup=answermarkup)

            elif message.text == ('Donna.'):
                answermarkup.add(Markup.goaheadbtn)
                answermarkup.add(Markup.skipbtn)
                bot.send_message(message.chat.id,
                                 "Look. I think I might be good at this. I think you might find me valuable.",
                                 reply_markup=answermarkup)

            elif message.text == ('Go ahead.'):
                finalmarkup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                finalmarkup.add(Markup.finishbtn)
                bot.send_message(message.chat.id, '[Donna grabs the phone.]', reply_markup=finalmarkup)
                bot.send_message(message.chat.id,
                                 '[into phone] Bartlet for America, ' + message.chat.first_name + ' ' + message.chat.last_name + '\'s' + ' office. Uh, yes, I think I\'m going to someone from the press office get back to you if it\'s related to -- yes. Uh, yes',
                                 reply_markup=answermarkup)

            elif message.text == ('[You\'re taking your badge holder off your neck and hanging it to Donna, she smiles]'):
                Hack.flashback_is_active = False
                bot.send_message(message.chat.id,
                                 "[into phone] Yes.")
                bot.send_message(message.chat.id, "End of Play ;) Did you enjoyed it?", reply_markup=Markup.commandmarkup)


            elif message.text == ("Exit"):
                bot.send_message(message.chat.id,"End of Play. I hope you will get to the end one time...")
                Hack.flashback_is_active = False
                Hack.numberofcalls = 0

        else:

           # bot.send_message(message.chat.id, "Ok, I got you. But I don't know what to say on this now...")


        # TODO Add more quotes to quotes.txt.

            quotesarchive  = open("quotes.txt", "r")
            quotesarchive = quotesarchive.read().split("[e]")
            print (len(quotesarchive))
            bot.send_message(message.chat.id,quotesarchive[random.randrange(0,len(quotesarchive)-1)],reply_markup=None)


except Exception as Error:

    client.captureException()






#Echoing Function

'''

@bot.message_handler(func=lambda message: True)

def echo_all(message):

        bot.reply_to(message, message.text)

'''

# none_stop True/False (default False) - Don't stop polling when receiving an error from the Telegram servers

bot.polling(none_stop=True, interval=0)
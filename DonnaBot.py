import telebot
from telebot import types
from keyboard import markup
from keyboard import hack


bot = telebot.TeleBot("TOKEN")

updates = bot.get_updates(1234,100,20)

@bot.message_handler(commands=['start'])
def send_introduce(message):
    bot.send_message(message.chat.id, 'Hello, ' + message.chat.first_name +'.')
    bot.send_message(message.chat.id, "I'm Donatella Moss, you can chat with me whenver you want.")
    bot.send_message(message.chat.id, 'Anyway, I can be sometimes busy at work in the West Wing with Josh. So, you\'ll need to wait a little ;)')
    bot.send_message(message.chat.id, 'You can see with /help command, what we can do together')
    bot.send_message(message.chat.id, 'Looking forward to chat with you.')
    bot.send_message(message.chat.id, 'Donna.')


@bot.message_handler(commands=['help'])
def help_text(message):
    txt = open('helpfile.txt')
    print (txt)
    helptext = txt.read()
    bot.send_message(message.chat.id,helptext)





# Intro Recreated from the Season 2 In the Shadow of Two Gunmen Part II

@bot.message_handler(commands=['flashback'])

@bot.message_handler(content_types=['text'])
def process_message(message):
    print (message.text)

    if (message.text == '/flashback'):
        hack.flashback_is_active = True

    if (hack.flashback_is_active == True):
        print ('Flashback is active - Acting by the script')
        answermarkup = types.ReplyKeyboardMarkup(row_width=1)

        if (message.text == '/flashback'):
            answermarkup = types.ReplyKeyboardMarkup(row_width=1)
            answermarkup.add(markup.hibtn)
            bot.send_message(message.chat.id, "Choose option from keyboard to begin", reply_markup=answermarkup)

        elif (message.text == 'Hi!'):
            print(message.text)
            answermarkup.add(markup.whoareyoubtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "Hi!", reply_markup=answermarkup)


        elif message.text == ('Who are you?') and (hack.numberofcalls == 0):
            hack.numberofcalls = hack.numberofcalls + 1
            iambtn = types.KeyboardButton('I\'m' + ' ' + message.chat.first_name + ' ' + message.chat.last_name)
            answermarkup.add(iambtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "I'm Donna Moss, who are you?", reply_markup=answermarkup)



        elif message.text == ('I\'m' + ' ' + message.chat.first_name + ' ' + message.chat.last_name):
            answermarkup.add(markup.yesbtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "Ah.", reply_markup=answermarkup)

        elif message.text == ('Yes.'):
            answermarkup.add(markup.oldassistantbtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "I\'m your new assistant.", reply_markup=answermarkup)

        elif message.text == ('Did I have an old assistant?'):
            answermarkup.add(markup.whoareyoubtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "Maybe not.", reply_markup=answermarkup)


        elif message.text == ('Who are you?') and (hack.numberofcalls == 1):
            hack.numberofcalls = hack.numberofcalls + 1
            answermarkup.add(markup.whichwomanbtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id,
                             "I'm Donna Moss, I came here to volunteer and the woman assigned me to you.",
                             reply_markup=answermarkup)


        elif message.text == ('Which woman?'):
            answermarkup.add(markup.youmeanbtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "Becky.", reply_markup=answermarkup)

        elif message.text == ('You mean Margaret?'):
            answermarkup.add(markup.whoareyoubtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "Yes.", reply_markup=answermarkup)

        elif message.text == ('Who are you?') and (hack.numberofcalls == 2):
            hack.numberofcalls = hack.numberofcalls + 1
            answermarkup.add(markup.goingtotalkbtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "I'm Donna Moss, I'll be working as your assistant.",
                             reply_markup=answermarkup)


        elif message.text == ('I\'m going to talk to Margaret.'):
            answermarkup.add(markup.yeahbtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "Actually, " + message.chat.first_name + '...', reply_markup=answermarkup)

        elif message.text == ('Yeah?') and (hack.numberofcalls == 3):
            hack.numberofcalls = hack.numberofcalls + 1
            answermarkup.add(markup.yeahbtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "When I said I was assigned to you?", reply_markup=answermarkup)

        elif message.text == ('Yeah?') and (hack.numberofcalls == 4):
            hack.numberofcalls = hack.numberofcalls + 1
            answermarkup.add(markup.whoareyoubtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "I may have been overstating it a little.", reply_markup=answermarkup)

        elif message.text == ('Who are you?') and (hack.numberofcalls == 5):
            hack.numberofcalls = hack.numberofcalls + 1
            answermarkup.add(markup.boyfriendbtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "I'm Donna Moss, I drove up here from Madison, Wisconsin?",
                             reply_markup=answermarkup)

        elif message.text == ('When did your boyfriend break up with you?'):
            answermarkup.add(markup.parentsjokebtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, 'What makes you think that my boyfriend broke up with me?',
                             reply_markup=answermarkup)

        elif message.text == ('Well, you\'re too old for your parents to have kicked you out of the house.'):
            answermarkup.add(markup.graduateqtnbtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id,
                             "I'm here because I want to work for Bartlet. I'm a college graduate, with a degree in Political Science and Government",
                             reply_markup=answermarkup)

        elif message.text == ('Where did you graduate?') and (hack.numberofcalls == 6):
            hack.numberofcalls = hack.numberofcalls + 1
            answermarkup.add(markup.graduateqtnbtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "Hmm?", reply_markup=answermarkup)

        elif message.text == ('Where did you graduate?') and (hack.numberofcalls == 7):
            hack.numberofcalls = hack.numberofcalls + 1
            answermarkup.add(markup.lookbtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "Okay, when I said I graduated, I may have been overstating a little?",
                             reply_markup=answermarkup)

        elif message.text == ('Look...'):
            answermarkup.add(markup.fromwherebtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "I was a couple of credits short.", reply_markup=answermarkup)

        elif message.text == ('From where?'):
            answermarkup.add(markup.majoredqtnbtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "University of Wisconsin.", reply_markup=answermarkup)

        elif message.text == ('You majored in Political Science and Government?'):
            answermarkup.add(markup.uhuhbtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "And, uh, Sociology and Psychology.", reply_markup=answermarkup)

        elif message.text == ('Uh-huh.'):
            answermarkup.add(markup.okbtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "And biology for a while, with a minor in French?",
                             reply_markup=answermarkup)

        elif message.text == ('Okay.'):
            answermarkup.add(markup.majorsqtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "And, uh, drama?", reply_markup=answermarkup)

        elif message.text == ('You had five majors and two minors in four years?'):
            answermarkup.add(markup.oklistenbtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "Two years.", reply_markup=answermarkup)

        elif message.text == ('Okay, listen...'):
            answermarkup.add(markup.bfolderqtnbtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "I had to drop out. I had to drop out.", reply_markup=answermarkup)

        elif message.text == ('Your boyfriend was older than you?'):
            answermarkup.add(markup.joshtirade)
            answermarkup.add(markup.boyfriendolder)
            bot.send_message(message.chat.id, "I think that question is of a personal nature?",
                             reply_markup=answermarkup)

        elif message.text == ('Your boyfriend was older?'):
            answermarkup.add(markup.lawstudentbtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "Yes.", reply_markup=answermarkup)

        elif message.text == ('Law student?'):
            answermarkup.add(markup.joshtirade2)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "Medical student.", reply_markup=answermarkup)

        elif message.text == (
        'And the idea was that you\'d drop out and pay the bills till he was done with his residency.'):
            answermarkup.add(markup.whybrokeqtnbtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "Yes.", reply_markup=answermarkup)

        elif message.text == ('And why did Dr. Freeloader break up with you.'):
            answermarkup.add(markup.joshtirade3)
            answermarkup.add(markup.startover)
            bot.send_message(message.chat.id, "What makes you think he broke up with me?", reply_markup=answermarkup)

        elif message.text == ('This can\'t be a place where people come to find their confidence and start over.'):
            answermarkup.add(markup.sorrybtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "Why not?", reply_markup=answermarkup)

        elif message.text == ('I\'m sorry?'):
            answermarkup.add(markup.becausebtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "Why can't it be those things?", reply_markup=answermarkup)

        elif message.text == ('Because...'):
            answermarkup.add(markup.joshtirade4)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "What, is it going to interfere with my typing?",
                             reply_markup=answermarkup)

        elif message.text == (
        'Donna, we\'re picking up today and going to South Carolina. If you want to stay in the Manchester office'):
            answermarkup.add(markup.cantcarrybtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "I want to come to Charleston.", reply_markup=answermarkup)

        elif message.text == ('I can\'t carry you, Donna! I got a lot of guys out there not making the trip.'):
            answermarkup.add(markup.withwhat)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id, "I'll pay my own way.", reply_markup=answermarkup)

        elif message.text == ('With what?'):
            answermarkup.add(markup.donnabtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id,
                             "I'll sleep on the floor, I'll sell my car. Eventually, you're going to put me on salary.",
                             reply_markup=answermarkup)

        elif message.text == ('Donna.'):
            answermarkup.add(markup.goaheadbtn)
            answermarkup.add(markup.skipbtn)
            bot.send_message(message.chat.id,
                             "Look. I think I might be good at this. I think you might find me valuable.",
                             reply_markup=answermarkup)

        elif message.text == ('Go ahead.'):
            finalmarkup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
            finalmarkup.add(markup.finishbtn)
            bot.send_message(message.chat.id, '[Donna grabs the phone.]', reply_markup=finalmarkup)
            bot.send_message(message.chat.id,
                             '[into phone] Bartlet for America, ' + message.chat.first_name + ' ' + message.chat.last_name + '\'s' + ' office. Uh, yes, I think I\'m going to someone from the press office get back to you if it\'s related to -- yes. Uh, yes',
                             reply_markup=answermarkup)

        elif message.text == ('[You\'re taking your badge holder off your neck and hanging it to Donna, she smiles]'):
            hack.flashback_is_active = False
            bot.send_message(message.chat.id,
                             "[into phone] Yes.")
            bot.send_message(message.chat.id, "End of Play ;) Did you enjoyed it?")


        elif message.text == ("Exit"):
            hack.flashback_is_active = False

            '''
             # TODO Set Possible Options for Keyboard here or dismiss it.

            '''
    else:
        print ('Flashback isn\'t active - Handle this like the ordinary message')


    # TODO Set up for the text messages with type 'text' so we can get few basic answers behind the script.







#Echoing Function

'''

@bot.message_handler(func=lambda message: True)

def echo_all(message):

        bot.reply_to(message, message.text)

'''


bot.polling()
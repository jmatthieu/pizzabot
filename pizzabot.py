# -*- coding: UTF-8 -*-

import socket
# import string
import numpy as np
# import commands

"""
ADD CONFIG
"""

irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( IP, PORT ) )
irc.send ( 'USER  ' + IDENT + ' ' + IDENT + ' bla : ' + REALNAME + '\n' )
irc.send ( 'NICK ' + NICK + '\n')



while True:
    text = irc.recv(4096)
    print(text)
    data = text.split()

    if "PING" in text:
        irc.send('PONG ' + data[1] + '\n')
    if "Debian" in text:
        irc.send ( 'JOIN ' + channel + '\n')
        irc.send('PRIVMSG ' + channel + ' :Hello, I am the PizzaBot! I love to hear about pizzas... Type !help to learn more!\n')

    if "PRIVMSG" in text:
        print(text + '\n')
        print(data)
        if data[3] == ":!help":
            irc.send('PRIVMSG ' + channel + ' :Hello, you can !add a_pizza, !rm a_pizza, and type !pizzas to see the available pizzas\' list. You can display the ordered pizzas by typing !order\n')
        # ADD A PIZZA TO THE LIST
        if data[3] == ":!add":
            if data[4] in pizzalist:
                irc.send('PRIVMSG ' + channel + ' :You have taste! I added a ' + data[4] + ' to the list!\n')
                pizzalist[data[4]][0] += 1
            else:
                irc.send('PRIVMSG ' + channel + ' :No such pizza! Type !pizzas to see the menu!\n')
        # REMOVE A PIZZA FROM THE LIST
        if data[3] == ":!rm":
            if data[4] in pizzalist:
                if pizzalist[data[4]][0] > 0:
                    irc.send('PRIVMSG ' + channel + ' :OK, OK, I removed a ' + data[4] + ' from the list. I feel a bit sad.\n')
                    pizzalist[data[4]][0] -= 1
                else:
                    irc.send('PRIVMSG ' + channel + ' :No such pizza was ordered!\n')
        # LIST PEOPLE THAT ORDERED PIZZAS
        if data[3] == ":!listpeople":
            irc.send('PRIVMSG ' + channel + ' :Here is the list:\n')
            for ii in np.arange(0,len(pizzalist)):
                irc.send('PRIVMSG ' + channel + ' :' + peoplelist[ii] + ' ordered a ' + pizzalist[ii] + '\n')
        # LIST PIZZA ORDER LIST
        if data[3] == ":!order":
            somme = 0
            for key in pizzalist:
                somme += pizzalist[key][0]
            if somme == 0:
                irc.send('PRIVMSG ' + channel + ' :No one seems to crave for a pizza!\n')
            else:
                irc.send('PRIVMSG ' + channel + ' :The order contains:\n')
                for key in pizzalist:
                    if pizzalist[key][0] > 0:
                        irc.send('PRIVMSG ' + channel + ' :' + str(pizzalist[key][0]) + ' ' + key + '\n')
        # LIST AVAIL PIZZA
        if data[3] == ":!pizzas":
            irc.send('PRIVMSG ' + channel + ' :Here is the list of available pizzas (you can type !whatis pizza for more info):\n')
            for key in pizzalist:
                irc.send('PRIVMSG ' + channel + ' :' + key + '\n')
        # WHAT IS A PIZZA
        if data[3] == ":!whatis":
            if data[4] in pizzalist:
                irc.send('PRIVMSG ' + channel + ' :' + pizzalist[data[4]][1] + '\n')
            else:
                irc.send('PRIVMSG ' + channel + ' :No such pizza exists!\n')

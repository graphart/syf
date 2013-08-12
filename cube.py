#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nazwa pliku: code.py
import time
import random

global accusum
accusum = None
global winadd
global winadd2
global remisos
global accusum2
accusum2 = None
global accusum
accusum = 0
remisos = 0
winadd2 = 0
winadd = 0

def rzut_kostka(name1,name2,rep):
    swd = 1
    while swd < rep+1:
        filoop = random.randint(1,2)
        filoop2 = random.randint(1,2)
        print 'gracz %s wylosowal: ' % (name1),filoop, 'oraz ', filoop2
        accusum = filoop + filoop2
        print 'lacznie: ', accusum
        time.sleep(0.2)
        
        soloop = random.randint(1,2)
        soolop2 = random.randint(1,2)
        accusum2 = soloop + soolop2
        print 'gracz %s wylosowal: ' % (name2), soloop, 'oraz ', soolop2, 'lacznie: ', accusum2
        swd = swd +1
        time.sleep(0.2)
        
        if accusum > accusum2:
            global winadd
            winadd = winadd +1
            print 'player %s win!' %(name1), 'wygral po raz: ', winadd, '\n'           
        elif accusum < accusum2:
            global winadd2
            winadd2 = winadd2 +1 
            print 'player %s win!' % (name2), 'wygral po raz: ',winadd2, '\n'
        else:
            print 'remis!'
            global remisos
            remisos = remisos + 1
#################################
def repo():
    while True:
        rzut_kostka(1,2,1)
        print 'proba...'
        if accusum  > accusum2:
            break
        elif accusum < accusum2:
            break
        elif accusum == accusum2:
            continue

##################################                
rzut_kostka('wolfram','przegryw',6)
print '-------wyniki--------'
print 'gracz nr 1 lacznie wygral: ', winadd 
print 'gracz nr 2 lacznie wygral: ', winadd2 
print 'liczba remisow: ', remisos

if winadd > winadd2:
    print '-----------GRACZ NR 1 WYGRAL-------------'
elif winadd < winadd2:
    print '-----------gracz nr 2 wygral--------------'
elif winadd == winadd2:
    print '--------dogrywka-----------\n\n'
    repo()
#elif winadd == winadd2:
    #time.sleep(2.5)
#rzut_kostka()
    
    

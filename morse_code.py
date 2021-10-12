from machine import Pin, PWM
from time import sleep

# Importing Morse Code Dictionary
MorseCode = {'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

#Setting GPI Pinouts
button = Pin(10, Pin.IN, Pin.PULL_UP)
shortled = Pin(11, Pin.OUT)
longled = Pin(12, Pin.OUT)
speaker = PWM(Pin(13))

# Setting Variables
fast = 0.1
slow = 0.2
sound = True # Will allow you to turn the sound off/on
light = True # Will allow you to turn lights off/on
pitch = 600
volume = 1500
speaker.freq(pitch) #Pitch of sound. Higher this number, higher the pitch

# Setting LED 
shortled.low()
longled.low()

def LetterLookup(StringValue):
    for letter in MorseCode:
        if MorseCode[letter] == StringValue:
            return letter
    return ' '

def BlinkLetter(letter):
    
    if letter == ' ':
        sleep(0.6)
        return
    if letter != '':
        CurrentLetter = MorseCode[letter]

    print(f'{letter} : {CurrentLetter}')
    for cchar in CurrentLetter:
        if (cchar == '-'):
            blinkspeed = slow
        if (cchar == '.'):
            blinkspeed  = fast
        if light :
            if blinkspeed == fast: shortled.high()
            if blinkspeed == slow: longled.high()
        if sound :
            speaker.freq(pitch)
            speaker.duty_u16(volume)
        sleep(blinkspeed)
        if light :
            if blinkspeed == fast: shortled.low()
            if blinkspeed == slow: longled.low()
        if sound : speaker.duty_u16(0)
        sleep(blinkspeed)
    
    sleep(0.6)

def PlayMessage(message):
    for cchar in message:
        BlinkLetter(str.upper(cchar))

print('To use this, type "PlayMessage("YOUR STRING HERE")" to initiate this.')
print('This will translate your text to Morse Code and play it back for you!')
print('If you want Sound off, type "sound = False", "sound = True" to turn it on.')
print('If you want Light off, type "light = False", "light = True" to turn it on.')
print('')
print('Give it a go!')
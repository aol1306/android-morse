#!/usr/bin/python2
import time
import logging
import sys
import subprocess

# only set dot length
DOT = 0.2
DASH = 3*DOT


CODE = {
'a' : '.-',
'b' : '-...',
'c' : '-.-.',
'd' : '-..',
'e' : '.',
'f' : '..-.',
'g' : '--.',
'h' : '....',
'i' : '..',
'j' : '.---',
'k' : '-.-',
'l' : '.-..',
'm' : '--',
'n' : '-.',
'o' : '---',
'p' : '.--.',
'q' : '--.-',
'r' : '.-.',
's' : '...',
't' : '-',
'u' : '..-',
'v' : '...-',
'w' : '.--',
'x' : '-..-',
'y' : '-.--',
'z' : '--..',
'.' : '.-.-.-',
',' : '--..--',
'?' : '..--..',
'/' : '-..-.',
'@' : '.--.-.',
'1' : '.----',
'2' : '..---',
'3' : '...--',
'4' : '....-',
'5' : '.....',
'6' : '-....',
'7' : '--...',
'8' : '---..',
'9' : '----.',
'0' : '-----',
}

logging.basicConfig(level=logging.DEBUG)

def dot():
    logging.debug("dot")
    logging.info("singal on")
    cmd = 'termux-vibrate -f -d '+str(int(DOT*1000))
    try:
        ret = subprocess.call(cmd, shell=True)
    except OSError as e:
        logging.error(e)
        logging.error("Install termux-api first!")
        quit()
    logging.info("singal off")

def dash():
    logging.debug("dash")
    logging.info("singal on")
    cmd = 'termux-vibrate -f -d '+str(int(DASH*1000))
    try:
        ret = subprocess.call(cmd, shell=True)
    except OSError as e:
        logging.error(e)
        logging.error("Install termux-api first!")
        quit()
    logging.info("singal off")

def part_of_letter_sleep():
    logging.debug("part of letter sleep")
    time.sleep(DOT)

def letter_sleep():
    logging.debug("letter sleep")
    time.sleep(DASH)

def word_sleep(): 
    logging.debug("word sleep")
    time.sleep(DOT*7)

def transmit_letter(letter):
    letter = letter.lower()
    logging.debug("transmitting letter "+letter)
    try:
        code = CODE[str(letter)]
    except KeyError:
        logging.error("no such letter")
        return
    size = len(code)
    i = 1
    for sign in code:
        if sign == '.':
            dot()
        if sign == '-':
            dash()
        if (i<size):
            part_of_letter_sleep()
        i += 1

def transmit_word(word):
    size = len(word)
    i = 1
    for letter in word:
        transmit_letter(letter)
        if (i<size):
            letter_sleep()
        i += 1

def transmit(text):
    text = text.split()
    size = len(text)
    i = 1
    for word in text:
        transmit_word(word)
        if (i<size):
            word_sleep()
        i += 1

if __name__ == "__main__":
    try:
        while True:
            transmit(sys.argv[1])
            logging.info("Sleeping for 10 seconds before transmitting again.")
            time.sleep(10)
    except IndexError:
        quit("usage: ./morse.py '[text]'")

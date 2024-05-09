"Caear Cipher by Eric McAfee"

#Constants for message and key
MESSAGE = ''
KEY = 0

def encryptMessage(message):
    translatedMessage = ''
    for character in (message):
        unicodeVal = ord(character)
        translatedMessage += (chr(unicodeVal + KEY))
    return translatedMessage

def decodeMessage(message):
    translatedMessage = ''
    for character in (message):
        unicodeVal = ord(character)
        translatedMessage += (chr(unicodeVal - KEY))
    return translatedMessage



MESSAGE = input("Please enter a message to encyrpt > ")
KEY = int(input("Please enter a secret key > "))
scrambledMessage = encryptMessage(MESSAGE)
input("Press Enter to scramble message.")
f = open("translatedMessage", "w")
f.write(scrambledMessage)
f.close()



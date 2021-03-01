class CaesarCypher(object):
    """docstring for CaesarCypher"""

    # Numbers as key dictionary
    numKeyIndex = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f",
                   7: "g", 8: "h", 9: "i", 10: "j", 11: "k", 12: "l", 13: "m",
                   14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t",
                   21: "u", 22: "v", 23: "w", 24: "x", 25: "y", 26: "z"}

    # Letters as key dictionary
    charKeyIndex = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6,
                    "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13,
                    "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
                    "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

    # INIT
    def __init__(self, message, key):
        """Initialize class members"""
        self.message = message
        self.key = key

    # Encode message based on given key
    def encode(self):
        """Encode your message based on the key"""

        # Init
        messageList = []
        encodedMessage = ""

        # Add message to array
        for i in self.message.lower():
            messageList.append(i)

        # Loop through each char in message
        for i in messageList:
            # Check if current char is a letter
            if i in self.charKeyIndex:
                # Make sure key plus letter index is less than 26
                if self.charKeyIndex[i] + self.key <= 26:
                    # Shift charachter over
                    encodedMessage += self.numKeyIndex[self.charKeyIndex[i] + self.key]
                # Wrap back to beginning if index exceeds 26
                else:
                    encodedMessage += self.numKeyIndex[(self.charKeyIndex[i] + self.key) - 26]
            # Adds non-alpha chars to output string
            else:
                encodedMessage += i

        # return output
        return encodedMessage

    def checkKey(self, key):
        """Check to see if the key is valid"""
        if key < 0 and key > 25:
            print("Your key is invalid")
            return False
        else:
            return True

    def decode(self):
        """Decode the message based on a specific key"""
        messageList = []
        decodedMessage = ""

        for i in self.message.lower():
            messageList.append(i)

        for i in messageList:
            if i in self.charKeyIndex:
                if self.charKeyIndex[i] - self.key >= 0:
                    decodedMessage += self.numKeyIndex[(self.charKeyIndex[i] - self.key)]
                else:
                    decodedMessage += self.numKeyIndex[(self.charKeyIndex[i] - self.key) + 26]
            else:
                decodedMessage += i
        return decodedMessage

    def encodeFromFile(self, file):
        fileMessage = open(file)
        return fileMessage

    def decodeFromFile(self, file):
        fileMessage = open(file)
        return fileMessage

menu = True
while menu:
    print("*" * 13)
    print("Caesar Cypher")
    print("*" * 13 + "\n")
    choice = input("Select: Encode/Decode/File: ")
    if choice.lower() == "encode" or choice.lower() == "e":
        message = input("Enter your message here: ")
        key = int(input("Enter your encryption key: "))
        cypher = CaesarCypher(message, key)
        cypher.checkKey(key)
        if cypher.checkKey(key):
            print("Your encoded message is | " + cypher.encode() + " |\n")
            menuChoice = input("Would you like to continue? ")
            if menuChoice.lower() == "yes" or menuChoice.lower() == "y":
                menu = True
            else:
                menu = False

    elif choice.lower() == "decode" or choice.lower() == "d":
        message = input("Enter your message here: ")
        key = int(input("Enter your encryption key: "))
        cypher = CaesarCypher(message, key)
        cypher.checkKey(key)
        if cypher.checkKey(key):
            print("Your decoded message is | " + cypher.decode() + " |\n")
            menuChoice = input("Would you like to continue? ")
            if menuChoice.lower() == "yes" or menuChoice.lower() == "y":
                menu = True
            else:
                menu = False

    elif choice.lower() == "file" or choice.lower() == "f":
        message = input("Encode or Decode: ")
        if message.lower() == "encode" or message.lower() == "e":
            menu = False
    else:
        print("Your selection was invalid, please try again")

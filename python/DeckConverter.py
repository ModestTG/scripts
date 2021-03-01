from html.parser import HTMLParser
import os


class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		outFile = open("F:\Student Data\Temp\\" + os.path.splitext(file)[0] + ".txt", "a")
		for att in attrs:
			if att[0] == 'number':
				outFile.write(att[1] + " ")
			elif att[0] == 'name':
				if att[1] == 'Mountain':
					outFile.write("[ZEN:244] " + att[1] + "\n")
				elif att[1] == 'Plains':
					outFile.write("[ZEN:233] " + att[1] + "\n")
				elif att[1] == 'Swamp':
					outFile.write("[ZEN:241] " + att[1] + "\n")
				elif att[1] == 'Island':
					outFile.write("[ZEN:237] " + att[1] + "\n")
				elif att[1] == 'Forest':
					outFile.write("[ZEN:269] " + att[1] + "\n")
				else:
					outFile.write(att[1] + "\n")
		outFile.close()

		def handle_data(self, data):
			if self.get_starttag_text() == 'deckname':
				outFile.write("NAME:" + os.path.splitext(file)[0] + "\n")

parser = MyHTMLParser()
for file in os.listdir("E:\Google Drive\Miscellaneous\Decks - Cockatrice"):
	if file.endswith(".cod"):
		inFile = open("E:\Google Drive\Miscellaneous\Decks - Cockatrice\\" + file, "r")
		parser.feed(inFile.read())
		print("Working on deck: " + os.path.splitext(file)[0])
		inFile.close()

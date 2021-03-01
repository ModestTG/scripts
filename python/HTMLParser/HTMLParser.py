from html.parser import HTMLParser
from html.entities import name2codepoint


class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		# outFile = open("output.txt", "a")
		print("Start tag:", tag)
		for attr in attrs:
			print("     attr:", attr)
			if attr[0] == 'number':
				# outFile.write(attr[1] + " ")
				pass
			elif attr[0] == 'name':
				# outFile.write(attr[1] + "\n")
				pass
		# outFile.close()

	def handle_endtag(self, tag):
		print("End tag  :", tag)

	def handle_data(self, data):
		if data is None:
			print("Data     : None")
		else:
			print("Data     :", data)

	def handle_comment(self, data):
		print("Comment  :", data)

	def handle_entityref(self, name):
		c = chr(name2codepoint[name])
		print("Named ent:", c)

	def handle_charref(self, name):
		if name.startswith('x'):
			c = chr(int(name[1:], 16))
		else:
			c = chr(int(name))
		print("Num ent  :", c)

	def handle_decl(self, data):
		print("Decl     :", data)

parser = MyHTMLParser()
file = open("E:\Google Drive\Miscellaneous\Decks - Cockatrice\Blue-White-Red Control.txt", "r")
parser.feed(file.read())

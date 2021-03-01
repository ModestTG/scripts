myHTML = open("E:\Google Drive\Miscellaneous\Decks - Cockatrice\Ancient Wilds.cod", "r")
page = myHTML.read()
for item in page.split("</card>"):
	if "<card>" in item:
		print(item[item.find("<card>") + len("<card>"):])

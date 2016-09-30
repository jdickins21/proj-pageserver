import os.path

def main():
	if os.path.exists("pages/trivia.html"):
		print("no slash: true")
	
	if os.path.exists("/pages/trivia.html"):
		print("slash: true")
		
	if os.path.exists("~pages/trivia.html"):
		print("no slash tilda: true")
		
	if os.path.exists("~/pages/trivia.html"):
		print("tilda slash: true")
		
	
main()
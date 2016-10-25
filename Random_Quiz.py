Easy_Quizzes = ["Gala, Jonagold and Pink Lady are varieties of __________.",
				"__________ was named after the Italian city of Venice ",
				"If you were puting numbers on new changing room lockers to be numbered from 1 to 100, you would use the number 9, __________ times.",
				"In the Star Wars films, __________ and __________ played Obi Wan Kenobi"]
Blank = "__________"


Easy_Answers =[["APPLE"], ["VENEZUELA"], ["20"], ["ALEC GUINESS", "EWAN MCGREGOR"]]

def Answer_Match(mode, question_count, blank):
	if mode == "E":
		return Easy_Answers[question_count][blank]
	
def Number_Of_Blanks(splitted_string):
	count = 0
	for pos in splitted_string:
		if pos == Blank:
			count += 1
			return count

def Prompt_User(blank, answer):
	user_input = raw_input("Please fill in blank " + (str)(blank) + ": ")
	while user_input != answer:
		user_input = raw_input("Please try again. Fill in blank " + (str)(blank) + ": ")


def Select_Quiz(mode,Quiz):
	question_count = 0
		
	for question in Quiz: 
		print "QUESTION " + (str)(question_count) + " : "
		print question

		splitted_string = question.split()	
		new_string = []
		blank = 0
		for word in splitted_string:
			if Blank not in word:
				new_string.append(word)
			else: 
				answer = Answer_Match(mode, question_count, blank)
				Prompt_User(blank, answer)
				word = word.replace(Blank, answer)
				new_string.append(word)
				blank += 1
		new_string = " ".join(new_string)
		print new_string + "\n"
			
		question_count += 1

def Random_Quiz():
	print "Welcome to random quiz! Please select a difficulty"
	print "Enter E for Easy Mode"
	print "Enter M for Medium Mode"
	print "Enter H for Hard Mode"

	mode = raw_input("Mode: ")
	if mode == "E":
		print "\n\n\n\nWelcome to Easy Mode! Please answer the following ten questions."
		print "Please write all your answers in upper case"
		Select_Quiz(mode, Easy_Quizzes)

Random_Quiz()
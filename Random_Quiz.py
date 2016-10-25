Easy_Quizzes = ["Gala, Jonagold and Pink Lady are varieties of __________.",
				"__________ was named after the Italian city of Venice ",
				"If you were puting numbers on new changing room lockers to be numbered from 1 to 100, you would use the number 9, __________ times.",
				"In the Star Wars films, __________ and __________ played Obi Wan Kenobi"]
Blank = "__________"


Easy_Answers =[["Apple"], ["Venezuela"], ["20"], ["Alec Guiness", "Ewan McGregor"]]

def Answer_Match(user_input, mode, question_count):
	if mode == "E":
		if user_input == Easy_Answers[question_count]:
			print "Correct!"
			return Easy_Answers[question_count][0]
		else:
			print "Incorrect."
			return Easy_Answers[question_count][0]

def Number_Of_Blanks(splitted_string):
	count = 0
	for pos in splitted_string:
		if pos == Blank:
			count += 1
			return count


def Select_Quiz(mode):
	if mode == "E":
		print "\n\n\n\nWelcome to Easy Mode! Please answer the following ten questions."
		question_count = 0
		
		for question in Easy_Quizzes: 
			print "QUESTION " + (str)(question_count) + " : "
			print question



			splitted_string = question.split()	
			new_string = []
			for word in splitted_string:
				if Blank not in word:
					new_string.append(word)
				else: 
					user_input = raw_input("Please fill the blank: ")
					answer = Answer_Match(user_input, mode, question_count)
					word = word.replace(Blank, answer)
					new_string.append(word)
			new_string = " ".join(new_string)
			print new_string
			
			question_count += 1




def Random_Quiz():
	print "Welcome to random quiz! Please select a difficulty"
	print "Enter E for Easy Mode"
	print "Enter M for Medium Mode"
	print "Enter H for Hard Mode"

	mode = raw_input("Mode: ")

	Select_Quiz(mode)
Random_Quiz()
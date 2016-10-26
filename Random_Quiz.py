Blank = "_________________"

Easy_Quizzes = ["Gala, Jonagold and Pink Lady are varieties of " + Blank + " .",
				Blank + " was named after the Italian city of Venice ",
				"If you were puting numbers on new changing room lockers to be numbered from 1 to 100 , you would use the number 9 , " + Blank + " times .",
				"In the Star Wars films , " + Blank + " and " + Blank + "played Obi Wan Kenobi ."]


Easy_Answers =[["APPLE"], ["VENEZUELA"], ["20"], ["ALEC GUINESS", "EWAN MCGREGOR"]]

def Answer_Match(mode, answer, answer_index):
	if mode == "E":
		return Easy_Answers[answer][answer_index]

	
#def Number_Of_Blanks(splitted_string):
	#count = 0
	#for pos in splitted_string:
		#if pos == Blank:
			#count += 1
			#return count

def Prompt_User(blank_index, answer):
	user_input = raw_input("Please fill in blank " + (str)(blank_index) + ": ")
	while user_input != answer:
		user_input = raw_input("Please try again. Fill in blank " + (str)(blank_index) + ": ")
	print "Correct!"


def Display_Answers(new_string, question, answer):
	join_string = " ".join(new_string)
	string_index = join_string.find(answer)
	space = len(Blank)
	string_with_answer = J= join_string  + question[string_index + space:]
	print string_with_answer



def Select_Quiz(mode,quiz):
	question_index = 0
		
	for question in quiz: 
		print "QUESTION " + (str)(question_index) + " : "
		print question

		splitted_string = question.split()	
		new_string = []
		blank_index = 0	
		for word in splitted_string:
			if Blank not in word:
				new_string.append(word)
			else: 
				answer = Answer_Match(mode, question_index, blank_index)
				Prompt_User(blank_index, answer)
				new_string.append(answer)
				Display_Answers(new_string, question, answer)
				blank_index += 1
		question_index += 1

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
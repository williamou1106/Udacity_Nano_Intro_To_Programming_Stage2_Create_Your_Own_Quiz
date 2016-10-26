import sys

#Creating a blank for user to fill in the answer.
Blank = "_________________"

#Stores quizzes in lists
Easy_Quizzes = ["Gala, Jonagold and Pink Lady are varieties of " + Blank + " .",
				Blank + " was named after the Italian city of Venice ",
				"If you were puting numbers on new changing room lockers to be numbered from 1 to 100 , you would use the number 9 , " + Blank + " times .",
				"In the Star Wars films , " + Blank + " and " + Blank + " played Obi Wan Kenobi ."]

#Stores answers in Lists. Questions with multiple answers are stored in a list within the lists.
Easy_Answers =[["APPLE"], ["VENEZUELA"], ["20"], ["ALEC GUINESS", "EWAN MCGREGOR"]]


# Takes in the "mode" for selecting which quiz from above, the "question_index" for selecting which matching answer to the respective question, and the "answer_index" to
# account for questions with multiple answers. Returns the answer to the question
def Answer_Match(mode, question_index, answer_index):
	if mode == "E":
		return Easy_Answers[question_index][answer_index]

#prompts the user to answer the current blank repeatedly until correct, or until penalties run out. "Blank_index" is to name and print the blank numerically for the current question.
#"answer" is used match the answer to the user input. "penalty" keeps track of errors user make.
def Prompt_User(blank_index, answer, penalty):
	user_input = raw_input("\nPlease fill in blank " + (str)(blank_index) + ": ")
	while user_input != answer:
		user_input = raw_input("Please try again. Fill in blank " + (str)(blank_index) + ": ")
		penalty = penalty - 1
		if penalty <= 0: 
			sys.exit("\nYou've used up all your penality. Quiz has shut down")
	print "\nCorrect!"
	return penalty

#Takes in the string from "Select_Quiz", fills the current blank with answer, and print on screen. The "new_string" is joined together and concatenated with the
#rest of the string by finding the location of the blank in question. The product is "string_with_answer".
def Display_Answers(new_string, question, answer):
	join_string = " ".join(new_string)
	string_index = join_string.find(answer) + len(Blank)
	string_with_answer = join_string + question[string_index:]
	print string_with_answer


def Select_Quiz(mode, quiz, penalty):
	#Starts at question 1 on position zero in the quizzes above.
	question_index = 0
	#Relay through each questions	
	for question in quiz: 
		#Print the question number on the screen
		print "\nQUESTION " + (str)(question_index) + " : "
		print question
        #Split the question into parts in list for the purpose of locating the blanks.
		splitted_string = question.split()	
		new_string = []
		#Create a blank index to keep track of blanks in the current question
		blank_index = 0
		#Go through each parts in the list to find blanks
		for word in splitted_string:
			if Blank not in word:
				new_string.append(word)
			else:
				# When Blanks are located, use the "Answer_Match" to find the answer for the blank 
				# then prompts the user using the "Prompt_User" to ask user to test user. If user
				# gets the correct answerm, "Display_Answers" will print the question with the answer
				# on screen.
				answer = Answer_Match(mode, question_index, blank_index)
				penalty = (int)(Prompt_User(blank_index, answer, penalty))
				new_string.append(answer)
				Display_Answers(new_string, question, answer)
				blank_index += 1
		# Goes to the next question
		question_index += 1

def Random_Quiz():
	print "WELCOME TO RANDOM QUIZ! PLEASE SELECT A DIFFICULTY"
	print "***Enter E for Easy Mode"
	print "***Enter M for Medium Mode"
	print "***Enter H for Hard Mode"
	print "***Penalty is the number of errors you can make before you fail the quiz.\n"
	#Let user select the game mode, and the penalty they can have before quiz quits
	mode = raw_input("Mode: ")
	penalty = raw_input("Penalty: ")
	if mode == "E":
		print "\n\n\n\nWELCOME TO EASY MODE! PLEASE ANSWER THE FOLLOWING 10 QUESTIONS."
		print "***Please write all your answers in upper case"
		print "***For questions with multiple answer. If required.Please answer in alphabetical order\n"
		Select_Quiz(mode, Easy_Quizzes, penalty)

Random_Quiz()
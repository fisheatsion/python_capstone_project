# declare varables
questions = (" When should you use lambda functions in Python?:",
             " How do you create a variable with the floating-point number 2.8?:",
             " How do you insert COMMENTS in Python code?: ",
             " Which one is NOT a legal variable name?: ",
             " How do you create a variable with the numeric value 5?: ")  # tuple Questions

options = (("A. For complex functions", "B. replace named functions",
             "C. For short inline operations (e.g., inside map()", "D.To speed up code execution"),
           ("A. x = 2.8", "B. A and D", "C. float x = 2.8", "D. x = float(2)"),
           ("A. /*This is a comment*/", "B. //This is a comment",
            "C. #This is a comment", "D. This is a comment#"),
           ("A. MYvar,", "B. my-var", "C. my_var", "D. _myvar"),
           ("A. C and D", "B. x = five", "C.int x = 5", "D. x = 5")) # 2 dimentional Tulip

answers = ("C", "A", "C", "B", "D")  # Tuple of answers
guesses = []  # a list of guesses
score = 0
question_num = 0

for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("---------------------")
print("       RESULTS       ")
print("---------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end="")
print()    

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()    

score = int(score / len(questions) * 100)
print("----------------------")
print(f"Your score is: {score}%")
print("----------------------")
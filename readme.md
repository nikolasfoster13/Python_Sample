# Little Professor
Little Professor was a toy "calculator" that would generate ten different math problems to solve. For instance, if the toy were to display "4 + 0 = ", the user would answer "4". If the toy were to display "4 + 1 = ", the user would answer "5". If the user were to answer incorrectly, the toy would display "EEE". After three incorrect answers for the same problem, the toy would simply display the correct answer.

professor.py is a program that:
* Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program will reprompt.
* Randomly generates 10 math problems formatted as "x + y = ", wherein each x and y is a non-negative integer with n digits. 
* Prompts the user to solve each of these problems. If an answer is not correct (or not even a number), the program outputs "EEE" and prompts the user again, allowing the user up to three tries in total for that problem. If the user still has not answered correctly after three tries, the program outputs the correct answer.
* The program ultimately outputs the user's score: the number of correct answers out of 10.

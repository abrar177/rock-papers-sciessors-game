
#in this assignment, I will be coding different functions to create a hangman game.
#the game consists of 8 attempts to guess the correct letter, and the user losing the game
#if the correct letters are not guessed in the 8 attempts.
#the second part is building a matrix filled with 0s and 1s, and then using that to see if there's an even number
#of 1s in the list of columns.

import random

def check_term(term, guesses):
    """
    here, i'm checking to see if the character of the secret word is in the word, and making the correct dashes for guessing.     

    :param term, guesses: parameters are term, and guesses, and it's used to check if the user guesses is in the term    
    :return: returning even_columns which contain the indexes of columns with an even numbers of 1. 
    :if statements: if character is in the term, we add that to the  char. if not, we add dashes
    """
    won = True
    result = ""  # Initialize an empty string to store the result

    for char in term:
        if char in guesses:
            result += char  # Append the character to the result string
        else:
            result += '-'  # Append a dash to the result string
            won = False

    print(result)  # Print the result after checking all characters
    return won

def play_hangman():
    """
    here, we're trying to see if the user letter is in the secret word. if it is, the dahses replace, if not we store that into a list, and check other conditions, example if it's repeating or is not a letter. 
    :param term, guesses: parameters are term, and guesses, and it's used to check if the user guesses is in the term    
    :return: no return, but if it's not in won, it states how many tries we have left. 
    :if statements: if user guesses non-letter or more than one, it asks them to input a letter. if it's not in the word, is subtracts from tries. 
    """
    # Secret word is "banjo"
    secret_word = "banjo"

    #stores all the guessed letters here
    guesses = []
    
    won = False  # Initialize won as False
    print("Let's play hangman!")

    check_term(secret_word, guesses)
    tries = 8

    #tries is more than 0 and not won
    while tries > 0 and not won:
        user_input = input('Guess a letter: ').lower()  #turns it into lowercase letter 


        #make sure if it's a lsingle etter 
        if not user_input.isalpha() or len(user_input) != 1:
            print("That is not a letter. Enter a letter.")
        elif user_input in guesses:
            print(f"You've already guessed {user_input}")
        else:
            guesses.append(user_input)
            if user_input not in secret_word:
                tries -= 1
                won = check_term(secret_word, guesses)
            else:
                won = check_term(secret_word, guesses)

            #tells user how many tries left 
            if not won:
                print("You have", tries, "tries remaining.")

    if won:
        print("You win!")  #game won
    else:
        print("You lose.")    #game lost 
            

#problem 2
def make_matrix(num_rows, num_cols):
    """
    using for loops to iterate the 0s and 1s to create a matrix with rows and columns. 
    
    :param num_rows, num_cols: represents the rows and columns to build the matrix   
    :return: returning a which is the matrix filled with 0s and 1s. 
    :if statements: none
    """

    # Made an empty matrix
    matrix =  []

    #checking values in range rows 
    for i in range(num_rows):
        row = [random.randint(0,1) for r in range (num_cols)]  #inputing either 1 or 0
        matrix.append(row)   #adds to row 
        return matrix   #gives us the overall matrix 
       



#problem 3
def even_cols(matrix):
    """
    using the matrix from the last problem to determine if the columns have an equal numbers of 1.
    using for loops to repeat the process of going through num_rows and using module to see if it's divisible by 2. 
    
    :param matrix: matrix is the parameter that the function is taking.    
    :return: returning even_columns which contain the indexes of columns with an even numbers of 1. 
    :if statements: if not matrix bascially returns an empty list when the matrix is empty. 
    """
    even_columns = []  #An empty list to store column indexes


    if not matrix:
        return even_columns  # Returns an empty list if the matrix is empty

    #number of rows and columns in the input matrix 
    num_rows = len(matrix)     #tells us the length of the matrix 
    num_cols = len(matrix[0])    #length of matrix at value 0

    #for loop for columns and counts 0s
    for col in range(num_cols):
        count_ones = 0   #counts number of 1s in current column
        for row in range(num_rows): 
            count_ones += matrix[row][col]   #add matrix rows and columns 

        #see if it has even numbers of 1
        if count_ones % 2 == 0:
            even_columns.append(col)

    return even_columns #gives back indexes of columns with an even numbers of 1 




    
#print results
def main():
    play_hangman()

if __name__ == '__main__':
    main()

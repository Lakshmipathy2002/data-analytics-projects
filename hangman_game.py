import random

fields = ['programming', 'sports', 'states', 'bodyparts','contries']

def word_guess(field):
    programming = ['java', 'sql', 'python', 'machinelearning', 'reactjs', 'excel', 'powerbi', 'javascript', 'html', 'css']
    sports = ['cricket', 'hockey', 'football', 'chess', 'badminton', 'basketball', 'tennis']
    states = ['assam', 'kerala', 'nepal', 'tamilnadu', 'karnataka', 'telangana', 'andhrapradesh']
    bodyparts = ['eye', 'ear', 'head', 'hands', 'legs', 'neck']
    contries=['india','srilanka','newzealand','england','bangladesh','australia','westindies','southafrica']

    collection = {'programming': programming, 'sports': sports, 'states': states, 'bodyparts': bodyparts, 'contries':contries}
    
    val = collection[field]
    word = random.choice(val)
    return word

def user_guess_word(word, guessed_letter):
    display = "" 
    for i in word:
        if i in guessed_letter:
            display += i
        else:
            display += "_"
    return display

def hangman():
    print("Let's play hangman game...")
    selected_field = random.choice(fields)
    print("Your guess word will be one of the", selected_field, "domain........")
    secret_word = word_guess(selected_field)
    guessed_letter = []
    attempts = 5

    while attempts > 0:
        print("Word:", user_guess_word(secret_word, guessed_letter))
        guess = input("Guess letter: ").lower()
        
        if guess in guessed_letter:
            print("You have already guessed that letter. Try again...")
            continue
        guessed_letter.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print("Incorrect guess! Attempts left:", attempts)
        
        if set(secret_word) <= set(guessed_letter):
            print("Congratulations! You guessed the correct word:", secret_word)
            break

    if attempts == 0:
        print("Sorry, your attempts are completed.")
        print("The secret word is:", secret_word)

while True:
    hangman()
    next_call = input("Do you want to play again? (yes/no): ").lower()
    if next_call != 'yes':
        print("Thanks for playing this game.")
        break
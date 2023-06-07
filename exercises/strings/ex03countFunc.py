def countChar(phrase, alphabet):
    count = 0
    for letter in phrase:
        if letter == alphabet:
            count = count + 1
        
    print(count)


userInput = input('Enter a string:')
character = input('Enter letter to be counter:')
countChar(userInput.lower(), character.lower())
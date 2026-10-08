def remove_fourth_character(word: str) -> str:
    #fourthWord = word[3:3] 
    previousWord = word[0:3]
    afterWord = word[4:]
    newWord = previousWord + afterWord
    return newWord
    


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))

def get_middle(s):
    '''
    You are going to be given a word.
    Your job is to return the middle character of the word.
    If the word's length is odd, return the middle character.
    If the word's length is even, return the middle 2 characters.
    '''
    return s[len(s) // 2] if len(s) % 2\
        else f'{s[len(s) // 2 - 1]} {s[len(s) // 2]}'.replace(' ', '')
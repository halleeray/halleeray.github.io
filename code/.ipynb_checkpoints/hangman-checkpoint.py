# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = list(word)
        self.progress = list(len(self.word)*'_')

    def guess(self, char):
        if self.remaining_guesses == -1 or self.status == STATUS_LOSE or self.status == STATUS_WIN:
            raise ValueError("The game has already ended.")

        else:
            if char in self.progress:
                #char already guessed
                self.remaining_guesses -= 1
            
            elif char in self.word:
                for x in range(len(self.word)):
                    if self.word[x] == char:
                        self.progress[x] = char
            else:
                #char not guessed and not in word
                self.remaining_guesses -= 1
    
            if all(char != '_' for char in self.progress):
                self.status = STATUS_WIN
            else:
                if self.remaining_guesses == -1:
                    self.status = STATUS_LOSE
        

    def get_masked_word(self):
        return "".join(self.progress)

    def get_status(self):
        return self.status
    
#passed 7 tests - completed
            

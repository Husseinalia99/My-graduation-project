class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        
        return self.word + ': ' + self.meaning
       
flash = []
print("welcome to flashcard")
 
while(True):
    word = input("Enter the word : ")
    meaning = input("Enter the meaning of the word : ")
     
    flash.append(flashcard(word, meaning))
    option = int(input("enter 0 , if you want to add another flashcard : "))
     
    if(option==0):
        break
         
print("\nYour flashcards")
i=0
while i < len(flash):
    print(flash[i])
    i=i+1
    
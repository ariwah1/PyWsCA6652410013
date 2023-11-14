def sen():
    sentence = input("Enter sentence:")

    words = sentence.split()

    numword = len(words)

    numdulicates = 0 
    set_word = set(words)
    for words in set_word :
     numdulicates += words.count(words)-1

    print("the sentece contains {} word".format(numword))
    print("the are {} dulicates word the word are".format(numdulicates))
    for words in set_word :
            print(" ",words,words.count(words))

if __name__ == "__sen__":
    sen()

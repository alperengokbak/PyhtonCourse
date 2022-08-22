def sortingSentence():
    s = input("Write Sentence To Sort Whole Letters: ")
    sentence = s.split()
    sentence.sort()
    for word in sentence:
        print(word)

#%% The Best Way To Sort Sentence
sortingSentence()


def __init__(self):
    # open stop_words.txt for reading
    # create a list attribute
    infile = open("stop_words.txt")
    self.stop_words = []
    for word in infile:  # loop through each word in text file
        word = word.strip()
        self.stop_words.append(word)  # add to new list

    print("Initializing Word Counter")
    # set the attrbute wordCounts to an empty dictionary
    self.wordCounts = {}

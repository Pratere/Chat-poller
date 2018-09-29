from difflib import SequenceMatcher
test1 = ["String", "String", "Strong", "Strang", "String", "Wrong", "Wrang", "Wong", "Dong", "String", "String", "Strong", "Strang", "String", "Wrong", "Wrang", "Wong", "Dong", "Clong"]
test2 = [" String", "string", "Strwing", "Strong ", "Sta ir", "Stare", "s Tor"]
test3 = ["String", "String", "Strong", "Strang", "String", "Wrong", "Wrang", "Wong", "Dong", "String", "String", "Strong", "Strang", "String", "Wrong", "Wrang", "Wong", "Dong", "Clong", " String", "string", "Strwing", "Strong ", "Sta ir", "Stare", "s Tor"]

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def getSimilars(list1):
    startDict = [] # A list to hold dictionaries of similair words and their frequency
    for string in list1:
        found = False # An initial false found value to see if the string is found in a dictionary
        # print(string)
        stringl = string.lower().replace(" ", "") # Make the string lowercase and remove all spaces
        if len(startDict) == 0:
            startDict.append({stringl:1}) # If there are no dictionaries in the list then we need to make the first one
            # print(stringl, "Added to new Dict")
            found = True # Say we found a place for it
        else:
            for dict in startDict:
                if stringl in dict:
                    dict[stringl] += 1 # Add 1 to the count of that word
                    # print(stringl, "Found in Dict:", dict)
                    found = True # Say we found a place for it
                    break # We do not need to look at anymore of the strings because we found it
                else:
                    for key in dict:
                        if similar(stringl, key) >= 0.75:
                            dict[stringl] = 1
                            found = True # Say we found a place for it
                            # print(stringl, "Found to be similar in Dict")
                            break # We do not need to look at anymore of the strings because we found it
            if not found:
                startDict.append({stringl:1}) # If we can not find the word in any of our dictionaries make a new one for it
                # print(stringl, "Added to new Dict")


    return startDict

def getTopWords(listOfDicts):
    topWords = {} # A dictionary to hold our keywords and their total counts
    for dict in listOfDicts:
        top = 0
        total = 0
        for key in dict:
            if dict[key] > top: # If a word has more counts than the current top word in that dictionary make it the top word
                top = dict[key]
                topKey = key
            total += dict[key] # Add all the counts together to make the total for that word
        if total in topWords: # If words tie add them to a string
            topWords[total] += " + " + topKey
        else:
            topWords[total] = topKey # Create a new key:value pair to hold the new word

    return topWords

def main():
    print(getTopWords(getSimilars(test1)))
    print(getTopWords(getSimilars(test2)))
    print(getTopWords(getSimilars(test3)))

if __name__ == '__main__':
    main()

def makeScrabbleDict():
    d = {}
    d[1] = "AEIOULNSTR"
    d[2] = "DG"
    d[3] = "BCMP"
    d[4] = "FHVWY"
    d[5] = "K"
    d[8] = "JX"
    d[10] = "QZ"

    scoreDict = {}
    for k,v in d.items():
        for letter in v:
            scoreDict[letter] = k
    return scoreDict

def scoreWord(word):
    word = word.upper()
    sd = makeScrabbleDict()
    score = 0
    for letter in word:
        score += sd[letter]

    return score

# print(scoreWord("lovely"))


# Note - add your code here if you completed the "Competency" option on the quiz
def topNWords(length, numWords):
        words = ["example", "lovely", "python", "coding"]  # Replace with actual word list
        filtered_words = [word for word in words if len(word) == length]  # Filter words by length
        scored_words = [(word, scoreWord(word)) for word in filtered_words]  # Calculate scores for each word
        scored_words.sort(key=lambda x: x[1], reverse=True)  # Sort by score in descending order
        nwords = scored_words[:numWords]  # Get the top N words
        return nwords
    
    # Example usage
print(topNWords(6, 2))  # Replace 6 and 3 with desired length and number of words


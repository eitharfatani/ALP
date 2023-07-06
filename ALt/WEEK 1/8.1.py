'''
In these tasks you will be given one or more examples of code.

- Look at each example , study it carefully.
- Write a prediction of what it will do when it runs. Your prediction should be added to the code as comments. You should use the key terms list, item and index in your predictions.
- Run the code, compare what happens to your prediction.
- Add comments to note down and differences between your prediction and what actually happened.

'''

# Example Code 1

Sentence = ["Always", "look", "on", "the", "bright", "side", "of",]
print(Sentence) #print the word that stored in the variable
print(Sentence[1]) #look is an item
Sentence.append("life") #life is added to the items
Sentence[4] = "sunny" #sunny gonna take bright place
print(Sentence[4]) #print sunny
print(Sentence[0] + " " + Sentence[3]) #sunny and a space are added and printed
print(Sentence) #print the sentence with changes
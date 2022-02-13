# Explantation
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"



# My solution:
def order(sentence):
    sentence_array = sentence.split(' ')
    dic = {}
    
    for word in sentence_array:
        for char in word:
            # Checks if the character is a number
            if char.isalpha():
                continue
            else: 
            # Creates a key:value pair, with number in word, and word 
            # example: ('lo4g': 4)
                dic[word] = int(char)
                
    #Sorting the previously creted DICTIONARY
    # we use the sorted function, that returns an array
    # For our iterable, we use dic.items() which returns a list of the given dictionary's (key, value) tuple pair.
    # We also specify the key parameter, this is a function that is applied to each element in the array for the sort comparison
    # in this case, the key will return the value of our dictionary, which contains a number, these numbers are used 
    # for the sorting. 
    # Once the sorting is done, a sorted array, containing the (key:value) tuple pair is returned.
    sorted_dic = sorted(dic.items(), key=lambda x: x[1])

    # Iterating through the sorted dictionary, and creating a list of keys
    answer = []
    for i in sorted_dic:
        answer.append(i[0])
    # Returning the list of keys as a sentence
    return ' '.join(answer)






# SIMPLE SOLUTION -- only works in this scenario

def order(sentence):
    if sentence != '':
    # function min will ignore all the characters, It's doing min on each word, which returns the smallest character which is always the digit.
        return ' '.join(sorted(sentence.split(' '), key=min))
    else:
        return ''


# Other solution:

def order(words):
# use sorted words that star with number for the key, then sort the sorted words to get final answer.
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))
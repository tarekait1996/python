import functools

#Problem 1
def word_lengths(phrase):
    words = phrase.split(" ")
    print(words)
    lengths = list(map(lambda x: len(x),words))
    print(lengths)

word_lengths('How long are the words in this phrase')

#problem 2

def digits_to_num(digits):
    length = len(digits)
    max = 10 **(length - 1)
    sum =0
    # method with reduce
    number = functools.reduce(lambda x,y: (x*10)+y,digits)
    #method with for loop
    for digit in digits :
        sum += digit * max
        max /= 10
    print(sum)
    print(number)

digits_to_num([3,4,3,2,1])

#problem 3

def filter_words(word_list,letter):
    new_list = list(filter(lambda x : x[0] == letter, word_list))
    return new_list
l = ['hello','are','cat','dog','ham','hi','go','to','heart']
new_list = filter_words(l,'h')
print(new_list)

#problem 4

def concatenate(L1,L2,connector):
    return [word1+connector+word2 for (word1,word2) in zip(L1,L2)]


print(concatenate(['A','B'],['a','b'],'-'))


'''
def concatenate(L1, L2, connector):
    
    pass

concatenate(['A','B'],['a','b'],'-')

['A-a', 'B-b']


'''
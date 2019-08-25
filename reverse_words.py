def reverse_words(string):
    words = string.split(" ")
    reverse = []
    length = len(words) - 1

    for word in words: 
        reverse.append(words[length])
        length -= 1

    output = ' '.join(reverse)
    print (output)
    

reverse_words( "popcorn is so cool isn't it yeah i thought so" )
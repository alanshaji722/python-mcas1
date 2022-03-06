#Alan Shaji
#21MCA002

def word_count(sto):
    counts = {}
    words = sto.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1


    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))

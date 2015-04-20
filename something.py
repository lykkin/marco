def most_common_char(li):
    colors = ['red', 'blue', 'green']
    freq = {}
    for word in li:
        if word in colors:
            for char in word:
                try:
                    freq[char] += 1
                except KeyError:
                    freq[char] = 1
    res, count = None, 0
    for char, occurances in freq.iteritems():
        if occurances > count:
            res, count = char, occurances
    return res

most_common_char(['red', 'blue', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'green'])

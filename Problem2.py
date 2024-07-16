def count_num(words):
    lst = []
    s = ""
    for _, v in enumerate(words):
        if v >= chr(97) and v <= chr(119):
            s += " "
        else:
            s += v
    lst = s.split(" ")
    words = []
    for i in lst:
        if i != '' and i.count("0") == 0:
            words.append(i)
    return (len(set(words)))

# words = "a12bc34d8ef34"
# words = "leet1234code234"
words = "a1b01c001"


print(count_num(words))

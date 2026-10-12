from collections import Counter
word = ["DBMS","Operating system","DBMS","Networking","python", "python","DBMS"]
word_count=Counter(word)
print("All counter",word_count)
print("Total no of time",word_count["DBMS"])
print("commo in All",word_count.most_common(1))
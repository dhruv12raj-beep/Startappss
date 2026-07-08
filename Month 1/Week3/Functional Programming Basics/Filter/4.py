# 28.	Filter words starting with 'a'.
words=['apple',
       'banana',
       'ant',
       'cat',
       'air']


filtered = list(filter(lambda x : x.startswith("a"), words))
print(filtered)
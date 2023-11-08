words = input().split()
word_to_count = dict()

for w in words:
    count = word_to_count.get(w, 0)
    print(count)
    word_to_count[w] = count + 1

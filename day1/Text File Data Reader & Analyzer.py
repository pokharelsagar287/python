# #Simple Beam Load Calculator

# length = float(input("Enter the span length of the beam in meters:"))
# load = float(input("\nEnter the load on the beam in kN: "))


# #calculation of maximun bending moment
# bending_moment = (load * length**2) / 8

# print("The maximum bending moment is: ", bending_moment, "kNm")
# Open and read the file
with open('notes.txt', 'r', encoding="utf-16") as file:
    # extract text from the file
    text = file.read()
    # convert text to lower text
    text = text.lower()
    import string
    for punct in string.punctuation:
        text = text.replace(punct, "")
#split the text into words
words = text.split()
total_words = len(words)
# count the number of unique words
unique_words = len(set(words))

#step 5 count word using dictionary
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

#step 6 find 5 most repeated word
sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
most_repeated_words = sorted_word_count[:5]

#print the results
print(f"Total number of words: {total_words}")
print(f"Total number of unique words: {unique_words}")
print("Most repeated words:")
for word, count in most_repeated_words:
    print(f"{word}: {count} times")

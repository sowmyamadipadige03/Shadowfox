from autocorrect_module import autocorrect_text
from next_word_predictor import build_trigrams, predict_next_word

# Step 1: Load training text from sample_corpus.txt
with open("sample_corpus.txt", "r") as file:
    corpus = file.read()

# Step 2: Autocorrect the corpus and build the trigram model
corrected_corpus = autocorrect_text(corpus)
trigrams = build_trigrams(corrected_corpus)

# Step 3: Get user input
user_input = input("Type a sentence: ")

# Step 4: Autocorrect user input
corrected_input = autocorrect_text(user_input)
print("\n Corrected Input:", corrected_input)

# Step 5: Predict next word using last 2 words
words = corrected_input.split()
if len(words) >= 2:
    prediction = predict_next_word(words[-2], words[-1], trigrams)
    print("Next Word Prediction:", prediction)
else:
    print("Please enter at least 2 words to get a next word prediction.")



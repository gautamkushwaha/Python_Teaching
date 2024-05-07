from enchant import DictWithPWL
from nltk.tokenize import word_tokenize

# Load dictionary
d = DictWithPWL("en_US")

def spell_check(text):
  # Preprocess text
  # Tokenize, convert to lowercase, etc.
  words = word_tokenize(text.lower())

  # Spell check each word
  changes = {}
  for word in words:
    if not d.check(word):
      suggestions = d.suggest(word)
      # Choose best suggestion based on your logic
      corrected_word = suggestions[0]
      changes[word] = corrected_word

  # Output corrected text with highlighted changes
  corrected_text = ""
  for word in words:
    if word in changes:
      corrected_text += f"<mark>{changes[word]}</mark>"
    else:
      corrected_text += word + " "

  # Print results
  print("Original text:", text)
  print("Corrected text:", corrected_text)
  print("Changes:", changes)

# Get user input
user_text = input("Enter text to spellcheck: ")

spell_check(user_text)

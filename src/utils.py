import string

# util for removing punctuation from strings
punctuation = string.punctuation
translator = str.maketrans("", "", punctuation)

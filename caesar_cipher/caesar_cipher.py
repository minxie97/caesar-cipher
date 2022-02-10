import re
from nltk.corpus import words, names

def encrypt(plain, key):
  encrypted = ""

  for char in plain:
    if re.match(r"[A-Z]", char):
      new_num = ((ord(char) + key - 65) % 26) + 65
    elif re.match(r"[a-z]", char):
      new_num = ((ord(char) + key - 97) % 26) + 97
    else:
      new_num = ord(char)
    encrypted += chr(new_num)

  return encrypted

def decrypt(plain, key):
  return encrypt(plain, -key)

def crack(plain):
  for key in range(0, 26):
    attempt = decrypt(plain, key)
    attempt_list = attempt.split()

    score = 0

    for word in attempt_list:
      word = re.sub(r"[^a-zA-Z]", "", word)
      if word.lower() in words.words() or word in names.words():
        score += 1
      if word == "":
        score += 1

    if score == len(attempt_list):
      return attempt
  return ""

import emoji
from art import *
import pyjokes as pj

# Task 1 - Emoji
a = 5
print(emoji.emojize(f'Python is a {a} :star2: language!', language='alias'))
print(emoji.emojize(f':lion: :crown:', language='alias'))
print(emoji.emojize(f':monkey: :genie: :princess: :heart: :man:', language='alias'))
print(emoji.emojize(f':white_flower:', language='alias'))
print(emoji.demojize("🧞"))

# Task 2 - Art printing
a = 7
tprint(f'Logiscool is {a} years old!')
art = text2art("Logiscool", font='block', decoration='barcode7')
print(art)

# Task 3 - Jokes
print(pj.get_joke())

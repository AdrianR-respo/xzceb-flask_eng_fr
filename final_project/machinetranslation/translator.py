'''
translator module

This module provides fuctions for translation natural languages.
Includes functions for translation from English to French and French to English.
'''

from deep_translator import MyMemoryTranslator

def english_to_french(text):
    '''Function translating from English to French'''
    translator = MyMemoryTranslator(source='en-GB',target='fr-FR')
    french_text = translator.translate(text)
    return french_text

TEXT = "Hello, how are you"
french_text = english_to_french(TEXT)
print(french_text)

english_to_french(TEXT)

print("\n")



def french_to_english(text):
    '''Function translating from French to English'''
    translator = MyMemoryTranslator(source='fr-FR',target='en-GB')
    english_text = translator.translate(text)
    return english_text

TEXT = "Je suis content, merci"
english_text = french_to_english(TEXT)
print(english_text)

french_to_english(TEXT)

print("\n")

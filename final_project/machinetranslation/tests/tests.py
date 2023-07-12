import unittest 
import requests


class TranslationTests(unittest.TestCase):
    def test_e2f_translation(self):
        english_to_french = "Hello, how are you"
        expected_french_text = "Bonjour, comment allez-vous"

        response = requests.get(f"https://api.mymemory.translated.net/get?q={english_to_french}&langpair=en-GB|fr-FR")
        translation = response.json()["responseData"]["translatedText"]

        self.assertEqual(translation, expected_french_text)
        self.assertNotEqual(translation, "Invalid translation")



    def test_f2e_translation(self):
        french_to_english = "Je suis content, merci"
        expected_english_text = "I'm happy, thank you"

        response = requests.get(f"https://api.mymemory.translated.net/get?q={french_to_english}&langpair=fr-FR|en-GB")
        translation = response.json()["responseData"]["translatedText"]

        self.assertEqual(translation, expected_english_text)
        self.assertNotEqual(translation, "Invalid translation")


if __name__ == '__main__':
    unittest.main()
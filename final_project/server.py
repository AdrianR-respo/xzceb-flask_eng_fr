from machinetranslation import translator
from flask import Flask, render_template, request
import json
from deep_translator import MyMemoryTranslator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench(text):
    textToTranslate = request.args.get('textToTranslate')
    # Write your code herein tin
    translator = MyMemoryTranslator(source='en-GB',target='fr-FR')
    french_text = translator.translate(text)
    return french_text & "Translated text to French"
    french_text = english_to_french(TEXT)
    print(french_text)

@app.route("/frenchToEnglish")
def frenchToEnglish(text):
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translator = MyMemoryTranslator(source='fr-FR',target='en-GB')
    english_text = translator.translate(text)
    return english_text & "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

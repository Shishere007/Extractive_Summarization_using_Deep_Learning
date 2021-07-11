from os import system

system("pip install -r requirements.txt")

import nltk

nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')
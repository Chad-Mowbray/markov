import re
import random

class MarkovGenerator:

    def __init__(self):
        self.lexicon = {}

    def read_file(self):
        with open("source.txt", "r") as f:
            text = f.read()
        return text
    
    def cleaner(self, word):
        word = word.lower()
        word = re.sub(r"[^a-z]", "", word)
        return word

    
    def get_clean_text(self, raw_text):
        words = raw_text.split(" ")
        cleaned = [self.cleaner(word) for word in words]
        filter_empty = [word for word in cleaned if word != ""]
        self.cleaned = filter_empty

    def build_lexicon(self):
        for i in range(len(self.cleaned) - 1):
            if self.cleaned[i] in self.lexicon:
                self.lexicon[self.cleaned[i]].append(self.cleaned[ i + 1])
            else:
                self.lexicon[self.cleaned[i]] = [self.cleaned[ i + 1]] 

    def generate_text(self, num_words):
        generated_text = ""
        current_word = "he"
        generated_text += current_word
        for _ in range(num_words + 1):
            next_word = random.choice(self.lexicon[current_word])
            generated_text += " " + next_word
            current_word = next_word
        return generated_text

    def run(self):
        raw_text = self.read_file()
        self.get_clean_text(raw_text)
        self.build_lexicon()


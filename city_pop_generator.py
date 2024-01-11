import pandas as pd
# Japanese morphological analysis engine
from janome.tokenizer import Tokenizer
import markovify

# Format the lyrics
def format_special_character(text):
    replace_chars = ['\\n', '\n', '\u3000', '・・・', '...', '(', ')', '「', '」', '…', '、', ',']
    for char in replace_chars:
        text = text.replace(char, '')
    text = text.replace(' ', '\n').replace('\n\n', '')
    return text

def generate_lyrics(text):
    # Create a new instance of the Tokenizer
    t = Tokenizer()

    # Split the text file in words
    words = t.tokenize(text, wakati = True)

    # Store the words in a list
    word_list = [word for word in words]

    # Stringify
    word_list_string = ' '.join(word_list)

    # Use NewLineText as there is no punctuation
    text_model = markovify.NewlineText(word_list_string, state_size=2)

    # Produce a sentence
    for i in range(11):
        print(f'----------------{i}----------------')
        sentence = text_model.make_sentence()
        if sentence == None:
            print('No sentence')
        else:
            print(sentence.replace(' ', ''))

df = pd.read_csv('lyrics.csv')
pd.set_option("display.max_colwidth", 1000)
string = df['lyrics'].to_string(index=False)

with open('lyrics.txt', 'w') as output_file:
    output_file.write(string)

with open('lyrics.txt', 'r') as file:
    text = file.read()

formatted_text = format_special_character(text)
generate_lyrics(formatted_text)
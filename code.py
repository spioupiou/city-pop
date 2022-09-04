import pandas as pd
# Japanese morphological analysis engine
from janome.tokenizer import Tokenizer
import markovify

df = pd.read_csv('lyrics.csv')
pd.set_option("display.max_colwidth", 1000)
string = df['lyrics'].to_string(index=False)

output_file = open('lyrics.txt', 'w')
output_file.write(string)
output_file.close()

# Format the lyrics
text_file = open('lyrics.txt', 'r')
text = text_file.read()

text = text.replace('\\n', ' ')
text = text.replace('\n', ' ')
text = text.replace('\u3000', '')

text = text.replace('・・・', '')
text = text.replace('...', '')
text = text.replace('...', '')
text = text.replace('(', '')
text = text.replace(')', '')
text = text.replace('「', '')
text = text.replace('」', '')
text = text.replace('…', '')
text = text.replace('、', '')
text = text.replace(',', '')
print(text)
text = text.replace(' ', '\n')
text = text.replace('\n\n', '')
print(text)
# Create a new instance of the Tokenizer
t = Tokenizer()

# Split the text file in words
words = t.tokenize(text, wakati = True)

# Store the words in a list
word_list = []
for i in words:
    word_list.append(i)

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

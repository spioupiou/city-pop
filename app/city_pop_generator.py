# Japanese morphological analysis engine
from janome.tokenizer import Tokenizer
import markovify


# Format the lyrics
def format_special_character(text):
    replace_chars = [
        "\\n",
        "\n",
        "\u3000",
        "・・・",
        "...",
        "(",
        ")",
        "「",
        "」",
        "…",
        "、",
        ",",
    ]
    for char in replace_chars:
        text = text.replace(char, "")
    text = text.replace(" ", "\n").replace("\n\n", "")
    return text


def generate_lyrics(text):
    # Create a new instance of the Tokenizer
    t = Tokenizer()

    # Split the text file in words
    words = t.tokenize(text, wakati=True)

    # Stringify
    word_list_string = " ".join([word for word in words])

    # Use NewLineText as there is no punctuation
    text_model = markovify.NewlineText(word_list_string, state_size=2)

    # Produce a sentence
    generated_lyrics = []

    for i in range(10):
        print(f"----------------{i+1}----------------")
        sentence = text_model.make_sentence()
        if sentence == None:
            print("No sentence")
        else:
            print(sentence.replace(" ", ""))
            generated_lyrics.append(sentence.replace(" ", ""))
    return generated_lyrics


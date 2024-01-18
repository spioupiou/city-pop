import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS
from city_pop_generator import format_special_character, generate_lyrics
import os

app = Flask(__name__)
CORS(app)

def load_data():
    df = pd.read_csv("data/lyrics.csv")
    pd.set_option("display.max_colwidth", 1000)
    string = df["lyrics"].to_string(index=False)

    with open("data/lyrics.txt", "w") as output_file:
        output_file.write(string)

@app.route("/api/v1", methods = ['GET'])
def generate():
    if not os.path.exists("data/lyrics.txt"):
        load_data()

    with open("data/lyrics.txt", "r") as file:
        text = file.read()

    formatted_text = format_special_character(text)
    generated_lyrics = generate_lyrics(formatted_text)
    return jsonify({"lyrics": generated_lyrics})


if __name__ == "__main__":
    app.run(host=os.getenv('HOST', '0.0.0.0'), debug=True, port=os.getenv("PORT", 8000))

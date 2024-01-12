import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS
from city_pop_generator import format_special_character, generate_lyrics

app = Flask(__name__)
CORS(app)


@app.route("/api/v1", methods = ['GET'])
def generate():
    df = pd.read_csv("lyrics.csv")
    pd.set_option("display.max_colwidth", 1000)
    string = df["lyrics"].to_string(index=False)

    with open("lyrics.txt", "w") as output_file:
        output_file.write(string)

    with open("lyrics.txt", "r") as file:
        text = file.read()

    formatted_text = format_special_character(text)
    generated_lyrics = generate_lyrics(formatted_text)
    return jsonify({"lyrics": generated_lyrics})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)

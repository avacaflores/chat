from flask import Flask, request, render_template
import ollama
import os

app = Flask(__name__)
ollama_host = os.environ.get('OLLAMA_HOST', 'http://localhost:11434')
client = ollama.Client(host=ollama_host)

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        message = request.form.get("message")
        response = client.chat(model='qwen2.5:0.5b', messages=[{'role': 'user', 'content': message}])
        bot_message = response.message.content
        return render_template("index.html", user_message=message, bot_message=bot_message)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
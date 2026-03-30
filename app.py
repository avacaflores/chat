from flask import Flask, request, render_template
import ollama

app = Flask(__name__)
client = ollama.Client(host='http://localhost:11434')

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
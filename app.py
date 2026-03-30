from flask import Flask, render_template, request
import ollama

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_message = request.form['message']
        response = ollama.chat(model='qwen2.5:0.5b', messages=[{'role': 'user', 'content': user_message}])
        bot_message = response['message']['content']
        return render_template('index.html', user_message=user_message, bot_message=bot_message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
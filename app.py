from flask import Flask, render_template, request
import openai
openai.api_key = "api_key"

app = Flask(__name__)
app.static_folder = 'static'
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    output = openai.Completion.create(
        engine="text-davinci-003",
        prompt=userText,
        temperature=0.7,
        max_tokens=2000,
        n=1,
        stop=None,
    )    
    return output.choices[0].text
if __name__ == "__main__":
    app.run()




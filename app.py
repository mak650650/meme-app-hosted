from flask import Flask, render_template, request
import get_meme

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def home():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        return render_template("greet.html", name=request.form.get("name","World"))


@app.route('/meme', methods=["POST"])
def meme_func():
    meme_pic, subreddit = get_meme.get_meme()
    return render_template("show_meme.html", meme_pic=meme_pic, subreddit=subreddit)

if __name__ =="__main__":
    app.run(debug=True ,host="0.0.0.0")

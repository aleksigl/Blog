from flask import render_template
from blog import app
from blog.models import Entry, db

app.config["SECRET_KEY"] = "qwerty"


@app.route("/")
def index():
    all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc())
    return render_template("homepage.html", all_posts=all_posts)



if __name__ == "__main__":
    app.run(debug=True)


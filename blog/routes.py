from flask import render_template, request, flash, redirect, url_for
from blog import app
from blog.models import Entry, db
from blog.forms import EntryForm

app.config["SECRET_KEY"] = "qwerty"


@app.route("/")
def index():
    all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc())
    return render_template("homepage.html", all_posts=all_posts)


@app.route("/new-post/", methods=["GET", "POST"])
def create_entry():
    form = EntryForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            try:
                entry = Entry(
                    title=form.title.data,
                    body=form.body.data,
                    is_published=form.is_published.data
                )
                db.session.add(entry)
                db.session.commit()
                flash('Twój post został opublikowany.', 'success')
                return redirect(url_for("index"))
            except Exception as e:
                db.session.rollback()
                error = str(e)
    entries = Entry.query.all()
    return render_template("entry_form.html", form=form, entries=entries, error=error)


@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
def edit_entry(entry_id):
    entry = Entry.query.filter_by(id=entry_id).first_or_404()
    form = EntryForm(obj=entry)
    print(f"Title: {form.title}")
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            try:
                form.populate_obj(entry)
                db.session.commit()
                flash('Twoje zmiany zostały opublikowane.', 'success')
                return redirect(url_for("index"))
            except Exception as e:
                db.session.rollback()
                error = str(e)
    entries = Entry.query.all()
    return render_template("entry_form.html", form=form, entries=entries, error=error)


if __name__ == "__main__":
    app.run(debug=True)


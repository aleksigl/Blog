from flask import render_template, request, flash, redirect, url_for
from blog import app
from blog.models import Entry, db
from blog.forms import EntryForm

app.config["SECRET_KEY"] = "qwerty"


@app.route("/")
def index():
    all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc())
    return render_template("homepage.html", all_posts=all_posts)


def manage_entry(entry_id=None):
    entry = None
    error = ""
    if entry_id:
        entry = Entry.query.get_or_404(entry_id)

    form = EntryForm(obj=entry)

    if request.method == "POST":
        if form.validate_on_submit():
            try:
                if entry:
                    form.populate_obj(entry)
                    flash('Twoje zmiany zostały opublikowane.', 'success')
                else:
                    entry = Entry(
                        title=form.title.data,
                        body=form.body.data,
                        is_published=form.is_published.data
                    )
                    db.session.add(entry)
                    flash('Twój post został opublikowany.', 'success')
                db.session.commit()
                return redirect(url_for("index"))
            except Exception as e:
                db.session.rollback()
                error = f"Błąd: {str(e)}"
                flash(error, 'danger')
    entries = Entry.query.all()
    return render_template("entry_form.html", form=form, entries=entries, error=error)


@app.route("/new-post/", methods=["GET", "POST"])
def create_entry():
    return manage_entry()


@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
def edit_entry(entry_id):
    return manage_entry(entry_id)


if __name__ == "__main__":
    app.run(debug=True)


from flask import render_template, request, flash, redirect, url_for, session
from blog import app
from blog.models import Entry, db
from blog.forms import EntryForm, LoginForm
import functools


app.config["SECRET_KEY"] = "qwerty"


def login_required(view_func):
    @functools.wraps(view_func)
    def check_permissions(*args, **kwargs):
        if session.get('logged_in'):
            return view_func(*args, **kwargs)
        return redirect(url_for('login', next=request.path))
    return check_permissions


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


@app.route("/")
def index():
    all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc())
    return render_template("homepage.html", all_posts=all_posts)


@app.route("/new-post/", methods=["GET", "POST"])
@login_required
def create_entry():
    return manage_entry()


@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
@login_required
def edit_entry(entry_id):
    return manage_entry(entry_id)


@app.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    errors = None
    next_url = request.args.get('next')
    if request.method == 'POST':
        if form.validate_on_submit():
            session['logged_in'] = True
            session.permanent = True
            flash('You are now logged in.', 'success')
            return redirect(next_url or url_for('index'))
        else:
            errors = form.errors
    return render_template("login_form.html", form=form, errors=errors)


@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        session.clear()
        flash('You are now logged out.', 'success')
    return redirect(url_for('index'))


@app.route('/drafts/', method=['GET'])
@login_required
def list_drafts():
    drafts = Entry.query.filter_by(is_published=False).order_by(Entry.pub_date.desc())
    return render_template("homepage.html", drafts=drafts)


if __name__ == "__main__":
    app.run(debug=True)


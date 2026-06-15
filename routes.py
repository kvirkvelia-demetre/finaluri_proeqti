from ext import app, db
from flask import render_template, redirect, flash, request
from forms import RegisterForm, BookForm, LoginForm, CommentForm
from models import Book, User, Comment
from flask_login import login_user, logout_user, login_required, current_user
from os import path


@app.route("/")
def home():
    query = request.args.get("search")
    if query:
        books = Book.query.filter(Book.title.ilike(f"%{query}%")).all()
    else:
        books = Book.query.all()
    return render_template("index.html", books=books, role="admin")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            flash("This username is already taken")
            return redirect("/register")


        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@app.route("/add_book", methods=["GET", "POST"])
@login_required
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        new_book = Book(
            title=form.title.data,
            release_year=form.release_year.data,
            author=form.author.data,
            genre=form.genre.data,
            description=form.description.data
        )
        img = form.image.data
        new_book.image = img.filename
        if img:
            directory = path.join(app.root_path, "static", "images", img.filename)
            img.save(directory)
        new_book.create()
        return redirect("/")
    return render_template("add_book.html", form=form)


@app.route("/update_book/<int:book_id>", methods=["GET", "POST"])
@login_required
def update_book(book_id):
    book = Book.query.get(book_id)
    form =BookForm(title=book.title, release_year=book.release_year)
    if form.validate_on_submit():
        book.title = form.title.data
        book.release_year = form.release_year.data
        image = form.image.data
        if image:
            directory = path.join(app.root_path, "static", "images", image.filename)
            image.save(directory)
            book.image = image.filename

        book.save()
        return redirect("/")
    return render_template("add_book.html", form=form)



@app.route("/delete_book/<int:book_id>")
@login_required
def delete_book(book_id):
    book = Book.query.get(book_id)
    book.delete()
    return redirect("/")


@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/book/<int:book_id>", methods=["GET", "POST"])
@login_required
def book_details(book_id):
    book = Book.query.get_or_404(book_id)
    form = CommentForm()

    if form.validate_on_submit():
        new_comment = Comment(
            comment=form.comment.data,
            book_id=book.id,
            user_id=current_user.id
        )
        db.session.add(new_comment)
        db.session.commit()
        return redirect(f"/book/{book_id}")

    comments = Comment.query.filter_by(book_id=book.id).all()
    return render_template("book_details.html", book=book, comments=comments, form=form)
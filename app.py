from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from models import db, User, Post
from forms import RegisterForm, LoginForm, PostForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '1420'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def index():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template("index.html", posts=posts)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data.strip()).first():
            flash("Username already exists!", "warning")
            return redirect(url_for("register"))
        user = User(
            username=form.username.data.strip(),
            password=generate_password_hash(form.password.data.strip())
        )
        db.session.add(user)
        db.session.commit()
        flash("Registration successful! Please log in.", "success")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data.strip()).first()
        if user and check_password_hash(user.password, form.password.data.strip()):
            login_user(user)
            flash("Logged in successfully!", "success")
            next_page = request.args.get("next")
            return redirect(next_page or url_for("index"))
        flash("Invalid username or password", "danger")
    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have logged out.", "info")
    return redirect(url_for("index"))

@app.route("/post/new", methods=["GET", "POST"])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data.strip(),
                    content=form.content.data.strip(),
                    author_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash("Post created!", "success")
        return redirect(url_for("index"))
    return render_template("new_post.html", form=form)

@app.route("/post/<int:post_id>")
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post.html", post=post)

@app.route("/post/<int:post_id>/edit", methods=["GET", "POST"])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author_id != current_user.id:
        flash("You cannot edit this post!", "danger")
        return redirect(url_for("post_detail", post_id=post.id))

    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data.strip()
        post.content = form.content.data.strip()
        db.session.commit()
        flash("Post updated!", "success")
        return redirect(url_for("post_detail", post_id=post.id))
    return render_template("new_post.html", form=form)

@app.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author_id != current_user.id:
        flash("You cannot delete this post!", "danger")
        return redirect(url_for("post_detail", post_id=post.id))

    db.session.delete(post)
    db.session.commit()
    flash("Post deleted!", "info")
    return redirect(url_for("index"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)


#python -m venv venv
#venv\Scripts\activate
#pip install flask flask_sqlalchemy flask_login flask_wtf wtforms werkzeug
#pip freeze > requirements.txt
#python app.py

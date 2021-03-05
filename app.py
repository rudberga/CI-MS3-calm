import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

# Landing page
@app.route("/")
@app.route("/get_home")
def get_home():
    return render_template("index.html")


# Get artists and genres functionality
@app.route("/get_artists")
def get_artists():
    artists = list(mongo.db.artists.find())
    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("artists.html", artists=artists, genres=genres)


# Search functionality
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    artists = list(mongo.db.artists.find({"$text": {"$search": query}}))
    return render_template("artists.html", artists=artists)


# Sign up functionality
@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # Check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exist, try another one!")
            return redirect(url_for("sign_up"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Put new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile",username=session["user"]))
    return render_template("index.html")


# Log in functionality
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    return redirect(url_for(
                        "profile",username=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Username does not exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    
    return render_template("index.html")


# Profile page functionality
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    artists = list(mongo.db.artists.find())
    # Grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template(
            "profile.html", username=username, artists=artists)

    return redirect(url_for("login"))


# Log out functionality
@app.route("/logout")
def logout():
    # Remove user from session cookie
    flash("You have been logged out!")
    session.pop("user")
    return redirect(url_for("get_home"))


# Add artist functionality
@app.route("/add_artist", methods=["GET", "POST"])
def add_artist():
    if request.method == "POST":
        vocals = "on" if request.form.get("vocals") else "off"
        artist = {
            "genre_name": request.form.get("genre_name"),
            "artist_name": request.form.get("artist_name"),
            "nationality": request.form.get("nationality"),
            "vocals": vocals,
            "image": request.form.get("image"),
            "spotify": request.form.get("spotify"),
            "created_by": session["user"]
        }
        mongo.db.artists.insert_one(artist)
        flash("Artist Successfully Added")
        return redirect(url_for("get_artists"))

    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("artists.html", genres=genres)


# Edit artist functionality
@app.route("/edit_artist/<artist_id>", methods=["GET", "POST"])
def edit_artist(artist_id):
    if request.method == "POST":
        vocals = "on" if request.form.get("vocals") else "off"
        submit = {
            "genre_name": request.form.get("genre_name"),
            "artist_name": request.form.get("artist_name"),
            "nationality": request.form.get("nationality"),
            "vocals": vocals,
            "image": request.form.get("image"),
            "spotify": request.form.get("spotify"),
            "created_by": session["user"]
        }
        mongo.db.artists.update({"_id": ObjectId(artist_id)}, submit)
        flash("Artist Successfully Updated!")
        return redirect(url_for("get_artists"))

    artist = mongo.db.artists.find_one({"_id": ObjectId(artist_id)})
    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("edit_artist.html", artist=artist, genres=genres)


# Delete artist functionality
@app.route("/delete_artist/<artist_id>")
def delete_artist(artist_id):
    mongo.db.artists.remove({"_id": ObjectId(artist_id)})
    flash("Artist Successfully Deleted")
    return redirect(url_for("get_artists"))

# Add e-mail to db for newsletter functionality
@app.route("/newsletter", methods=["GET", "POST"])
def add_newsletter():
    if request.method == "POST":
        # Check if e-mail is already registered
        existing_email = mongo.db.newsletters.find_one(
            {"email": request.form.get("email").lower()})

        if existing_email:
            flash("Your E-mail is already subscribed!")
            return redirect(url_for("get_home"))

        email = {
            "email": request.form.get("email"),
        }
        mongo.db.newsletters.insert_one(email)
        flash("Successfully subscribed!")
        return redirect(url_for("get_home"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # CHANGE THIS TO "False" WHEN DEPLOYING PROJECT
            debug=True)

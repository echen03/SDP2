#Team Baguette Grabbers
#huangT, chenE, linW, wuJ
#SoftDev1 pd2
#P #02: The End
#2019-1-??

from flask import Flask, render_template, request,  session, redirect, url_for, flash
import sqlite3
import urllib, json
import db as dbase  #helper functions found in db.py
app = Flask(__name__)
app = Flask(__name__)
app.secret_key = "adsfgt"

session = {}
userInfo = {}

@app.route("/") #Initally loaded page
def root():
    if 'user' in session:
        return redirect(url_for("home"))
    else:
        return render_template("index.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    return render_template("login.html")

@app.route("/register", methods = ["POST", "GET"])
def register():
    return render_template("register.html")

@app.route("/update", methods = ["POST", "GET"]) #The page accessed to update your own data
def update():
    return render_template("update.html")

@app.route("/auth", methods = ["POST"]) #This route authenticates registration and log in, and other updates
def auth():
    if request.form['submit_button'] == "Sign me up": #If you were sent here by registering
        if dbase.addUser():
            return redirect(url_for("root"))
        else:
            return redirect(url_for("register")) #if addUser() returns false, it will also handle flashing the correct error message
    if request.form['submit_button'] == "Login": #if sent here by logging in
        if dbase.login():
            session['user'] = request.form['username'] #stores the user in the session
            dbase.fillUserInfo(userInfo) #gives easy access to user information via userInfo variable
            return redirect(url_for("home"))
        else:
            return redirect(url_for("login"))
    if request.form['submit_button'] == "Update Info": #If updating info, fill in db
        dbase.update()
        dbase.fillUserInfo(userInfo) #gives easy access to user information via userInfo variable
        return redirect(url_for("home"))
    if request.form['submit_button'] == "Update Key" or request.form['submit_button'] == "Add Key":
        dbase.updateAPIKey(request.form['submit_button'])
        return redirect(url_for("home"))

@app.route("/logout")
def logout():
    if 'user' in session:
        session.pop('user')
        dbase.userID = -1
    flash("Logout Success!")
    flash("index")
    return redirect(url_for("root"))


@app.route("/home")
def home():
    if 'user' not in session:
        return redirect(url_for("login"))
    user = session['user]
    list_of_games = db_manager.getGames()
    return render_template("home.html", user = user, list_of_games = list_of_games)

@app.route("/games-info/<game>")
def info(game):
    if 'user' not in session:
        return redirect(url_for("login"))
    user = session["username"]
    description = db_manager.getDescription(game)
    how_to_play = db_manager.getHtoP(game)
    image = db_manager.getImage(game)
    return render_template("games-info.html", user = user, description = description, how_to_play = how_to_play)

@app.route("/sudoku")
def sudoku():
    if 'user' not in session:
        return redirect(url_for("login"))
    return redirect(url_for("play-sudoku"))

if __name__ == "__main__":
    app.debug = True
    app.run()

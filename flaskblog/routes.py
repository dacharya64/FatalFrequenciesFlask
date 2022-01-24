from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post



posts = [ 
    {
        "tag": "sadies_sob_story",
        "name": "Sadie's Sob Story"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

 # "player_visited": false,
 #        "lead-outs": [
 #            "what_the_cops_know",
 #            "fullers_electrical_repair",
 #            "the_peculiar_death_of_myron_fink"
 #        ],
 #        "description": [
 #            "The scenario starts off for Vivian Sinclair on a Monday morning after she’s turned in her most recent story. Invite the player to describe it, if she likes. She may rest on her laurels and joke around with the guys in the Herald Tribune’s newsroom, or she may already be scouring a pile of newspaper clippings and notes for her next lead. Around 9 a.m., she gets a telephone call from downstairs.",
 #            "Use this as an opportunity to establish Viv’s newsroom and how she meets with interested parties. Does she have the receptionist send them up to her desk in a smoky room full of (mostly) men bent over typewriters and paper-strewn desks? Or does she meet with her Sources and sometime- clients in another location, such as a restaurant across the street? Have the player take a moment to describe something important that Viv keeps at her desk in the newsroom, or her regular order at the restaurant."
 #        ],
 #        "clues": {
 #            "Someone in George’s apartment building was murdered the day before he disappeared. She gives an address and third-story apartment number near the Brooklyn Navy Yard.": "false",
 #            "George went to work the next day, but no one’s seen him since. That was Thursday. He didn’t come to work Friday and wasn’t in his building.": "false"
 #        },
 #        "characters": ["sadie_cain"]
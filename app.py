from enum import unique
from wsgiref.validate import validator
from xmlrpc.client import boolean
from flask import Flask, jsonify, request, render_template, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from decouple import config
from distutils.util import strtobool
from db_utils import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'db_data/database.db'
Bootstrap(app)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

class LoginForm(FlaskForm):
    username = StringField('Användarnamn', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Lösenord', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Kom ihåg')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Ogiltig epost'), Length(max=50)])
    username = StringField('Användarnamn', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Lösenord', validators=[InputRequired(), Length(min=8, max=80)])

''' Page routes '''

@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def home():
    return render_template('home.html', title='Hem', avg_points=get_round_avg_points(round_id=0), \
        # my_points=get_round_your_points(round_id=0, team_id=1), highest_points=get_round_highest_points(round_id=0))
        my_points=10, highest_points=get_round_highest_points(round_id=0))

@app.route("/my-team")
def myTeam():
    return render_template('myTeam.html', title='Ta ut lag för nästa omgång', players=get_team_players(team_id=2))

@app.route("/transfers")
def transfers():
    # Add team_players=[] below
    return render_template('transfers.html', title='Övergångar', players=get_players(), round=get_current_round(), deadline=left_to_deadline(deadline='2022-09-20 17:59:59'))

@app.route('/points', methods=['GET'])
def points():
    return render_template('points.html', title='Poäng', players=get_team_players(team_id=2))

@app.route('/leagues', methods=['GET'])
def leagues():
    return render_template('leagues.html', title='Ligor')

@app.route('/games', methods=['GET'])
def games():
    return render_template('games.html', title='Matcher', games=get_games(), round=get_current_round(), deadline=left_to_deadline(deadline='2022-09-20 17:59:59'))

@app.route('/stats', methods=['GET'])
def stats():
    return render_template('stats.html', title='Statistik', player_stats=get_player_stats())

@app.route('/prizes', methods=['GET'])
def prizes():
    return render_template('prizes.html', title='Priser')

@app.route('/rules', methods=['GET'])
def api_get_rules():
    return render_template('rules.html', title='Regler', events=get_events())

@app.route('/about', methods=['GET'])
def api_get_about():
    return render_template('about.html', title='Om oss')

@app.route('/transfer-history', methods=['GET'])
def api_get_transfer_history():
    return render_template('transferHistory.html', title='Övergångshistorik')

@app.route('/transfer-planner', methods=['GET'])
def transfer_planner():
    return render_template('transferPlanner.html', title='Transfer Planner')



''' API's '''

@app.route('/api/players', methods=['GET'])
def api_players():
    position = request.args.get('position')
    club = request.args.get('club')
    if position == '':
        position = None
    if club == '':
        club = None
    return jsonify(get_players(position=position, club=club))

@app.route('/api/players/<player_id>', methods=['GET'])
def api_getplayer(player_id):
    return jsonify(get_player_by_id(player_id))

@app.route('/api/games', methods=['GET'])
def api_games():
    return jsonify(get_games())

@app.route('/api/team-players', methods=['GET'])
def api_starts():
    return jsonify(get_team_players())

@app.route('/api/users', methods=['GET'])
def api_get_users():
    return jsonify(get_users())

@app.route('/api/users/<user_id>', methods=['GET'])
def api_get_user(user_id):
    return jsonify(get_user_by_id(user_id))

@app.route('/api/users/add',  methods = ['POST'])
def api_add_user():
    user = request.get_json()
    return jsonify(insert_user(user))

@app.route('/api/users/delete/<user_id>',  methods = ['DELETE'])
def api_delete_user(user_id):
    return jsonify(delete_user(user_id))

@app.route('/api/users/update',  methods = ['PUT'])
def api_update_user():
    user = request.get_json()
    print(request.data)
    return jsonify(update_user(user))


''' SIGNUP, LOGIN and LOGOUT '''

@app.route('/sign-up', methods=['GET', 'POST'])
def signup():
        form = RegisterForm()
        if form.validate_on_submit():
            return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'
    # if request.method == 'POST':
    #     email = request.form.get('email')
    #     firstName = request.form.get('firstName')
    #     password1 = request.form.get('password1')
    #     password2 = request.form.get('password2')

    #     if len(email) < 4:
    #         flash('Ange en giltig email', category="error")
    #     elif len(firstName) < 2:
    #         flash('Namen måste var längre än 1 bokstav', category="error")
    #     elif password1 != password2:
    #         flash('Lösenorden matchar inte', category="error")
    #     elif len(password1) < 7:
    #         flash('Lösenordet är för kort. Välj ett lösenord som är minst 7 tecken', category="error")
    #     else:
    #         flash('Du är nu registrerad och kan logga in.', category="success")
        return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'
    # data = request.form
    # print(data)
    return render_template('login.html', form=form)




''' Mixed '''

@app.route('/clubs', methods=['GET'])
def api_get_clubs():
    return render_template('clubs.html', title='Klubbar', teams=get_clubs())

@app.route('/teams', methods=['GET'])
def api_get_teams():
    return render_template('teams.html', title='Lag', teams=get_teams())





if __name__ == '__main__':
    app.debug = strtobool(config('DEBUG'))
    app.run()
import json
from flask import Flask,render_template,request,redirect,flash,url_for
from exceptions import EmailNotFound, NotEnoughPoints

def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions

def getClubByEmail(email, clubs):
    try:
        club = [club for club in clubs if club['email'] == email][0]
    except IndexError:
        raise EmailNotFound()
    return club

def checkPlacesRequired(places_required, points_club):
    if places_required > points_club:
        raise NotEnoughPoints()
    return places_required

app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    try:
        club = getClubByEmail(request.form['email'], clubs)
        return render_template('welcome.html', club=club, competitions=competitions)
    except EmailNotFound as e:
        error = e.msg
    return render_template('index.html', error=error)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    try:
        placesRequired = checkPlacesRequired(int(request.form['places']), int(club['points']))
        competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
        flash('Great-booking complete!')
        return render_template('welcome.html', club=club, competitions=competitions)
    except NotEnoughPoints as e:
        error = e.msg
    return render_template('booking.html', club=club, competition=competition, error=error)



# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
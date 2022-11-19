import sqlite3
from decouple import config
import datetime

def connect_to_db():
    conn = sqlite3.connect(config('DB_PATH'))
    mycursor = conn.cursor()
    mycursor.execute("PRAGMA foreign_keys = ON;")
    return conn



''' 1. USERS FUNCTIONS ''' 

def insert_user(user):
    inserted_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name, email, phone, address, country) VALUES (?, ?, ?, ?, ?)", (user['name'], user['email'], user['phone'], user['address'], user['country']) )
        conn.commit()
        inserted_user = get_user_by_id(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_user


def get_users():
    users = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            user = {}
            user["user_id"] = i["user_id"]
            user["name"] = i["name"]
            user["email"] = i["email"]
            user["phone"] = i["phone"]
            user["address"] = i["address"]
            user["country"] = i["country"]
            users.append(user)

    except:
        users = []

    return users


def get_user_by_id(user_id):
    user = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        row = cur.fetchone()

        # convert row object to dictionary
        user["user_id"] = row["user_id"]
        user["name"] = row["name"]
        user["email"] = row["email"]
        user["phone"] = row["phone"]
        user["address"] = row["address"]
        user["country"] = row["country"]
    except:
        user = {}

    return user


def update_user(user):
    updated_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE users SET name = ?, email = ?, phone = ?, address = ?, country = ? WHERE user_id =?", (user["name"], user["email"], user["phone"], user["address"], user["country"], user["user_id"]))
        conn.commit()
        #return the user
        updated_user = get_user_by_id(user["user_id"])

    except:
        conn.rollback()
        updated_user = {}
    finally:
        conn.close()

    return updated_user


def delete_user(user_id):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from users WHERE user_id = ?", (user_id,))
        conn.commit()
        message["status"] = "User deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete user"
    finally:
        conn.close()

    return message


''' 2. CLUBS FUNCTIONS '''

def get_clubs():
    clubs = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM clubs")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            club = {}
            club["club_id"] = i["club_id"]
            club["name"] = i["name"]
            clubs.append(club)

    except:
        clubs = ['no clubs']

    return clubs


''' 3. PLAYERS FUNCTIONS '''

def insert_players(players):
    inserted_players = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("""INSERT INTO players (first_name, last_name, club_id, position, price)  
                    VALUES (?, ?, ?, ?, ?)""", (players['first_name'], players['last_name'], players['club_id'], players['position'], players['price']))
        conn.commit()
        inserted_players = get_players_by_id(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_players

def get_players(position=None, club=None):
    players = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        q = 'SELECT * FROM players'
        if position == None and club == None:
            pass
        elif position != None and club != None:
            # add validation check, try-except and send back complete list if errror
            q = q + f" WHERE position = '{position}' AND club_id = '{club}'"
        else:
            filts = []
            if position != None:
                filts.append(f"position = '{position}'")
            if club != None:
                filts.append(f"club_id = '{club}'")
            if len(filts) == 1:
                q = q + " WHERE " + filts[0]
            else:
                q = q + " WHERE " + filts[0]
                for i in filts[1:]:
                    q = q + " AND " + i
        
        cur.execute(q)

        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            player = {}
            player["player_id"] = i["player_id"]
            player["first_name"] = i["first_name"]
            player["last_name"] = i["last_name"]
            player["club_id"] = i["club_id"]
            player["position"] = i["position"]
            player["price"] = i["price"]
            players.append(player)

    except:
        players = ['no players with this filter']

    return players

def get_players_by_id(player_id, first_name, last_name, club_id, position, price):
    players = {
            'players':[
                {
                    'player_id':100,
                    'first_ name':'Daniel',
                    'first_ name':'Paulson',
                    'club_id':'ÖIS',
                    'position':'Mittfältare',
                    'price':4.5,
                },
                {
                    'player_id':101,
                    'first_ name':'Andrew',
                    'first_ name':'Mills',
                    'club_id':'ÖFK',
                    'position':'Målvakt',
                    'price':5.5,
                }
            ]
    }

def update_player(player_id):
    updated_player = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(f"UPDATE players SET club_id = 'SAIK', price = 8.5 WHERE player_id = '{player_id}'")
        conn.commit()
        #return the player
        updated_player = get_player_by_id(player_id)
        print('player updated')

    except:
        conn.rollback()
        updated_player = {}
        print('failed to update')
    finally:
        conn.close()

    return updated_player

def delete_player(player_id):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from players WHERE player_id = ?", (player_id,))
        conn.commit()
        message["status"] = "players deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete players"
    finally:
        conn.close()

    return message

def get_player_by_id(player_id):
    player = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM players WHERE player_id = ?", (player_id))
        row = cur.fetchone()
        # convert row objects to dictionary
        for i in row:
            player["player_id"] = i["player_id"]
            player["first_name"] = i["first_name"]
            player["last_name"] = i["last_name"]
            player["club_id"] = i["club_id"]
            player["position"] = i["position"]
            player["price"] = i["price"]
    except:
        player = {}

    return player


'''4. EVENTS FUNCTIONS '''

def get_events():
    events = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM events")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            event = {}
            event["event_id"] = i["event_id"]
            event["name"] = i["name"]
            event["points"] = i["points"]
            events.append(event)

    except:
        events = ['no events']

    return events


'''5. GAMES FUNCTIONS '''

def get_games():
    # need error checks
    games = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM games")

        rows = cur.fetchall()

    #     # convert row object to dictionary
        for i in rows:
            game = {}
            game["game_id"] = i["game_id"]
            game["competition_id"] = i["competition_id"]
            game["home_team"] = i["home_team"]
            game["away_team"] = i["away_team"]
            game["home_goals"] = i["home_goals"]
            game["away_goals"] = i["away_goals"]
            game["round_id"] = i["round_id"]
            game["date"] = i["date"]
            game["kick_off"] = i["kick_off"]
            games.append(game)
    except:
        games = {}

    return games

def get_games_by_id(round_number, competition_id):
    games = {
            'deadline':'29 Aug',
            'games':[
                {
                    'home_team':'AIK',
                    'away_team':'Hammarby IF',
                    'result':'1-0',
                    'date':'30 Aug',
                    'avsparkstid':'19:00'
                },
                {
                    'home_team':'Malmö FF',
                    'away_team':'Djurgårdens IF',
                    'result':'1-1',
                    'date':'31 Aug',
                    'avsparkstid':'19:00'
                }
            ]
    }
    # try:
    #     # conn = connect_to_db()
    #     # conn.row_factory = sqlite3.Row
    #     # cur = conn.cursor()
    #     # cur.execute("SELECT * FROM games WHERE games_id = ?", (player_id,))
    #     # row = cur.fetchone()

    #     # convert row object to dictionary
    #     games["deadline"] = '29 Aug'
    #     games["matches"] = 'AIK'
    #     games["last_name"] = i["last_name"]
    #     games["position"] = i["position"]
    #     games["price"] = i["price"]
    #     games["club_id"] = i["club_id"]
    #     games["competition_id"] = i["competition_id"]
    # except:
    #     games = {}

    return games


''' 6. TEAM functions '''

def get_teams():
    # need error checks
    teams = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM teams")

        rows = cur.fetchall()

    #     # convert row object to dictionary
        for i in rows:
            team = {}
            team["team_id"] = i["team_id"]
            team["user_id"] = i["user_id"]
            team["competition_id"] = i["competition_id"]
            team["name"] = i["name"]
            team["round_id"] = i["round_id"]
            team["points"] = i["points"]
            teams.append(team)
    except:
        teams = {}

    return teams

def get_team_players(team_id=2):
    players = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM team_players INNER JOIN players ON players.player_id = team_players.player_id WHERE team_players.team_id = 1;")
        rows = cur.fetchall()
        # convert row objects to dictionary
        for i in rows:
            player = {}
            player["team_players_id"] = i["team_players_id"]
            player["team_id"] = i["team_id"]
            player["player_id"] = i["player_id"]
            player["start"] = i["start"]
            player["first_name"] = i["first_name"]
            player["last_name"] = i["last_name"]
            player["club_id"] = i["club_id"]
            player["position"] = i["position"]
            player["price"] = i["price"]
            players.append(player)

    except:
        players = ['no players with this filter']

    return players

def update_team_players(team_id=2, players=[]):
    player_ids = []
    for player in players:
        print(player['player_id'])
        player_ids.append(player['player_id'])
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(f"UPDATE team_players ")
        rows = cur.fetchall()
        # convert row objects to dictionary
        for i in rows:
            player = {}
            player["team_players_id"] = i["team_players_id"]
            player["team_id"] = i["team_id"]
            player["player_id"] = i["player_id"]
            player["start"] = i["start"]
            player["first_name"] = i["first_name"]
            player["last_name"] = i["last_name"]
            player["club_id"] = i["club_id"]
            player["position"] = i["position"]
            player["price"] = i["price"]
            players.append(player)

    except:
        players = ['no players with this filter']

    return players

def validFormations(formation):
    # function that checks if formation is valid. This is done when picking starting11 and after round when substitutes are changed.
    pass


''' COMPETITION functions '''

def get_competitions():
    # need error checks
    competitions = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM competitions")

        rows = cur.fetchall()

    #     # convert row object to dictionary
        for i in rows:
            competition = {}
            competition["competition_id"] = i["competition_id"]
            competition["name"] = i["name"]
            competitions.append(competition)
    except:
        competitions = {}

    return competitions


''' 7 Functions to be executed after each round is finished '''

def updateStartPlayers():
    # execute this function after each round to update the starting 11 in each team. Either manually or automatically on a trigger.
    # if any player has not played, switch with subs1, if no minutes, switch with subs 2 etc.
    pass

def updatePoints():
    pass

def updateGameResults():
    pass

''' Other functions '''

def get_current_round():
    return 2

def left_to_deadline(deadline='2022-09-20 17:59:59'):
    current_time = datetime.datetime.now()
    deadline = datetime.datetime.strptime(deadline, '%Y-%m-%d %H:%M:%S')
    time_left = deadline-current_time
    print(type(current_time), type(deadline), type(time_left))
    day = time_left // datetime.timedelta(days=1)
    rest = time_left % datetime.timedelta(days=1)
    hour = rest // datetime.timedelta(hours=1)
    rest = rest % datetime.timedelta(hours=1)
    minute = rest // datetime.timedelta(minutes=1)
    rest = rest % datetime.timedelta(minutes=1)
    second = rest // datetime.timedelta(seconds=1)
    rest = rest % datetime.timedelta(seconds=1)
    return f"{day} dagar {hour} timmar {minute} minuter {second} sekunder"

def get_round_avg_points(round_id=0):
    # need error checks
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(f"SELECT avg(points) FROM teams WHERE round_id = '{round_id}'")

        rows = cur.fetchall()
        # convert row objects to dictionary
        for i in rows:
            average = i[0]

    except:
        average = ['could not calculate']

    return average

def get_round_your_points(round_id=0, team_id=0):
    # need error checks
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(f"SELECT points FROM teams WHERE round_id = '{round_id}' AND team_id = '{team_id}'")

        rows = cur.fetchall()
        # convert row objects to dictionary
        for i in rows:
            my_round_points = i[0]

    except:
        my_round_points = ['could not calculate']

    return my_round_points

def get_round_highest_points(round_id=0):
    # need error checks
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(f"SELECT MAX(points) FROM teams WHERE round_id = '{round_id}'")

        rows = cur.fetchall()
        # convert row objects to dictionary
        for i in rows:
            highest_round_points = i[0]

    except:
        highest_round_points = ['could not calculate']

    return highest_round_points

def get_player_stats():
    players = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT * FROM player_statistics')

        rows = cur.fetchall()

        # convert row objects to dictionary
        # for i in rows:
        #     player = {}
        #     player["player_id"] = i["player_id"]
        #     player["first_name"] = i["first_name"]
        #     player["last_name"] = i["last_name"]
        #     player["club_id"] = i["club_id"]
        #     player["position"] = i["position"]
        #     player["price"] = i["price"]
        #     players.append(player)

    except:
        players = ['no players with this filter']

    return players



''' Test executing code '''

# for i in get_players(position='', club='HBK'):
#     print(i)

# for i in get_round_avg_points():
#     print(i)

# for i in get_games():
#     print(i)

# for i in get_teams():
#     print(i)

# for i in get_team_players():
#     print(i)

# print(left_to_deadline())
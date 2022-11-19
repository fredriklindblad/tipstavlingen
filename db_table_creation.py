import sqlite3
from decouple import config

from db_utils import *

# def connect_to_db():
#     conn = sqlite3.connect(config('DB_PATH'))
#     return conn

def create_players_table():
    try:
        conn = connect_to_db()
        try:
            conn.execute('''DROP TABLE players''')
        except:
            pass
        conn.execute('''
            CREATE TABLE players (
                player_id INTEGER PRIMARY KEY NOT NULL,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                club_id INTEGER NOT NULL,
                FOREIGN KEY(club_id) REFERENCES clubs(club_id),
                position TEXT NOT NULL,
                price INTEGER NOT NULL
            );
        ''')

        conn.commit()
        print("Players table created successfully")
    except:
        print("Players table creation failed - Maybe table")
    finally:
        conn.close()

def insert_into_players_table():
    players = [ ['Andrew', 'Mills', 'ÖFK', 'GK', 4.5],
                ['Malcolm', 'Nilsson Säfqvist', 'HBK', 'GK', 5.5],
                ['Daniel', 'Paulson', 'ÖIS', 'MF', 6.0],
                ['Alexander', 'Johansson', 'HBK', 'FWD', 6.5],
                ['Aldin', 'Basic', 'SAIK', 'DEF', 6.0],
                ['Jack', 'Cooper Love', 'SAIK', 'FWD', 10.0],
                ['Samuel', 'Adrian', 'SÖD', 'DEF', 4.0],
                ['Alex', 'Simovski', 'DAL', 'DEF', 4.0],
                ['Jiloan', 'Hamad', 'ÖSK', 'MF', 8.0],
                ['Predag', 'Randelovic', 'UTS', 'MF', 6.0],
                ['Daniel', 'Ask', 'VSK', 'MF', 7.5],
                ['Gustav', 'Sandberg Magnusson', 'BP', 'MF', 8.0],
                ['Nikola', 'Vasic', 'BP', 'FWD', 9.0],
                ['Nicolas', 'Mortensen', 'TFF', 'FWD', 9.5],
                ['Oscar', 'Krusnell', 'BP', 'DEF', 5.0],
                ['Philip', 'Andersson', 'LBOIS', 'DEF', 4.5],
                ['Andreas', 'Johansson', 'HBK', 'DEF', 9.5],

            ]
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.executemany('''INSERT INTO players (first_name, last_name, club_id, position, price) VALUES (?, ?, ?, ?, ?)''', players)
        conn.commit()
        inserted_players = get_players()
        print('Insert successful')
    except:
        print('Failed to insert')
        conn().rollback()

    finally:
        conn.close()
    
    return inserted_players

def create_clubs_table():
    try:
        conn = connect_to_db()
        try:
            conn.execute('''DROP TABLE clubs''')
        except:
            pass
        conn.execute('''
            CREATE TABLE clubs (
                club_id INTEGER PRIMARY KEY NOT NULL,
                name TEXT NOT NULL
            );
        ''')

        conn.commit()
        print("Clubs table created successfully")
    except:
        print("Clubs table creation failed - Maybe table")
    finally:
        conn.close()

def insert_into_clubs_table():
    teams = ['AFC', 'Dalkurd', 'Halmstads BK', 'IF Brommapojkarna', 'IK Brage',
            'Jönköpings Södra IF', 'Landskrona BoIS', 'Norrby IF', 'Skövde AIK', 'Trelleborgs FF',
            'Utsiktens BK', 'Västerås SK', 'Örebro SK', 'Örgryte IS', 'Östers IF', 'Östersunds FK']
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        for team in teams:
            cur.execute(f"INSERT INTO clubs(name) VALUES ('{team}')")
        conn.commit()
        inserted_clubs = get_clubs()
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_clubs

def create_games_table():
    try:
        conn = connect_to_db()
        try:
            conn.execute('''DROP TABLE games''')
        except:
            pass
        conn.execute('''
            CREATE TABLE games (
                game_id INTEGER PRIMARY KEY NOT NULL,
                competition_id INTEGER NOT NULL,
                home_team TEXT NOT NULL,
                away_team TEXT NOT NULL,
                home_goals INTEGER NOT NULL,
                away_goals INTEGER NOT NULL,
                round_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                kick_off TEXT NOT NULL
            );
        ''')

        conn.commit()
        print("Games table created successfully")
    except:
        print("Games table creation failed - Maybe table")
    finally:
        conn.close()

def insert_into_games_table():
    games = [
                [1,'AIK','Hammarby',1,0,1, '21 Aug', '15:00'],
                [1,'MFF','Djurgården',4,1,1, '22 Aug', '19:00']
            ]
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.executemany('''INSERT INTO games (competition_id, home_team, away_team, home_goals, away_goals, round_id, date, kick_off) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', games)
        conn.commit()
        inserted_games = get_games()
        print('Insert successful')
    except:
        print('Failed to insert')
        conn().rollback()

    finally:
        conn.close()
    
    return inserted_games

def create_rounds_table():
    try:
        conn = connect_to_db()
        try:
            conn.execute('''DROP TABLE rounds''')
        except:
            pass
        conn.execute('''
            CREATE TABLE rounds (
                round_id INT PRIMARY KEY NOT NULL,
                competition_id INT NOT NULL,
                round_number INT NOT NULL,
                deadline DATETIME NOT NULL
            );
        ''')

        conn.commit()
        print("Rounds table created successfully")
    except:
        print("Rounds table creation failed - Maybe table")
    finally:
        conn.close()

def create_competitions_table():
    try:
        conn = connect_to_db()
        try:
            conn.execute('''DROP TABLE competitions''')
        except:
            pass
        conn.execute('''
            CREATE TABLE competitions (
                competition_id INT PRIMARY KEY NOT NULL,
                name TEXT NOT NULL
            );
        ''')

        conn.commit()
        print("Competitions table created successfully")
    except:
        print("Competitions table creation failed - Maybe table")
    finally:
        conn.close()

def insert_into_competitions_table():
    # competitions = ['Superettan', 'Damallsvenskan']

    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute('''INSERT INTO competitions (competition_id, name) VALUES (1, 'Superettan')''')
        conn.commit()
        inserted_competitions = get_competitions()
    except:
        print('Failed to insert')
        conn().rollback()

    finally:
        conn.close()
    
    return inserted_competitions

def create_player_match_events_table():
    try:
        conn = connect_to_db()
        try:
            conn.execute('''DROP TABLE player_match_events''')
        except:
            pass
        conn.execute('''
            CREATE TABLE player_match_events (
                player_match_event_id INT PRIMARY KEY NOT NULL,
                player_id INT NOT NULL,
                match_id INT NOT NULL,
                event_id INT NOT NULL,
                event_count INT NOT NULL
            );
        ''')

        conn.commit()
        print("Player_match_events table created successfully")
    except:
        print("Player_match_events table creation failed - Maybe table")
    finally:
        conn.close()

def create_events_table():
    try:
        conn = connect_to_db()
        try:
            conn.execute('''DROP TABLE events''')
        except:
            pass
        conn.execute('''
            CREATE TABLE events (
                event_id INTEGER PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                points INTEGER NOT NULL
            );
        ''')

        conn.commit()
        print("Events table created successfully")
    except:
        print("Events table creation failed - Maybe table")
    finally:
        conn.close()

def insert_into_events_table():
    events = [  ['Spelat 59 min',1],
                ['Spelat 60 min eller mer',2],
                ['Mål av målvakt eller back',6],
                ['Mål av mittfältare',5],
                ['Mål av forward',5],
                ['Assist',3],
                ['Nolla av målvakt och försvarare',4],
                ['Nolla av mittfältare',1],
                ['Målvakt straffräddning',5],
                ['Avgörande mål',1],
                ['Missad straffspark',-2],
                ['För varje två mål insläppt av målvakt eller försvarare',-1],
                ['Varning',-1],
                ['Utvisning',-3],
                ['Självmål',-2] 
            ]

    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.executemany('''INSERT INTO events (name, points) VALUES (?, ?)''', events)
        conn.commit()
        inserted_events = get_events()
    except:
        print('Failed to insert')
        conn().rollback()

    finally:
        conn.close()
    
    return inserted_events

def create_users_table():
    try:
        conn = connect_to_db()
        try:
            conn.execute('''DROP TABLE users''')
        except:
            pass
        conn.execute('''
            CREATE TABLE users (
                user_id INT PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                address TEXT NOT NULL,
                country TEXT NOT NULL
            );
        ''')

        conn.commit()
        print("Users table created successfully")
    except:
        print("Users table creation failed - Maybe table")
    finally:
        conn.close()

def create_teams_table():
    try:
        conn = connect_to_db()
        try:
            conn.execute('''DROP TABLE teams''')
        except:
            pass
        conn.execute('''
            CREATE TABLE teams (
                team_id INTEGER PRIMARY KEY NOT NULL,
                user_id INTEGER NOT NULL,
                competition_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                round_id INTEGER NOT NULL,
                points INTEGER NOT NULL
            );
        ''')
        conn.commit()
        print("Teams table created successfully")
    except:
        print("Teams table creation failed - Maybe table")
    finally:
        conn.close()

def insert_into_teams_table():
    teams = [  [1, 1, 'Framtiden', 1, 0],
               [2, 1, 'Jaget före laget', 1, 0]
            ]

    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.executemany('''INSERT INTO teams (user_id, competition_id, name, round_id, points) VALUES (?, ?, ?, ?, ?)''', teams)
        conn.commit()
        inserted_teams = get_teams()
    except:
        print('Failed to insert')
        conn().rollback()

    finally:
        conn.close()
    
    return inserted_teams

def create_team_players_table():
    try:
        conn = connect_to_db()
        try:
            conn.execute('''DROP TABLE team_players''')
        except:
            pass
        conn.execute('''
            CREATE TABLE team_players (
                team_players_id INT PRIMARY KEY NOT NULL,
                team_id INT NOT NULL,
                player_id INT NOT NULL,
                FOREIGN KEY (player_id) REFERENCES players(player_id),
                start INT NOT NULL
            );
        ''')
        conn.commit()
        print("Team_players table created successfully")
    except:
        print("Team_players table creation failed - Maybe table")
    finally:
        conn.close()

def insert_into_team_players_table():
    team_players = [  [1, 1, 1, 0],
                      [2, 1, 2, 1],
                      [3, 1, 3, 1],
                      [4, 1, 4, 1],
                      [5, 1, 5, 1],
                      [6, 1, 6, 1],
                      [7, 1, 7, 1],
                      [8, 1, 8, 1],
                      [9, 1, 9, 1],
                      [10, 1, 10, 1],
                      [11, 1, 11, 1],
                      [12, 1, 12, 0],
                      [13, 1, 13, 0],
                      [14, 1, 14, 0],
                      [15, 1, 17, 1],
                 ]

    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.executemany('''INSERT INTO team_players (team_players_id, team_id, player_id, start) VALUES (?, ?, ?, ?)''', team_players)
        conn.commit()
        print('Insert success')
    except:
        print('Failed to insert')
        conn().rollback()

    finally:
        conn.close()
    

def create_player_statistics_table():
    try:
        conn = connect_to_db()
        try:
            conn.execute('''DROP TABLE player_statistics''')
        except:
            pass
        conn.execute('''
            CREATE TABLE player_statistics (
                player_statistics_id INT PRIMARY KEY NOT NULL,
                player_id INT NOT NULL,
                minutes_played INT NOT NULL,
                goals INT NOT NULL,
                assists INT NOT NULL,
                yellow_cards INT NOT NULL,
                red_card INT NOT NULL
            );
        ''')

        conn.commit()
        print("Player_statistics table created successfully")
    except:
        print("Player_statistics table creation failed - Maybe table")
    finally:
        conn.close()


''' Executing the functions '''

create_players_table()
# insert_into_players_table()
# create_clubs_table()
# create_games_table()
# insert_into_games_table()
# create_rounds_table()
# create_competitions_table()
# insert_into_competitions_table()
# create_player_match_events_table()
# create_events_table()
# create_users_table()
# create_teams_table()
# insert_into_teams_table()
# create_team_players_table()
# insert_into_team_players_table()
# create_player_statistics_table()
# insert_into_clubs_table()
# insert_into_events_table()



''' SHOW '''
def fk_settings():
    conn = connect_to_db()
    mycursor = conn.cursor()
    mycursor.execute("PRAGMA foreign_keys;")
    rows = mycursor.fetchall()
    for x in rows:
        print(x)
    conn.close()

def show_tables():
    conn = connect_to_db()
    mycursor = conn.cursor()
    mycursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = mycursor.fetchall()
    for x in rows:
        print(x)
    conn.close()

def show_table_info():
    conn = connect_to_db()
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM team_players INNER JOIN players ON players.player_id = team_players.player_id WHERE team_players.team_id = 1;")
    rows = mycursor.fetchall()
    for x in rows:
        print(x)
    conn.close()

def show_info():
    conn = connect_to_db()
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM team_players;")
    rows = mycursor.fetchall()
    for x in rows:
        print(x)
    conn.close()


fk_settings()
# show_tables()
# show_table_info()
# show_info()
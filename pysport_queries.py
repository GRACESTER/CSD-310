import mysql.connector

# Connect to the database
config = {
    "user" : "pysports_user",
    "password": "birdbox2022!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
db = mysql.connector.connect(**config)
cursor = db.cursor()
print ("--DISPLAYING TEAM RECORDS--")
cursor.execute("SELECT team_id, team_name, mascot FROM pysports.team")
teams = cursor.fetchall()
for team in teams:
    print("\nTeam ID: {}".format(team[0]), "\nTeam Name: {}".format(team[1]), "\nMascot: {}".format(team[2]));

print()

cursor.execute("SELECT player_id, first_name, last_name, team_id FROM pysports.player")

print ("--DISPLAYING PLAYER RECORDS--")
players = cursor.fetchall()
for player in players:
    print("\nPlayer ID: {}".format(player[0]),

     "\nFirst Name: {}".format(player[1]),

     "\nLast Name: {}".format(player[2]),

     "\nTeam ID: {}".format(player[3]));

print()

print("Press any key to continue....")
db.close()
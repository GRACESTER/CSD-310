# Grace Steranko, Assignment 9.2, 7 July 2022
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
print("--DISPLAYING TEAM RECORDS--")
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
players = cursor.fetchall()
for player in players:
    print("\nPlayer ID: {}".format(player[0]),

     "\nFirst Name: {}".format(player[1]),

     "\nLast Name: {}".format(player[2]),

     "\nTeam Name: {}".format(player[3]))

print()
print("Press any key to continue....")
db.close() 

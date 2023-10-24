import psycopg2

# connects to the database with this filename you choose
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor() 

# Query 1 - select all artists from table
cursor.execute('SELECT * FROM "Artist"')

# Query 2  - select all names from the artist
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - Select only queen from artist table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" =%s', ["Queen"])

# Query 4 - Select artist id 51
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - Select only albums with artist id 51
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" =%s', [51])

# Query 6 - Tracks from queen
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" =%s' , ["Queen"])

# Query 7 
cursor.execute(
    'SELECT * FROM "Track" WHERE "Composer" =%s', ["Black Eyed Peas"])

# fetch the results(mulitple)
results = cursor.fetchall()
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)

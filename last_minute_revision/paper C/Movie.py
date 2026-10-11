# ============================================================
# Paper C - Question 1 (10 Marks)
#
# QUESTION:
# 1. Create Movie(MovieId, Title, Director, Genre, ReleaseYear).
# 2. Insert at least 10 records.
# 3. Display Action movies released between 2015 and 2021.
# 4. Count movies in each Genre.
# 5. Generate a pie chart showing movies per Genre.
#
# CONCEPT:
# 1. CREATE TABLE creates the Movie table.
# 2. executemany() inserts 10 movie records.
# 3. WHERE Genre = 'Action' filters Action movies.
# 4. BETWEEN 2015 AND 2021 selects the year range.
# 5. COUNT(*) counts movies.
# 6. GROUP BY Genre counts movies genre-wise.
# 7. matplotlib.pyplot.pie() draws the pie chart.
# ============================================================

import sqlite3
import matplotlib.pyplot as plt

con = sqlite3.connect("Movie.db")
cur = con.cursor()

# Create Movie table
cur.execute("""
CREATE TABLE IF NOT EXISTS Movie(
    MovieId INTEGER PRIMARY KEY,
    Title TEXT,
    Director TEXT,
    Genre TEXT,
    ReleaseYear INTEGER
)
""")

cur.execute("DELETE FROM Movie")

# Insert at least 10 records
data = [
    (1, "Warrior", "Raj", "Action", 2018),
    (2, "Funny Life", "Amit", "Comedy", 2019),
    (3, "Mission", "Jay", "Action", 2020),
    (4, "Love Story", "Neha", "Romance", 2017),
    (5, "Hero", "Kiran", "Action", 2014),
    (6, "Laugh Time", "Ravi", "Comedy", 2021),
    (7, "Crime City", "Mehul", "Thriller", 2016),
    (8, "Final Fight", "Raj", "Action", 2022),
    (9, "Family Day", "Nita", "Drama", 2018),
    (10, "Action Star", "Amit", "Action", 2019)
]

cur.executemany(
    "INSERT INTO Movie VALUES (?, ?, ?, ?, ?)", data
)
con.commit()

# 3. Display Action movies released between 2015 and 2021
print("Action movies released between 2015 and 2021:")

cur.execute("""
SELECT * FROM Movie
WHERE Genre = 'Action'
AND ReleaseYear BETWEEN 2015 AND 2021
""")

for row in cur.fetchall():
    print(row)

# 4. Count movies available in each Genre
print("\nNumber of movies in each Genre:")

cur.execute("""
SELECT Genre, COUNT(*)
FROM Movie
GROUP BY Genre
""")

genre_data = cur.fetchall()

for row in genre_data:
    print(row[0], ":", row[1])

# 5. Pie chart showing number of movies per Genre
genres = [row[0] for row in genre_data]
counts = [row[1] for row in genre_data]

plt.pie(counts, labels=genres, autopct="%1.1f%%")
plt.title("Number of Movies per Genre")
plt.show()

con.close()

# OUTPUT:
# Action movies released between 2015 and 2021:
# (1, 'Warrior', 'Raj', 'Action', 2018)
# (3, 'Mission', 'Jay', 'Action', 2020)
# (10, 'Action Star', 'Amit', 'Action', 2019)
#
# Number of movies in each Genre:
# Action : 5
# Comedy : 2
# Romance : 1
# Thriller : 1
# Drama : 1
#
# Pie chart displays the percentage of movies in each Genre.

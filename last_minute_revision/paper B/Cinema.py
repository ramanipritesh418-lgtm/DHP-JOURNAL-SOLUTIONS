# ============================================================
# Paper B - Question 1 (10 Marks)
#
# QUESTION:
# 1. Create Cinema(MovieID, MovieName, Genre, TicketsSold,
#    Collection).
# 2. Insert at least 10 records.
# 3. Display movies belonging to Comedy genre.
# 4. Delete movies where TicketsSold < 50.
# 5. Draw a bar chart of Collection for each Genre.
#
# CONCEPT:
# 1. CREATE TABLE creates the Cinema table.
# 2. executemany() inserts 10 movie records.
# 3. WHERE Genre = 'Comedy' filters Comedy movies.
# 4. DELETE removes movies with fewer than 50 tickets.
# 5. GROUP BY Genre groups movies by genre.
# 6. SUM(Collection) calculates total collection per genre.
# 7. matplotlib.pyplot.bar() creates the bar chart.
# ============================================================

import sqlite3
import matplotlib.pyplot as plt

con = sqlite3.connect("Cinema.db")
cur = con.cursor()

# Create Cinema table
cur.execute("""
CREATE TABLE IF NOT EXISTS Cinema(
    MovieID INTEGER PRIMARY KEY,
    MovieName TEXT,
    Genre TEXT,
    TicketsSold INTEGER,
    Collection REAL
)
""")

cur.execute("DELETE FROM Cinema")

# Insert at least 10 records
data = [
    (1, "Funny Day", "Comedy", 120, 60000),
    (2, "Hero", "Action", 200, 150000),
    (3, "Laugh Out", "Comedy", 80, 40000),
    (4, "Mystery House", "Thriller", 45, 25000),
    (5, "War Zone", "Action", 150, 120000),
    (6, "Family Time", "Drama", 60, 35000),
    (7, "Jokes", "Comedy", 30, 15000),
    (8, "Secret", "Thriller", 90, 50000),
    (9, "Love Story", "Romance", 75, 45000),
    (10, "Final Fight", "Action", 40, 20000)
]

cur.executemany(
    "INSERT INTO Cinema VALUES (?, ?, ?, ?, ?)", data
)
con.commit()

# Display Comedy movies
print("Comedy Movies:")

cur.execute("SELECT * FROM Cinema WHERE Genre = 'Comedy'")

for row in cur.fetchall():
    print(row)

# Delete movies where TicketsSold < 50
cur.execute("DELETE FROM Cinema WHERE TicketsSold < 50")
con.commit()

print("\nMovies after deletion:")

cur.execute("SELECT * FROM Cinema")

for row in cur.fetchall():
    print(row)

# Draw bar chart of total Collection for each Genre
cur.execute("""
SELECT Genre, SUM(Collection)
FROM Cinema
GROUP BY Genre
""")

result = cur.fetchall()

genres = [row[0] for row in result]
collections = [row[1] for row in result]

plt.bar(genres, collections)
plt.xlabel("Genre")
plt.ylabel("Collection")
plt.title("Collection for Each Genre")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

con.close()

# OUTPUT:
# Comedy Movies:
# (1, 'Funny Day', 'Comedy', 120, 60000.0)
# (3, 'Laugh Out', 'Comedy', 80, 40000.0)
# (7, 'Jokes', 'Comedy', 30, 15000.0)
#
# Movies with TicketsSold < 50 are deleted.
# Bar chart displays total collection for each remaining genre.

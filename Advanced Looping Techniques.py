# Task 1: The Selective DJ
genres = ["Rock", "Pop", "Hip Hop", "Jazz", "Electronic"]
selected_genres = genres[1:4]
for genre in selected_genres:
    print(genre)

# Task 2: The One-Liner Band with List Comprehensions
new_genres = [genre + " Music" for genre in genres]
print(new_genres)

# Task 3: Numerical Beats with range
for num in range(10, 0, -1):
    print(num)
print("The beat drops now!")

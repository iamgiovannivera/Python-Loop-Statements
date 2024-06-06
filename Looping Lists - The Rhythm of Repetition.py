# Task 1: The for Loop DJ Set
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for index, genre in enumerate(genres, start=1):
    print(f"Track {index}: Now playing {genre}")

# Task 2: The Remix Artist with while
index = 0
while index < len(genres):
    genre = genres[index]
    print(f"Track {index+1}: Now playing {genre}")
    if genre == 'Hip-hop':
        break 
    index += 1

# Task 3: Light Show Technician Loop
for index in range(len(genres)):
    genre = genres[index]
    if genre == 'Classical':
        continue  # Skip the Classical genre
    print(f"Track {index+1}: Light show is ready for {genre}")

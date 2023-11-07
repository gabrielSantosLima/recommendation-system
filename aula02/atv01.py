from math import sqrt

# Distância Euclidiana
EMPTY = -1

musics = ["Blues Traveler", "Broken Bells", "Deadmau5", "Norah Jones", "Phoenix", "Slightly Stoopid", "The Strokes", "Vampire Weekend"]

matrix = [
    ("Halley", [EMPTY, 4, 1, 4, EMPTY, EMPTY, 4, 1]),
    ("Veronica", [3, EMPTY, EMPTY, 5, 4, 2.5, 3, EMPTY]),
    ("Jordyn", [EMPTY, 4.5, 4, 5, 5, 4.5, 4, 4])
]

def euclid(person1: tuple[str, list[int]], person2: tuple[str, list[int]]):
    distance = 0
    for index in range(len(musics)):    
        music_name = musics[index]

        if person1[1][index] == EMPTY:
            print(f"for {music_name} ==> {person1[0]} empty.")
        elif person2[1][index] == EMPTY:
            print(f"for {music_name} ==> {person2[0]} empty.")
        else:
            distance += sqrt(person1[1][index] * person1[1][index] + person2[1][index] * person2[1][index])
            
    print(f"{person1[0]} - {person2[0]} : {distance:.2f}")
    print("===============================")

def main():
    euclid(matrix[0], matrix[1])
    euclid(matrix[0], matrix[2])

main()

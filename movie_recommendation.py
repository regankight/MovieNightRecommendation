# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:16:38 2025

@author: Regan
"""

import random

# Movie database
movies = {
    ("action", "short", "yes"): "John Wick 4 (2023)",
    ("action", "short", "no"): "Die Hard (1988)",
    ("comedy", "long", "yes"): "Glass Onion (2022)",
    ("comedy", "short", "no"): "Superbad (2007)",
    ("drama", "long", "yes"): "The Whale (2022)",
    ("drama", "short", "no"): "Good Will Hunting (1997)"
}

print("Welcome to the Movie Night Recommender!")
genre = input("What genre do you want? (action/comedy/drama): ").lower()
length = input("Do you want a short (< 2 hours) or long movie? (short/long): ").lower()
new_release = input("Do you want a newer movie (yes/no)? ").lower()

# Check if the combination exists in the movie database
if (genre, length, new_release) in movies:
    print(f"Recommended movie: {movies[(genre, length, new_release)]}")
else:
    print("No exact match found.")
    random_movie = random.choice(list(movies.values()))  # Pick a random movie
    print(f"Here's a random recommendation: {random_movie}")



Mahavatar_Narsimha = {
        "title": "Mahavatar Narsimha",
        "cast": ["Animated (voice cast not publicly listed)"],
        "release_date": "25 July 2025",
        "rating": 9.8,
        "genre": ["Mythological", "Animated"],
        "director": "Not credited",
        "language": ["Hindi", "Tamil", "Telugu", "Kannada", "Malayalam"],
        "duration": "2 hours 15 minutes",
        "description": "An animated mythological drama retelling the Narasimha avatar of Lord Vishnu."
    }

Su_from_So = {
        "title": "Su From So",
        "cast": ["Raj B Shetty", "Shaneel Gautham", "Prakash Thuminad"],
        "release_date": "25 July 2025",
        "rating": 9.3,
        "genre": ["Supernatural", "Comedy", "Drama"],
        "director": "Raj B Shetty",
        "language": ["Kannada"],
        "duration": "2 hours 10 minutes",
        "description": "A supernatural comedy-drama set in coastal Karnataka, blending folklore and emotion."
    }


movies = {"mahavatar narsimha": Mahavatar_Narsimha,
        "su from so": Su_from_So}
movie = input("Enter a movie to get details:").lower()
if movie in movies:
    print(f"\n Details for '{movie.title()}':\n")
    for key, value in movies[movie].items():
        print(f"{key.capitalize()}:{value}")
    
else:
    print ("Invalid movie name. try Mahavatar Narsimha, Su From So.")

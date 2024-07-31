# List of dictionaries containing the ratings
data = [
    {"oliver": 2, "pixel": 1, "pinky": 4},
    {"michael": 2, "oliver": 3, "pinky": 3},
    {"michael": 1, "oliver": 1, "pixel": 1}
]

# Dictionary to store the total ratings and count of ratings for each Fellow
ratings = {}

# Step 1: Aggregate the ratings
for entry in data:
    #print(entry)
    for fellow, rating in entry.items():
        if fellow not in ratings:
            ratings[fellow] = {'total': 0, 'count': 0}
        ratings[fellow]['total'] += rating
        
        ratings[fellow]['count'] += 1
        

# Step 2: Calculate the average ratings
average_ratings = {fellow: value['total'] / value['count'] for fellow, value in ratings.items()}

# Step 3: Determine the highest and lowest averages
highest_average = max(average_ratings, key=average_ratings.get)
lowest_average = min(average_ratings, key=average_ratings.get)

#print(f"The Fellow with the highest average rating is '{highest_average}'")
#print(f"The Fellow with the lowest average rating is '{lowest_average}'")
def get_rating(parameter_name, rating_scale):
    while True:
        try:
            print(f"\nRate {parameter_name} for the book:")
            for i, description in enumerate(rating_scale, start=0):
                print(f"{i}: {description}")

            rating = int(input("Enter your rating (0-5): "))
            if 0 <= rating <= 5:
                return rating
            else:
                print("Invalid input. Please enter a number between 0 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 5.")

def calculate_average(ratings):
    non_zero_ratings = [rating for rating in ratings if rating != 0]
    if non_zero_ratings:
        return round(sum(non_zero_ratings) / len(non_zero_ratings) * 2) / 2
    else:
        return 0  # If all ratings are 0, return 0

def interpret_rating(average_rating):
    if average_rating < 2:
        return "Poor"
    elif average_rating < 3:
        return "Fair"
    elif average_rating < 4:
        return "Good"
    elif average_rating < 5:
        return "Very Good"
    else:
        return "Excellent"

# Define rating scales
initial_response_scale = ["N/A", "Very negative", "Somewhat negative", "Indifferent", "Somewhat positive", "Very positive"]
recommendation_scale = ["N/A", "Highly discourage", "Discourage", "Neutral", "Encourage", "Highly encourage"]
re_readability_scale = ["N/A", "Definitely not reread", "Unlikely to reread", "Neutral", "Likely to reread", "Definitely will reread"]
plot_structure_scale = ["N/A", "Not engaged at all", "Somewhat engaged", "Moderately engaged", "Very engaged", "Extremely engaged"]
character_scale = ["N/A", "Uninteresting", "Slightly relatable", "Moderately relatable", "Very relatable", "Incredibly relatable"]

# Get ratings for each parameter
initial_response = get_rating("Initial Response", initial_response_scale)
recommendation = get_rating("Recommendation", recommendation_scale)
re_readability = get_rating("Re-Readability", re_readability_scale)
plot_structure = get_rating("Plot/Structure", plot_structure_scale)
character = get_rating("Character", character_scale)

# Calculate average rating
ratings = [initial_response, recommendation, re_readability, plot_structure, character]
average_rating = calculate_average(ratings)

# Interpret and display the result
interpretation = interpret_rating(average_rating)
print(f"\nAverage Rating: {average_rating:.1f} - {interpretation}")

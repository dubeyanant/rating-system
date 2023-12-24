def get_rating(parameter_name, rating_scale):
    while True:
        try:
            print(f"Rate {parameter_name} for the book:")
            for i, description in enumerate(rating_scale, start=1):
                print(f"{i}: {description}")

            rating = int(input("Enter your rating (1-5): "))
            if 1 <= rating <= 5:
                return rating
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

def calculate_average(ratings):
    return sum(ratings) / len(ratings)

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
initial_response_scale = ["Very negative", "Somewhat negative", "Indifferent", "Somewhat positive", "Very positive"]
recommendation_scale = ["Would not recommend", "Might not recommend", "Neutral", "Would recommend", "Highly recommend"]
re_readability_scale = ["Definitely not reread", "Unlikely to reread", "Neutral", "Likely to reread", "Definitely will reread"]
plot_structure_scale = ["Not engaged at all", "Somewhat engaged", "Moderately engaged", "Very engaged", "Extremely engaged"]
character_scale = ["Not relatable at all", "Somewhat relatable", "Moderately relatable", "Very relatable", "Extremely relatable"]

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
print(f"\nAverage Rating: {average_rating:.2f} - {interpretation}")

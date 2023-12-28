from colorama import Fore, Style  # Import colorama

def get_rating(parameter_name, rating_scale):
    while True:
        try:
            print(f"\nRate {parameter_name}:")
            for i, description in enumerate(rating_scale, start=0):
                print(f"{i}: {description}")

            rating = int(input(Fore.BLUE + "Enter your rating (0-5): " + Style.RESET_ALL))
            if 0 <= rating <= 5:
                return rating
            else:
                print(Fore.RED + "Invalid input. Please enter a number between 0 and 5." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number between 0 and 5." + Style.RESET_ALL)

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
again_scale = ["N/A", "Definitely not going through it again", "Unlikely to go through it again", "Neutral", "Likely to go through it again", "Definitely will go through it again"]
plot_structure_scale = ["N/A", "Not engaged at all", "Somewhat engaged", "Moderately engaged", "Very engaged", "Extremely engaged"]
character_scale = ["N/A", "Uninteresting", "Slightly interesting", "Relatable", "Moderately relatable", "Very relatable"]
ending_scale = ["N/A", "Worst", "Bad", "Neutral", "Good", "Awesome"]

# Get ratings for each parameter
initial_response = get_rating("Initial Response", initial_response_scale)
recommendation = get_rating("Recommendation", recommendation_scale)
again = get_rating("Re-Readability", again_scale)
plot_structure = get_rating("Plot/Structure", plot_structure_scale)
character = get_rating("Character", character_scale)
ending = get_rating("Ending", ending_scale)

# Calculate average rating
ratings = [initial_response, recommendation, again, plot_structure, character, ending]
average_rating = calculate_average(ratings)

# Interpret and display the result
interpretation = interpret_rating(average_rating)
print(Fore.GREEN + f"\nAverage Rating: {average_rating:.1f} - {interpretation}"  + Style.RESET_ALL)

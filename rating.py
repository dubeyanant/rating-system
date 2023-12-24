def get_initial_response_rating():
    print("Rate initial response for the book:")
    print("1: Very negative | 2: Somewhat negative | 3: Indifferent | 4: Somewhat positive | 5: Very positive")
    while True:
        try:
            rating = int(input("Enter your rating (1-5): "))
            if 1 <= rating <= 5:
                return rating
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

def get_recommendation_rating():
    print("Rate recommendation for the book:")
    print("1: Would not recommend | 2: Might not recommend | 3: Neutral | 4: Would recommend | 5: Highly recommend")
    while True:
        try:
            rating = int(input("Enter your rating (1-5): "))
            if 1 <= rating <= 5:
                return rating
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

def get_re_readability_rating():
    print("Rate Re-Readability for the book:")
    print("1: Definitely not reread | 2: Unlikely to reread | 3: Neutral | 4: Likely to reread | 5: Definitely will reread")
    while True:
        try:
            rating = int(input("Enter your rating (1-5): "))
            if 1 <= rating <= 5:
                return rating
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

def get_plot_rating():
    print("Rate Plot of the book:")
    print("1: Not engaged at all | 2: Somewhat engaged | 3: Moderately engaged | 4: Very engaged | 5: Extremely engaged")
    while True:
        try:
            rating = int(input("Enter your rating (1-5): "))
            if 1 <= rating <= 5:
                return rating
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

def get_character_rating():
    print("Rate Character of the book:")
    print("1: Not relatable at all | 2: Somewhat relatable | 3: Moderately relatable | 4: Very relatable | 5: Extremely relatable")
    while True:
        try:
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

# Get ratings for each parameter
initial_response = get_initial_response_rating()
recommendation = get_recommendation_rating()
re_readability = get_re_readability_rating()
plot_structure = get_plot_rating()
character = get_character_rating()

# Calculate average rating
ratings = [initial_response, recommendation, re_readability, plot_structure, character]
average_rating = calculate_average(ratings)

# Interpret and display the result
interpretation = interpret_rating(average_rating)
print(f"\nAverage Rating: {average_rating:.2f} - {interpretation}")

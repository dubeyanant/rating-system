def get_rating(prompt):
    print(prompt)
    print("1: Poor | 2: Fair | 3: Good | 4: Very Good | 5: Excellent")
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
initial_response = get_rating("Rate the Initial Response:")
recommendation = get_rating("Rate the Recommendation:")
re_readability = get_rating("Rate the Re-Readability:")
plot_structure = get_rating("Rate the Plot/Structure:")
character = get_rating("Rate the Character:")

# Calculate average rating
ratings = [initial_response, recommendation, re_readability, plot_structure, character]
average_rating = calculate_average(ratings)

# Interpret and display the result
interpretation = interpret_rating(average_rating)
print(f"\nAverage Rating: {average_rating:.2f} - {interpretation}")

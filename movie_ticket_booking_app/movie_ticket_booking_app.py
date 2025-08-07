# Movie data: title -> showtime -> price
movies = {
    "The Internship": {"10:00 AM": 8, "3:00 PM": 10},
    "Jobs": {"1:00 PM": 12, "6:00 PM": 15},
    "The Social Network": {"11:30 AM": 9, "5:30 PM": 13},
    "Avatar 2": {"12:00 PM": 10, "8:00 PM": 16}
}

total_tickets = 0
total_cost = 0
bookings = []

def show_movies():
    print("\nAvailable Movies:")
    for idx, movie in enumerate(movies.keys(), start=1):## to assign each movie a number (idx), starting from 1
        print(f"{idx}. {movie}")
    return list(movies.keys())

while True:
    movie_list = show_movies() ##This loop repeatedly asks til valid input is get

    try:
        movie_choice_num = int(input("\nSelect a movie by number: "))
        if not 1 <= movie_choice_num <= len(movie_list):  ##If the number is not between 1 and len(movie_list)
            print("Invalid movie selection.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    movie_choice = movie_list[movie_choice_num - 1]
    showtimes = movies[movie_choice]

    print(f"\nAvailable showtimes for '{movie_choice}':")
    showtime_list = list(showtimes.items())
    for idx, (time, price) in enumerate(showtime_list, start=1):## to assign each showtime_list a number (idx), starting from 1
        print(f"{idx}. {time} - ${price} per ticket")

    try:
        showtime_choice_num = int(input("Select a showtime by number: "))
        if not 1 <= showtime_choice_num <= len(showtime_list): ##If the number is not between 1 and len(showtime_list)
            print("Invalid showtime selection.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    selected_time, price_per_ticket = showtime_list[showtime_choice_num - 1]##We subtract 1 because list indices start at 0 SO TO adjusts the user's input (like "1" for the first option) to the correct list index

    try:
        num_tickets = int(input("How many tickets do you want to book? "))
        if num_tickets <= 0:
            print("Invalid number of tickets.")
            continue
    except ValueError:
        print("Please enter a valid number.")#IF INPUT IS NOT NUMBER
        continue

    booking_cost = price_per_ticket * num_tickets
    total_tickets += num_tickets
    total_cost += booking_cost
    bookings.append(f"{movie_choice} at {selected_time} - {num_tickets} ticket(s)")

    print(f"\n✅ You booked {num_tickets} ticket(s) for '{movie_choice}' at {selected_time}. Total: ${booking_cost:.2f}")

    another = input("Would you like to book another movie? (yes/no): ").lower()
    if another != "yes":
        break

# Summary
print("-------------------------------------------")
print("\n             Booking Summary:            ")
print("-------------------------------------------")
for booking in bookings:
    print(f"- {booking}")
print("-------------------------------------------")    
print(f"Total tickets booked: {total_tickets}")
print("-------------------")
print(f"Total cost: ${total_cost:.2f}")
print("===================")
print(" Enjoy your movie!")

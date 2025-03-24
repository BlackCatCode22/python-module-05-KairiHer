# Ask for the file name
filename = input("Enter a file name: ")

# Create an empty dictionary to store the day counts
day_counts = {}

try:
    # Open the file
    with open(filename, 'r') as file:
        for line in file:
            # Check if the line starts with 'From'
            if line.startswith("From "):
                # Split the line into words
                words = line.split()
                # The third word is the day of the week
                day_of_week = words[2]
                
                # Update the count in the dictionary
                if day_of_week in day_counts:
                    day_counts[day_of_week] += 1
                else:
                    day_counts[day_of_week] = 1

    # Print the dictionary with the days of the week
    print(day_counts)

except FileNotFoundError:
    print("File not found. Please check the filename and try again.")

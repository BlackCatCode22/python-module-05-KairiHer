filename = input("Enter file name: ")


email_counts = {}

try:
    with open(filename, 'r') as file:
        for line in file:

            if line.startswith("From "):

                words = line.split()

                email = words[1]
                

                if email in email_counts:
                    email_counts[email] += 1
                else:
                    email_counts[email] = 1


    max_email = None
    max_count = None

    for email, count in email_counts.items():
        if max_count is None or count > max_count:
            max_email = email
            max_count = count


    print(max_email, max_count)

except FileNotFoundError:
    print("File not found. Please check the filename and try again.")

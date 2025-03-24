
filename = input("Enter file name: ")


email_counts = {}

try:

    with open(filename, 'r') as file:
        for line in file:

            if line.startswith("From "):

                words = line.split()

                email = words[1]
                

                if email in

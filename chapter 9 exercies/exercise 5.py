
filename = input("Enter a file name: ")


domain_counts = {}

try:

    with open(filename, 'r') as file:
        for line in file:

            if line.startswith("From "):

                words = line.split()

                email = words[1]
                
                domain = email.split('@')[1]
                
                if domain in domain_counts:
                    domain_counts[domain] += 1
                else:
                    domain_counts[domain] = 1

    print(domain_counts)

except FileNotFoundError:
    print("File not found. Please check the filename and try again.")

filename = 'words.txt'

word_dict = {}

with open(filename, 'r') as file:
    for line in file:

      word = line.strip()
      
      word_dict[word] = None

word_to_check = "example" 
if word_to_check in word_dict:
    print(f"{word_to_check} is in the dictionary.")
else:
    print(f"{word_to_check} is not in the dictionary.")

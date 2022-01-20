import csv
import re

file = open('enron_spam_data.csv')

csvreader = csv.reader(file)

header = []
header = next(csvreader)
print(header)

labels = []

i = 0
rows = []
for row in csvreader:
    if i == 1500: 
        break
    i = i + 1
    rows.append(row[1] + " " + row[2])
    if row[3] == "ham":
        labels.append(0)
    if row[3] == "spam":
        labels.append(1)



def get_freq_word(text, word):
    all_words = re.sub("[^\w]", " ",  text).split()
    if (len(all_words) != 0):
        freq = 100 * (all_words.count(word) / len(all_words))
    else:
        freq = 0
    return freq

def get_freq_char(text, char):
    all_words = text.split()
    if len(all_words) != 0:
        freq = 100 * (all_words.count(char) / len(all_words))
    else:
        freq = 0
    return freq


words_to_calculate_freq = ["make", "address", "all", "3d", "our", "over", "remove", "internet", "order", "mail", "receive", "will", "people", "report", "address", "free", "business", "email", "you", "credit", "your", "font", "000", "money", "hp", "hpl", "george", "650", "lab", "labs", "telnet", "857", "data", "415", "85", "technology", "1999", "parts", "pm", "direct", "cs", "meeting", "original", "project", "re", "edu", "table", "conference"]
chars_to_calculate_freq = [';', '(', '[', '!', '$', '#']

print(len(rows))
with open('enron_dataset.csv', 'w') as eron_dataset:
    i = 0
    for row in rows:
        for word in words_to_calculate_freq:
            freq = get_freq_word(row, word)
            eron_dataset.write(str(round(freq, 2)) + ",")
        for char in chars_to_calculate_freq:
            freq = get_freq_char(row, char)
            eron_dataset.write(str(round(freq, 2)) + ",")
        
        # Average length of uninterruped sequences of capital letters
        sequence = False
        number_of_sequences = 0
        uninterruped_chars = 0
        for char in row:
            if char.isupper():
                uninterruped_chars += 1
                sequence = True
            else:
                if sequence:
                    number_of_sequences += 1
                sequence = False

        if number_of_sequences != 0:
            average_length_uninterruped_sequences_of_capital_letters = uninterruped_chars / number_of_sequences
        else:
            average_length_uninterruped_sequences_of_capital_letters = 0
        eron_dataset.write(str(round(average_length_uninterruped_sequences_of_capital_letters, 2)) + ",")

        # Total number of capital letters in e-mail
        total_number_of_uninterruped_chars = uninterruped_chars

        # Length of longest uninterrupted sequence of capital letters
        uninterruped_chars = 0
        longest_uninterruped_sequence = 0
        for char in row:
            if char.isupper():
                uninterruped_chars += 1
            else:
                if uninterruped_chars > 0 and uninterruped_chars > longest_uninterruped_sequence:
                    longest_uninterruped_sequence = uninterruped_chars
                uninterruped_chars = 0
        eron_dataset.write(str(longest_uninterruped_sequence) + ",")

        eron_dataset.write(str(total_number_of_uninterruped_chars) +",")

        eron_dataset.write(str(labels[i]))

        eron_dataset.write("\n")
        i += 1


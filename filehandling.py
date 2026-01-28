# ============================================
# Question No. 1
# ============================================

def extract_firstwords(filename):
    first_words = []

    with open(filename, 'r') as file:
        for line in file:
            first_words.append(line.split()[0])

    return first_words


print(extract_firstwords('sample.txt'))

# yo function le file ko each line bata first word matra lincha


# ============================================
# Question No. 2
# ============================================

with open('a.txt', 'r') as source, open('b.txt', 'w') as destination:
    for line in source:
        destination.write(line)

# yo code le a.txt ko sabai content b.txt ma copy garcha


# ============================================
# Question No. 3
# ============================================

with open('story.txt', 'r') as file:
    line_number = 1
    for line in file:
        words = line.split()
        print(f"Line {line_number}: {len(words)} words")
        line_number += 1

# yo program le each line ko word count print garcha


# ============================================
# Question No. 4
# ============================================

count = 0

with open('story.txt', 'r') as file:
    for line in file:
        count += 1

print("Total lines:", count)

# yo code le story.txt ko total line count garcha


# ============================================
# Question No. 5
# ============================================

with open('employees.txt', 'r') as src, open('management.txt', 'w') as dest:
    for line in src:
        if 'Python' in line:
            dest.write(line)

# yo program le Python bhako line matra naya file ma copy garcha


# ============================================
# Question No. 6
# ============================================

with open('numbers.txt', 'r') as src, open('squared.txt', 'w') as dest:
    for line in src:
        number = int(line)
        dest.write(str(number * number) + '\n')

# yo code le number ko square calculate garera file ma lekcha


# ============================================
# Question No. 7
# ============================================

message = input("Enter message: ")

with open('history.log', 'a') as file:
    file.write(message + '\n')

# yo program le purano data delete nagari naya message add garcha


# ============================================
# Question No. 8
# ============================================

with open('input.txt', 'r') as src, open('output.txt', 'w') as dest:
    for line in src:
        dest.write(line.upper())

# yo code le text lai uppercase ma change garcha

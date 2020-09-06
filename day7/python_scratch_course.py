from collections import defaultdict, Counter

# Line indentation

for i in [1, 2, 3, 4, 5]:
    print(i)
    for j in [1, 2, 3, 4, 5]:
        print(j)
        print(i + j)
    print(i)
print("done logging")

# Long identifier across several lines
long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 +
                           11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)
print(long_winded_computation)

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
easier_to_read_list_of_lists = [[1,2,3],
                                 [4,5,6],
                                 [7,8,9]]

print(list_of_lists)
print(easier_to_read_list_of_lists)

# Lists

x = [1, 2, 3]
x.extend([4, 5, 6])
print(x)

x = [1, 2, 3]
# y is new copy
y = x + [4, 5, 6]
print(x)
print(y)

# Tuples
print("Tuples")
my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3


def sum_and_product(x, y):
    return (x + y),(x * y)

try:
    print(my_tuple)
    print(other_tuple)
    print("Sum is %d" % s)
    print("Product is %d" % p)
    s, p = sum_and_product(3,7)
    my_tuple[1] = 3
except:
    print("Cannot modify a tuple")


# Dictionares
empty_dict = {}
empty_dict2 = dict()
grades = {"Joel": 80, "Tim": 95}

joel_grade = grades["Joel"]

print(joel_grade)
print(grades["Tim"])

# key error
try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate!")

# Faster than check through keys
joel_has_grade = "Joel" in grades
joel_has_grade2 = "Joel" in grades.keys()
print("joel_has_grade = %s" % str(joel_has_grade))
print("joel_has_grad2 = %s" % str(joel_has_grade2))

# get method for dictionaries
joels_grade = grades.get("Joel", 0)
kates_grade = grades.get("Kate", 0)
no_ones_grade = grades.get("No One")

print("Joel grade : %d" % joels_grade)
print("Kates grade : %d" % kates_grade)
print("Kates grade : %s" % no_ones_grade)

# Assign key-value pairs using the same square bracket
grades["Tim"] = 99
grades["Kate"] = 100
num_students = len(grades)

print("Tim grade is %d" % grades["Tim"])
print("Kate grade is %d" % grades["Kate"])

# Dictonaries used to represents structured data
tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awsome",
    "retweet_count" : 100,
    "hashtags" : ['#data', '#science', '#datascience', '#awsome', '#yolo']
}

print("Tim grade is %d" % grades["Tim"])
print("Tim grade is %d" % grades["Tim"])

tweet_keys = tweet.keys()
tweet_values = tweet.values()
tweet_items = tweet.items()

print("user" in tweet_keys)
print("user" in tweet)
print("joelgrus" in tweet_values)


# Multipart key as key in dictionary. Solution -> use tuple

test_dict = {}
test_dict[('A', 'A')] = 4
test_dict[('A', 'B')] = 3
test_dict[('B', 'A')] = 8
test_dict[('B', 'B')] = 2

print("test_dict ('A','A') is %s" % test_dict[('A', 'A')])

# Multipart key as list doesn't work. Keys have to be immutable
# Traceback (most recent call last):
#  File "C:/Github/100daysOfDataScience/day7/python_scratch_course.py", line 132, in <module>
#    test_dict_list[[1, 2]] = 10
# TypeError: unhashable type: 'list'
# Wniosek -> Do not use.
#test_dict_list = {}
#test_dict_list[[1, 2]] = 10
#test_dict_list[[1, 2]]
#print("test_dict_list [1, 2] is %s" % test_dict_list[[1, 2]])


# defaultdict()
# Dictionary keys are letters. How to make entire word ? document.split(' ')
print("defaultdict() example. Keys are letters")
document = "Dog is fine. Cat is wrong. Dsdsdw."

word_counts = defaultdict(int)
for word in document:
    word_counts[word] += 1
print(word_counts)


print("defaultdict() example. Keys are words.")
document = "Dog is fine. Cat is wrong. Dsdsdw."

word_counts = defaultdict(int)
for word in document.split(' '):
    word_counts[word] += 1
print(word_counts)


# Counter for counting histograms
# change list to dictionary
c = Counter([0, 1, 2, 0])
word_counts = Counter(document.split(' '))
print(word_counts)

print("Top 2 most common words")
# Print 2 top common words
for word, item in word_counts.most_common(2):
    print(str(word) + " " + str(item))


# Network analysis
# Find key connector - person who connects people the most
# Entry data
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]

friendship = [(0,1),(1,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

# Build list of friends for every user
for user in users:
    user["friends"] = []

for i, j in friendship:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

print("User 0 has %s friends" % len(users[0]["friends"]))


# How many friends user has
def number_of_friends(user):
    return len(user["friends"])


# Total number of connection
total_connections = sum(number_of_friends(user) for user in users)
print("Total number of connections is: %s " % total_connections)


# Average number of connections per user
num_users = len(users)
avg_connections = total_connections / num_users
print("Average connection per user is %s " % avg_connections)

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]


def friends(user):
    _, b = user
    return b


num_friends_by_id = sorted(num_friends_by_id, key=friends, reverse=True)

print(num_friends_by_id)


from collections import defaultdict, Counter

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

interests = [
    (0, "Hadoop"), (0, 'BigData'),(0, 'Hbase'),(0, 'Java'),
    (0, "Spark"), (0, 'Storm'), (0, 'Cassandra'),
    (1, 'NoSQL'), (1, 'MongoDB'), (1, 'Cassandra'), (1, 'HBase'),
    (1, 'Python'), (2, 'Python'), (6, 'mathematics'), (2, 'mathematics')
]


# find users with target_interest
def data_scientists_who_like(target_interest):
    return[user_id for user_id, user_interest in interests
           if user_interest == target_interest]


# interest -> list of user
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

interest_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interest_by_user_id[user_id].append(interest)


def most_common_interest_with(user):
    return Counter(interested_user_id
                   for interest in interest_by_user_id[user["id"]]
                   for interested_user_id in user_ids_by_interest[interest]
                   if interested_user_id != user["id"])


if __name__ == "__main__":
    print("User 0 has %s interests shared with user %s " % (most_common_interest_with(users[0]).most_common(1)[0][0],most_common_interest_with(users[0]).most_common(1)[0][1]))
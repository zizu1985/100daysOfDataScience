# users data structure - list of dictonaries
from collections import Counter

"""
    1. Build friends of friends feature
    2. Mutual friends - what friends of friends using counter method. 
"""

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

# friendship data structure
friendship = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

# Build list of friends for every user
for user in users:
    user["friends"] = []

for i, j in friendship:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])


def friends_of_friend_ids_bad(user):
    " foaf is short for friends of friend "
    return [foaf["id"]
            for friend in user["friends"]   # for each of user's friends
            for foaf in friend["friends"]]  # get each of_their_friends


def friends_of_friend_ids_bad_plus_mine_friends(user):
    " foaf is short for friends of friend plus friends of mine"
    l = [foaf["id"]
            for friend in user["friends"]   # for each of user's friends
            for foaf in friend["friends"]]
    ul = list(friend["id"] for friend in user["friends"])
    """ append for list is not the same as + to list. Add element as whole vs add each element directly"""
    l += ul
    return l
    # get each of_their_friends


def not_the_same(user, other_user):
    return user["id"] != other_user["id"]


def not_friends(user, other_user):
    """ other_user is not friend of user if he is not in user["friends"]
        He is not_the_same as any of user in friends
    """
    return all(not_the_same(user, friend) for friend in other_user["friends"])


def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                   for friend in user["friends"]
                   for foaf in friend["friends"]
                   if not_the_same(user, foaf)
                   and not_friends(user, foaf))


if __name__ == "__main__":
    choice = int(input("Please provide user to whom recommendation should be done. 99 displays some tests : w"))
    if choice == 99:
        print("Full list of friends of friends for user 1 is %s" % friends_of_friend_ids_bad(users[1]))
        print("Friends of user 1 are %s" % [friend["id"] for friend in users[1]["friends"]])
        print("Friends of user 0 are %s" % [friend["id"] for friend in users[0]["friends"]])
        print("Friends of user 2 are %s" % [friend["id"] for friend in users[2]["friends"]])
        print("Friends of user 3 are %s" % [friend["id"] for friend in users[3]["friends"]])

        # Why output is not [0, 2, 3, 0, 1, 3, 1, 2, 4] ?
        # Solution: Bad select user = 1 in users dictionary. Replace with users[1]
        # friends of friends

        print("Full list of friends of friends for user 1 plus his/her friends is %s" % friends_of_friend_ids_bad_plus_mine_friends(users[1]))
        print("=====")
        print("Friends in common for user 3 are %s" % friends_of_friend_ids(users[5]))
    else:
        cnt = friends_of_friend_ids(users[choice])
        if len(cnt) > 0:
            elem , freq = cnt.most_common(1)[0]
        print("Recommended new friend for you is %s and his/her name is %s" % (users[elem]["id"],users[elem]["name"]))
        print("Frequence of recommended friend is %s" % freq)
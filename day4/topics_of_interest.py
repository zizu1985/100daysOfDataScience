from collections import Counter

interests = [
    (0, "Hadoop"), (0, 'BigData'),(0, 'Hbase'),(0, 'Java'),
    (0, "Spark"), (0, 'Storm'), (0, 'Cassandra'),
    (1, 'NoSQL'), (1, 'MongoDB'), (1, 'Cassandra'), (1, 'HBase'),
    (1, 'Python'), (2, 'Python'), (6, 'mathematics'), (2, 'mathematics')
]

if __name__ == "__main__":
    words_and_counts = Counter(word
                               for user, interest in interests
                               for word in interest.lower().split())

    for word, count in words_and_counts.most_common():
        if count > 1:
            print(word, count)
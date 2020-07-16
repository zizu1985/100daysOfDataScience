from collections import defaultdict

# List of tuples
salaries_and_tenuries = [(83000, 8.7), (88000, 8.1),
                         (48000, 0.7), (76000, 6),
                         (69000, 6.5), (76000, 7.5),
                         (60000, 2.5), (83000, 10),
                         (48000, 1.9), (63000, 4.2)]

salary_by_tenure = defaultdict(list)

# keys are years
# value is salary
for salary, tenure in salaries_and_tenuries:
    salary_by_tenure[tenure].append(salary)

average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}


def tenure_bucket(tenure):
    if tenure < 2:
        return "1. less than two"
    if tenure < 5:
        return "2. between two and five"
    else:
        return "3. more than five"

# keys -> bucket
# value -> average salary
# 1. First build new dictionary (bucket -> list of salaries)
# 2. Modify dictionary with put statistics for bucket for each entry


salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenuries:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

average_salary_by_bucket = dict(sorted(average_salary_by_bucket.items()))

if __name__ == "__main__":
    print("Average salary by tenure.")
    print(average_salary_by_tenure)
    print("Average salary by tenure bucket")
    print(average_salary_by_bucket)
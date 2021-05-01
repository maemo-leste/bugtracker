#!/usr/bin/env python3
import datetime
import github3

ORG = "maemo-leste"
REPO = "bugtracker"

gh = github3.GitHub()
data = {REPO: {}}

for i in enumerate(gh.issues_on(ORG, REPO, state="all")):
    data[REPO][i[0]] = {
        "created_at": i[1].created_at,
        "closed_at": i[1].closed_at,
    }

one_day = datetime.timedelta(days=1)
now = datetime.datetime.now(datetime.timezone.utc)

last_number = max([int(i) for i in data[REPO].keys()])
first_date = data[REPO][last_number]["created_at"]

day = datetime.datetime(first_date.year,
                        first_date.month,
                        first_date.day,
                        tzinfo=datetime.timezone.utc)
day += one_day

result = {}

f = open("result.tsv", "w")
f.write("date\tOpen\tClosed\n")

while day < now:
    key = day.strftime("%Y-%m-%d")

    open_issues = 0
    closed_issues = 0

    for i in data[REPO]:
        elem = data[REPO][i]

        if elem["created_at"] > day:
            continue

        if isinstance(elem["closed_at"],
                      datetime.datetime) and elem["closed_at"] < day:
            closed_issues += 1
        else:
            open_issues += 1

    output = "%s\t%d\t%d" % (key, open_issues, closed_issues)

    f.write(output + "\n")
    day += one_day

f.close()

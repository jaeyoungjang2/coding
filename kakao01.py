id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2
answer = []
alerted = {}
alert = {}

for user in id_list:
    alert[user] = []
    alerted[user] = 0

for report_info in report:
    report = report_info.split()
    reporter = report[0]
    criminal = report[1]

    if criminal in alert[reporter]:
        continue
    else:
        alert[reporter].append(criminal)
        alerted[criminal] += 1

for user in id_list:
    response = 0
    for criminal in alert[user]:
        if alerted[criminal] >= k:
            response += 1
    answer.append(response)

print(answer)

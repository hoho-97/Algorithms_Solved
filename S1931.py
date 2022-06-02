from sys import stdin as st

n = int(st.readline())

meeting_schedules = dict()
for _ in range(n):
    meeting = tuple(map(int, st.readline().split()))
    for m in range(meeting[0], meeting[1]):
        if m not in meeting_schedules.keys():
            meeting_schedules[m] = [meeting]
        else:
            meeting_schedules[m].append(meeting)
sorted(meeting_schedules.keys(), key=lambda x : len(meeting_schedules[x]))


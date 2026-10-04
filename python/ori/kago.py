kago = input().split()

note = {}

for furutu in kago:
    if furutu in note:
        note[furutu] += 1
    else:
        note[furutu] = 1

for name,kosuu in note.items():
    print(f"{name}:{kosuu}")
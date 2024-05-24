def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(25))


def eleves_du_mois(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = []

    for i in range(len(notes)):
        if notes[i] == note_maxi:
            meilleurs_eleves.append(eleves[i])
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]]

    return (note_maxi, meilleurs_eleves)


eleves_nsi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]
print(eleves_du_mois(eleves_nsi, notes_nsi))
print(eleves_du_mois([], []))

def effectif_notes(notes_eval: list):
    somme = 0
    tab_final = []
    for i in range(11):
        somme = 0
        for j in range(len(notes_eval)):
            if notes_eval[j] == i:
                somme += 1
        tab_final.append(somme)

    return tab_final
eff = [2,0,5,9,6,9,10,5,7,9,9,5,0,9,6,5,4]
print(effectif_notes(eff))

def notes_triees(notes_eval):
    notes = effectif_notes(notes_eval)
    tab_final = []
    for i in range(len(notes)):
        for j in range(notes[i]):
            tab_final.append(i)

    return tab_final
notes_triees(eff)

def dec_to_bin(nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0:
        return str(1)
    else:
        return dec_to_bin(q) + str(r)


def bin_to_dec(nb_bin):
    if len(nb_bin) == 1:
        if nb_bin[0] == '0':
            return 0
        else:
            return 1
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit=1
        return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit

print(dec_to_bin(25))
print(bin_to_dec('101010'))



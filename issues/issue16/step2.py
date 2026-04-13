import re
import sys
from parseheadline import parseheadline


def adjust_hw(basehw, suffix, lid):
    basehw = re.sub('[a][Hm]$', 'a', basehw) # rameSaH -> rameSa
    suffix = suffix.lstrip('[-˚]') # -nI -> nI
    # kamala / -lam = kamalam
    if (basehw.endswith('a') and suffix.endswith('am')) and ((basehw + 'm').endswith(suffix)):
        return basehw + 'm'
    # Sveta / -taH = SvetaH
    elif (basehw.endswith('a') and suffix.endswith('aH')) and ((basehw + 'H').endswith(suffix)):
        return basehw + 'H'
    # kamala / -lA = kamalA
    elif (basehw.endswith('a') and suffix.endswith('A')) and ((basehw[:-1] + 'A').endswith(suffix)):
        return basehw[:-1] + 'A'
    # ISAna / -nI = ISAnI
    elif (basehw.endswith('a') and suffix.endswith('I')) and ((basehw[:-1] + 'I').endswith(suffix)):
        return basehw[:-1] + 'I'
    # aguru / -ru = aguru
    elif basehw.endswith(suffix):
        return basehw
    # akziti / -tiH = akzitiH
    elif basehw.endswith(suffix.rstrip('[mH]')):
        return basehw + suffix[-1]
    # aNkin / -nI = aNkinI
    elif (basehw+'I').endswith(suffix):
        return basehw + 'I'
    # anurAgin / -RI = anurAgiRI
    elif (basehw[:-1]+'RI').endswith(suffix):
        return basehw[:-1] + 'RI'
    # atikaTA / -Ta/TaH/Tam = atikaTa/atikaTaH/atikaTam
    elif re.sub('A$', 'a', basehw).endswith(re.sub('a[Hm]*$', 'a', suffix)):
        return basehw[:-2] + suffix
    # siMhala[mH]* / -lAH = siMhalAH
    elif re.sub('a$', 'AH', basehw).endswith(suffix):
        return basehw[:-2] + suffix
    # aditi / -tI = aditI
    elif re.sub('i$', 'I', basehw).endswith(suffix):
        return basehw[:-1] + 'I'
    # apAYc / -k = apAk
    elif re.sub('Yc$', 'k', basehw).endswith(suffix):
        return basehw[:-2] + 'k'
    # kanizWaka / -zWikA = kanizWikA
    elif re.sub('aka$', 'ikA', basehw).endswith(suffix):
        return re.sub('aka$', 'ikA', basehw)
    # janman / -hetuH = janmahetuH
    elif basehw == 'janman' and not re.search('^[aAiIuUfFxeEoO]', suffix):
        return 'janma' + suffix
    # atiruc / -k = atiruk
    elif basehw.endswith('c') and suffix == 'k':
        return basehw[:-1] + 'k'
    # kuSIlava / -vO = kuSIlavO
    elif re.sub('a$', 'O', basehw).endswith(suffix):
        return re.sub('a$', 'O', basehw)
    # tariH / -rI = tarI
    elif re.sub('iH$', 'I', basehw).endswith(suffix):
        return re.sub('iH$', 'I', basehw)
    # aBisvara + re
    elif re.sub('a$', 'e', basehw).endswith(suffix):
        return re.sub('a$', 'e', basehw)
    # upastamBaka + tA
    elif suffix == 'tA':
        return basehw + 'tA'
    # upastamBaka + tvam
    elif suffix == 'tvam':
        return basehw + 'tvam'
    # aviSeza + ka[HM]*
    elif re.search('^ka[HM]*$', suffix):
        return basehw + suffix
    # AmuktiH + kti = AmuktiH
    elif basehw.endswith('H') and re.sub('iH$', 'i', basehw).endswith(suffix):
        return basehw[:-1]
    elif basehw.endswith('H') and re.sub('uH$', 'u', basehw).endswith(suffix):
        return basehw[:-1]
    # If no matches, they need to be manually corrected
    return None


if __name__=="__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    log_file = sys.argv[3]

    fout = open(output_file, 'w')
    flog = open(log_file, 'w')
    flog.write('Lnum\tbasehw\tsuffix\tresolution\n')
    correct = 0
    wrong = 0

    with open(input_file, 'r') as fin:
        for lin in fin:
            lin = lin.rstrip()
            if '¦' in lin:
                pref = lin.split('¦')[0]
            if lin.startswith('<L>'):
                metaline = lin
                meta = parseheadline(lin)
                lid = meta['L']
                fout.write(lin + '\n')
            elif lin.startswith('.{@{#'):
                m = re.search(r'^[.]{@{#\-([^#]+)#}@}', lin)
                if m:
                    basehw = meta['k1']
                    suffix_str = m.group(1)
                    suffixes = [s.strip() for s in suffix_str.split(', -')]
                    for suffix in suffixes:
                        suggestion =  adjust_hw(basehw, suffix, lid)
                        if suggestion:
                            correct += 1
                            flog.write(f'{lid}\t{basehw}\t{suffix}\t{suggestion}\n')
                        else:
                            wrong += 1
                            flog.write(f'{lid}\t{basehw}\t{suffix}\tNone\n')
                        fout.write('<LEND>\n\n')
                        if suggestion:
                            metaline1 = metaline.replace('<k1>' + basehw, '<k1>' + suggestion)
                            metaline1 = metaline1.replace('<k2>' + basehw, '<k2>' + suggestion)
                            metaline1 = metaline1.replace('<pc>', '.XYZ<pc>')
                            fout.write(metaline1 + '\n')
                        else:
                            metaline1 = metaline.replace('<k2>', '.ABC<k2>')
                            metaline1 = metaline1.replace('<e>', '.ABC<e>')
                            metaline1 = metaline1.replace('<pc>', '.XYZ<pc>')
                            fout.write(metaline1 + '\n')
                        hw_rep =  pref + ' + .{@{#-' +  suffix + '#}@}¦'
                        lin_with_pref = lin.replace('.{@{#-' + suffix_str + '#}@}', hw_rep)
                        fout.write(lin_with_pref + '\n')
                else:
                    fout.write(lin + '\n')
            else:
                fout.write(lin + '\n')
    total = correct + wrong
    print(f'Resolved: {correct}, Unresolved: {wrong}, Total: {total}')
    fin.close()
    fout.close()
    flog.close()

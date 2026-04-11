import re
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
    # upastamBaka + tA
    elif suffix == 'tA':
        return basehw + 'tA'
    # aviSeza + ka[HM]*
    elif re.search('^ka[HM]*$', suffix):
        return basehw + suffix
    # If no matches, they need to be manually corrected
    print(lid + ' -> ' + basehw + ' + ' + suffix)
    return None


if __name__=="__main__":
    fout = open('tmp_ap_1.txt', 'w')
    correct = 0
    wrong = 0

    with open('tmp_ap_0.txt', 'r') as fin:
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
                m = re.search('^[.]{@{#\-([^ }]+)#}@}', lin)
                if m:
                    basehw = meta['k1']
                    suffix = m.group(1)
                    suggestion =  adjust_hw(basehw, suffix, lid)
                    if suggestion:
                        correct += 1
                    else:
                        wrong += 1
                    fout.write('<LEND>\n\n')
                    if suggestion:
                        metaline1 = metaline.replace('<k1>' + basehw, '<k1>' + suggestion)
                        metaline1 = metaline1.replace('<k2>' + basehw, '<k2>' + suggestion)
                        metaline1 = metaline1.replace('<pc>', '.XYZ<pc>')
                        fout.write(metaline1 + '\n')
                    else:
                        fout.write(metaline + '\n')
                    hw_rep =  pref + ' + .{@{#-' +  m.group(1) + '#}@}¦'
                    lin_with_pref = lin.replace('.{@{#-' + m.group(1) + '#}@}', hw_rep)
                    fout.write(lin_with_pref + '\n')
                else:
                    fout.write(lin + '\n')
            else:
                fout.write(lin + '\n')
    print('Resolved : ', correct, ' - ', correct*100/(correct+wrong), '%')
    print('Unresolved : ', wrong, ' - ', wrong*100/(correct+wrong), '%')
    print('Total : ', correct + wrong, ' - ', '100%')
    fin.close()
    fout.close()

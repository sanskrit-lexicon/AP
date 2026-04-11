import re
from parseheadline import parseheadline

fout = open('tmp_ap_1.txt', 'w')
correct = 0
wrong = 0

def adjust_hw(basehw, suffix):
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
    # If no matches, they need to be manually corrected
    print('No result found for: ' + basehw + ' + ' + suffix)
    return None

#print(adjust_hw('ISvaraH', '-rI'))

if __name__=="__main__":
    with open('tmp_ap_0.txt', 'r') as fin:
        for lin in fin:
            lin = lin.rstrip()
            if lin.startswith('<L>'):
                metaline = lin
                meta = parseheadline(lin)
            elif lin.startswith('.{@{#'):
                m = re.search('^[.]{@{#\-([^ }]+)#}@}', lin)
                if m:
                    basehw = meta['k1']
                    suffix = m.group(1)
                    resol = adjust_hw(basehw, suffix)
                    if resol:
                        correct += 1
                    else:
                        wrong += 1
                    print(basehw, suffix, adjust_hw(basehw, suffix))
                    #fout.write('<LEND>\n\n')
                    #fout.write(metaline + '\n')
            #fout.write(lin + '\n')
    print('Resolved : ', correct)
    print('Unresolved : ', wrong)
    print('Total : ', correct + wrong)


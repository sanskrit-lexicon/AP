import re
from parseheadline import parseheadline

fout = open('tmp_ap_1.txt', 'w')
correct = 0
wrong = 0

def adjust_hw(basehw, suffix):
    basehw = re.sub('a[Hm]$', 'a', basehw) # rameSaH -> rameSa
    suffix = suffix.lstrip('-') # -nI -> nI
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


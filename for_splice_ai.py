from sys import exit
from my_library import writting_file, checkfile, zagprint, few_columns

def revers(buk):
    if buk.upper()=='A':
        return 'T'
    if buk.upper()=='T':
        return 'A'
    if buk.upper()=='G':
        return 'C'
    if buk.upper()=='C':
        return 'G'
    if buk.upper()=='N':
        return 'N'

def zapis(buk):
    tri=[]
    if buk.upper()=='N':
        tri.append('N')
    if not(buk.upper()=='A'):
        tri.append('A')
    if not(buk.upper()=='T'):
        tri.append('T')
    if not(buk.upper()=='G'):
        tri.append('G')
    if not(buk.upper()=='C'):
        tri.append('C')

    return tri



name_fgens='gens_spliceAI_sorted.txt'
zagprint(name_fgens)
mfile=open(name_fgens,'r')
name_genom_file='changed_genom.fa'
genom=open(name_genom_file,'r')
file_out=open('splice_ai.txt','w')
file_out.write('#CHOM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tSAMPLE\n')
chm=[]
num_gen=0
num_stgen=1
chg='chr1'
const_s='\t100\tPASS\tMQ=50\tAF:GT\t0.5:0/1\n'
fl1=0
buk=''
for st in mfile:
    if  fl1==0:
        fl1=1
        continue
    fl3=0
    num_stgen+=1
    stm=st.split('\t')
    ch='chr'+stm[1]

    if not(ch in chm):
        chm.append(ch)

    strand=stm[2]
    start=int(stm[3])
    end=int(stm[4])
    num_st=start//50

    if start%50==0:
        ost_st=50
        num_st-=1
    else:
        ost_st=start%50

    while ((num_gen <= num_st) or not (ch == chg)):  # Пока положение не перевалит за cе И пока хромосома не равна нужной
        if fl3==1:
            break
        stg = genom.readline()[:-1]
        fl2 = 0
        if not ('>' in stg):
            num_gen += 1
        else:
            num_gen = 0
            fl2 = 1
            chg = stg.rstrip()[1:]
            print('{}'.format(ch), end=' ')

    if not((num_gen == num_st+1) and (ch == chg)):
        continue

    pos=ost_st-1
    while (start <= end):
        if pos==50:
            pos=0
            stg = genom.readline()[:-1]
            if not('>' in stg):
                num_gen+=1
            else:
                num_gen=0
                fl2 = 1
                chg = stg.rstrip()[1:]
                print('{}'.format(ch), end=' ')
        try:
            buk=stg[pos]
        except IndexError:
            print('error')
            print(pos)
            print(stg)
            print(st[:-1])
            print(num_stgen)
            print(num_gen)
            print()
            fl3=1
            if buk.upper=='N':
                fl3=1
                break
        # if strand=='-':
        #     buk=revers(buk)
        bukvas=zapis(buk)
        if not(bukvas[0]=='N'):
            for bukva in bukvas:
                file_out.write('{}\t{}\t.\t{}\t{}'.format(ch,start,buk.upper(),bukva)+const_s)
        pos += 1
        start+=1


print(chm)
mfile.close()
genom.close()
file_out.close()
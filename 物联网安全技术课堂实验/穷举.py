#coding=gbk
import string
def main():
    s0=input('����������s��')#BEEAKFYDJXUQYHYJIQRYHTYJIQFBQDUYJIIKFUHCQD
    s=s0.lower()
    m = []
    for i in string.ascii_lowercase:
        m.append(i)
    print('ԭʼ��ĸ��m��',m)
    s1=[]
    for i in s:
        s1.append(i)
    print('����s1��',s1)
    d=xiabiao(s1,m)
    kk(d,m)

def xiabiao(s1,m):
    d=[]
    i=0
    while i<len(s1):
        j=0
        while j<len(m):
            if s1[i]==m[j]:
                d.append(j)
                break
            j+=1
        i+=1
    print('��ԭʼ��ĸ����±�d��',d)
    return d

def kk(d,m):
    k1=list(range(1,26))
    for i in k1:
        ny = input('�����жϣ�')
        if ny == 'n' or ny == 'N':
            d1 = []
            for j in d:
                sum = 0
                sum = j + i
                if sum >= 26:
                    sum = sum - 26
                    d1.append(sum)
                else:
                    d1.append(sum)
            print('��λ�Ĵ�����',i)
            print('d1:',d1)
            shangbaio(d1, m)
            if i==25:
                ny = input('�����жϣ�')
                if ny == 'n' or ny == 'N':
                    print('��������ʧ��')
        if ny == 'y' or ny == 'Y':
            print('��������ɹ�')
            #print('��λ����ԭʼ��ĸ����±�d1��',d1)
            break

def shangbaio(d1,m):
    e=[]
    i=0
    while i<len(d1):
        j=0
        while j<len(m):
            if d1[i]==j:
                e.append(m[j])
            j+=1
        i+=1
    print('���ģ�',e)

main()
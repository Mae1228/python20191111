d='    sjjj    '.strip()
print(d)
import io
s='hhhj.kij'
sio=io.StringIO(s)
print(sio)
print(sio.getvalue())
print(sio.seek(4))
sio.write('v')
print(sio.getvalue())
a=3
print(a<<3)
f=[5,6,7]
f1=['d',8]
f.extend(f1)
print,(f),
c=[11,22,33,44,55,66,77,88,99,100,111,222,333,444,555,666,777,888,999]
print(c[-5:])
print(c[:-5])
c1='zxcvbnmasdfghjklqwertyuiop'
print(c1[2:])
dict={
    'name':'zzzz',
    'age':65,
    'sex':'f',
    'grade':3
}
a,b,c,d=dict.values()
print(a,b,c,d)
e,f,g,h=dict.items()
print(e,f,g,h)
print(type(e))
print(e[0],e[1])
c=int(input('fenshu'))
if c<100 and c>90:
    s='youxiu'
elif c>70 and c<90:
    s='lianghao'
print('s{0},c{1}'.format(c,s))
print('s{0},c{1}'.format(s,c))
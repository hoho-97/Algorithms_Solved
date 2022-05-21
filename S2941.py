word = input()
a = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in range(8):
    word = word.replace(a[i],'.')
print(len(word))
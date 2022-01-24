c=float(input('initial investment '))
r=.01
t=float(input('duration '))
n=float((input('times compounded per year ')))
p=c*(1+r/n)**(t*n)
v=round(p,2)
print('final value ',p)









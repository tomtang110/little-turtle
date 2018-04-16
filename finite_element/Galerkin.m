syms x a1 a2 a3
u=a1*x+a2*x^2+((1-a1-2*a2)/3)*x^3 % the ploynominal of u
w1=diff(u,a1)
w2=diff(u,a2)
d2=diff(u,x,2)
R=-d2-u+x^2
B=int(R*w1,x,1,0)
C=int(R*w2,x,1,0)
A=solve(B==0,C==0,a1,a2)
aa1=A.a1
aa2=A.a2
aa3=((1-aa1-2*aa2)/3)
u=aa1*x+aa2*x^2+aa3*x^3 % obtain the expression for u
u_5=vpa(subs(u,x,0.5))

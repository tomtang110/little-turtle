syms x a1 a2 a3
R=x+(-2+x-x^2)*a1+(-2+6*x-x^2+x^3)*a3
B=int(R*1,x,1,0)
C=int(R*x,x,1,0)
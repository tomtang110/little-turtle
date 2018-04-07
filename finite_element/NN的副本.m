function [B]=NN(x)
syms x1 y1 x2 y2 x3 y3 x y
x1=0.;x2=0.;x3=1.;
y1=0.;y2=2.;y3=1.;
fT=[1,x,y];
C=[1 x1 y1;1 x2 y2;1 x3 y3];
C1=C^-1;
B=fT*C1;
end
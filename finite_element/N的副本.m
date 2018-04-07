function [B]=N(x,y)
syms x1 x2 x3 x4 x5 
syms y1 y2 y3 y4 y5 
x1=0.;,x2=2.;,x3=2.;,x4=0.;,x5=1.;
y1=0.;,y2=0.;,y3=2.;,y4=2.;,y5=1.;
fT=[1,x,y,x^2,x*y];
C=[1 x1 y1 x1^2 x1*y1;...
    1 x2 y2 x2^2 x2*y2;...
    1 x3 y3 x3^2 x3*y3;...
    1 x4 y4 x4^2 x4*y4;...
    1 x5 y5 x5^2 x5*y5];
C1=C^-1;
B=fT*C1;
end
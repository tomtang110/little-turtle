clear all
clc
syms x1 x2 x3 y1 y2 y3 x y 
f_xy=[1 x y];
C=[1 x1 y1;1 x2 y2;1 x3 y3];
C_transp=C^(-1);
N=f_xy*C_transp;
N_T=transpose(N);
N_xy=[diff(N_T(1),x);diff(N_T(1),y);diff(N_T(2),x);diff(N_T(2),y);...
    diff(N_T(3),x);diff(N_T(3),y)];
B_e=vpa(zeros(2,3));
B_e(1,1)=N_xy(1);B_e(1,2)=N_xy(3);B_e(1,3)=N_xy(5);
B_e(2,1)=N_xy(2);B_e(2,2)=N_xy(4);B_e(2,3)=N_xy(6);
B_real1=double(subs(B_e,[x1,y1,x2,y2,x3,y3],[0,0,2,0,1,1]));
B_real2=double(subs(B_e,[x1,y1,x2,y2,x3,y3],[0,2,0,0,1,1]));
B_real3=double(subs(B_e,[x1,y1,x2,y2,x3,y3],[2,2,0,2,1,1]));
B_real4=double(subs(B_e,[x1,y1,x2,y2,x3,y3],[2,0,2,2,1,1]));
A=det([1 1 1;x1 x2 x3;y1 y2 y3])/2;
A_real=double(subs(A,[x1,y1,x2,y2,x3,y3],[0,2,0,0,1,1]));
t=1;
k=25*10^(-5);
V_real1=k*B_real1*A_real;
number=[125,415,345,235];
B={B_real1,B_real2,B_real3,B_real4};
K=zeros(5);
for e = 1:length(B)
    tmp = cell2mat(B(e))
    n = number(e)
    Q_K = zeros(5)
    C = Bb(n,tmp)
    K = K + Q_K
end




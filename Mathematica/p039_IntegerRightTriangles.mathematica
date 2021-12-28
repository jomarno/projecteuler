A=Table[{p,Length[Solve[{a+b+c==p,a^2+b^2==c^2,Element[{a,b,c},PositiveIntegers]},{a,b,c}]]},{p,12,1000}];
A[[Position[A[[;;,2]],Max[A[[;;,2]]]][[1,1]],1]]
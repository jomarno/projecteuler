factorials = Table[k!, {k,0,9}];
Total[Table[If[k == Total[factorials[[IntegerDigits[k]+1]]], k, 0], {k,3,10^7}]]
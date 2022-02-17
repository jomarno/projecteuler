A = Flatten[Table[Table[
        Catch[
            n = 0;
            While[PrimeQ[n^2+a*n+b], n++];
            Throw[{n, a*b}]
        ],
        {a, -b, 1000, 2}],
        {b, Table[Prime[n], {n, 1, PrimePi[1000]}]}
    ], 1];
    
A[[Ordering[A[[;;, 1]], -1][[1]], 2]]
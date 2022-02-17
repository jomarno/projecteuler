powers = Table[k^5, {k,0,9}];

Total[
    Table[
        If[k == Total[powers[[IntegerDigits[k]+1]]], 
            k, 
            0
        ], 

        {k, 10, 10^6}
    ]
]
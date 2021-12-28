Length[
    Solve[
        {
            p1/100 + p2/50 + p5/20 + p10/10 + p20/5 + p50/2 + P1 + 2 P2 == 2, 
            Element[{p1, p2, p5, p10, p20, p50, P1, P2}, NonNegativeIntegers]
        },
        {p1, p2, p5, p10, p20, p50, P1, P2}
    ]
]
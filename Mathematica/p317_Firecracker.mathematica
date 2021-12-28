f[x_, y_, \[Theta]_] := ((y0 + v0 Sin[\[Theta]] t - 1/2 g t^2 - y) /. t -> x/(v0 Cos[\[Theta]]))
Y = Simplify[Solve[{f[x, y, \[Theta]] == 0, D[f[x, y, \[Theta]], \[Theta]] == 0}, {y, \[Theta]}]][[1, 1, 2]];
Print[DecimalForm[N[(2 Pi*Integrate[x Y, {x, 0, Solve[Y == 0, x][[2, 1, 2]]}] /. {g -> 981/100, v0 -> 20, y0 -> 100}), 11]]]
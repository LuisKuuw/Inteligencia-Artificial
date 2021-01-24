function ENUMERATION-ASK(X , e, bn) returns a distribution over X
inputs: X , the query variable
e, observed values for variables E
bn, a Bayes net with variables vars
Q(X ) ← a distribution over X , initially empty
for each value xi of X do
Q(xi) ← ENUMERATE-ALL(vars, exi )
where exi is e extended with X = xi
return NORMALIZE(Q(X))
function ENUMERATE-ALL(vars, e) returns a real number
if EMPTY?(vars) then return 1.0
V ← FIRST(vars)
if V is an evidence variable with value v in e
then return P (v | parents(V )) × ENUMERATE-ALL(REST(vars), e)
else return
P
v
P (v | parents(V )) × ENUMERATE-ALL(REST(vars), ev)
where ev is e extended with V = v
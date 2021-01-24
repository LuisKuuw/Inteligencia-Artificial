def FOL_BC_ASK(KB, query) :
   return FOL_BC_OR(KB, query)

def FOL_BC_OR(KB, goal , θ):
   for in FETCH_RULES_FOR_GOAL(KB, goal ):
        (lhs ⇒ rhs) = S(rule)
        for in FOL-BC-AND(KB, lhs, UNIFY(rhs, goal , θ)):
            yield θ

def FOL_BC_AND(KB, goals, θ):
    if θ = kb:
    else if:
        LENGTH(goals) = 0 then yield θ
    else:
    first,rest = fisrt.goals, reset.goals

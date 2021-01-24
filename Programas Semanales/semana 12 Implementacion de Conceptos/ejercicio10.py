Init(Tire(Flat ) ∧ Tire(Spare) ∧ At(Flat, Axle) ∧ At(Spare, Trunk ))
Goal (At(Spare, Axle))
Action(Remove(obj , loc),
PRECOND: At(obj , loc)
EFFECT: ¬ At(obj , loc) ∧ At(obj , Ground))
Action(PutOn(t, Axle),
PRECOND: Tire(t) ∧ At(t, Ground) ∧ ¬ At(Flat, Axle) ∧ ¬ At(Spare, Axle)
EFFECT: ¬ At(t, Ground) ∧ At(t, Axle))
Action(LeaveOvernight ,
PRECOND:
EFFECT: ¬ At(Spare, Ground) ∧ ¬ At(Spare, Axle) ∧ ¬ At(Spare, Trunk)
∧ ¬ At(Flat, Ground) ∧ ¬ At(Flat, Axle) ∧ ¬ At(Flat, Trunk))
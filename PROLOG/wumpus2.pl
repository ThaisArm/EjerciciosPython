% Hechos
oro(0, 3).
pozo(1, 5).
pozo(3, 1).
pozo(3, 4).
pozo(5, 4).
wumpus(1, 2).
:- dynamic explorador/2.

posicion_inicial(X,Y):-retractall(explorador(_,_)), assert(explorador(X,Y)).
ver_posicion(X,Y):-call(explorador(X,Y)).
adyacente(X1, Y1, X2, Y2) :- (X1 =:= X2, abs(Y1 - Y2) =:= 1) ; (Y1 =:= Y2, abs(X1 - X2) =:= 1).


mover_arriba(X, Y) :- X > 0, X1 is X - 1, assert(explorador(X1,Y)),retract(explorador(X,Y)),!.
mover_abajo(X, Y) :- X < 4, X1 is X + 1, assert(explorador(X1,Y)),retract(explorador(X,Y)),!.
mover_derecha(X, Y) :- Y < 4, Y1 is Y + 1, assert(explorador(X,Y1)),retract(explorador(X,Y)),!.
mover_izquierda(X, Y) :- Y > 0, Y1 is Y - 1, assert(explorador(X,Y1)),retract(explorador(X,Y)),!.

brisa(X, Y) :- pozo(X1, Y1), adyacente(X, Y, X1, Y1).
hedor(X, Y) :- wumpus(X1, Y1), adyacente(X, Y, X1, Y1).

ganaste(X, Y) :-oro(X, Y).
perdiste(X,Y) :- pozo(X,Y); wumpus(X,Y).

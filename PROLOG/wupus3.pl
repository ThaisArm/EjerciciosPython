oro(0, 3).
pozo(1, 5).
pozo(3, 1).
pozo(3, 4).
pozo(5, 4).
wumpus(1, 2).
:- dynamic explorador/2.

posicion_inicial(X,Y):-retractall(explorador(_,_)), assert(explorador(X,Y)).
ver_posicion(X,Y):-call(explorador(X,Y)).

%define las posiciones que puede tener
abajo(X, Y, X1, Y) :- X < 5, X1 is X + 1.
arriba(X, Y, X1, Y) :- X > 0, X1 is X - 1.
derecha(X, Y, X, Y1) :- Y < 5, Y1 is Y + 1.
izquierda(X, Y, X, Y1) :- Y > 0, Y1 is Y - 1.

%define las posicones adyascentes
adyacente(X,Y,X1,Y1) :- abajo(X, Y, X1, Y1);arriba(X, Y, X1, Y1);izquierda(X, Y, X1, Y1);derecha(X, Y, X1, Y1).

%si la posicion X1,Y1(pozo) tiene como adyascente a X,Y entonces X,Y en brisa - lo mismo con hedor
es_brisa(X, Y, X1,Y1) :- pozo(X1, Y1), adyacente(X1, Y1, X, Y).
es_hedor(X, Y, X1,Y1) :- wumpus(X1, Y1), adyacente(X1, Y1, X, Y).
brillo(X, Y) :- oro(X, Y).

mover_arriba(X, Y) :- X > 0, X1 is X - 1, assert(explorador(X1,Y)),retract(explorador(X,Y)),!.
mover_abajo(X, Y) :- X < 4, X1 is X + 1, assert(explorador(X1,Y)),retract(explorador(X,Y)),!.
mover_derecha(X, Y) :- Y < 4, Y1 is Y + 1, assert(explorador(X,Y1)),retract(explorador(X,Y)),!.
mover_izquierda(X, Y) :- Y > 0, Y1 is Y - 1, assert(explorador(X,Y1)),retract(explorador(X,Y)),!.

%Si X,Y es brisa en cualquier poso A,B , el explorador esta en la posicion X1,Y1 y el explorador tiene como adyascente a la brisa entonces hay una brisa al rededor y por consecuente hay un pozo cerca
brisa_alrededor(X, Y, X1,Y1) :-es_brisa(X,Y,A,B), explorador(X1, Y1), adyacente(X1, Y1, X, Y).
hedor_alrededor(X, Y, X1,Y1) :-es_hedor(X,Y,A,B), explorador(X1, Y1), adyacente(X1, Y1, X, Y).
brillo_alrededor(X, Y, X1,Y1) :-brillo(X,Y), explorador(X1, Y1), adyacente(X1, Y1, X, Y).

ganaste(X, Y) :-oro(X, Y).
perdiste(X,Y) :- pozo(X,Y); wumpus(X,Y).



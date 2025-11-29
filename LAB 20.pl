% By SriJan Karki

% --- Facts ---
male('Ram').
male('Shyam').
male('Sujan').
male('Ramesh').

female('Sita').

female('Sita').
female('Gita').
female('Emma').
female('Olivia').

parent('Sita', 'Gita').
parent('John', 'David').
parent('Mary', 'David').
parent('John', 'Emma').
parent('Mary', 'Emma').
parent('David', 'Michael').
parent('Olivia', 'Michael').
parent('Emma', 'James').

sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
female('Emma').
female('Olivia').

parent('John', 'David').
parent('Mary', 'David').
parent('John', 'Emma').
parent('Mary', 'Emma').
parent('David', 'Michael').
parent('Olivia', 'Michael').
parent('Emma', 'James').
father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
grandfather(X, Y) :- male(X), grandparent(X, Y).
grandmother(X, Y) :- female(X), grandparent(X, Y).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
brother(X, Y) :- male(X), sibling(X, Y).
sister(X, Y) :- female(X), sibling(X, Y).


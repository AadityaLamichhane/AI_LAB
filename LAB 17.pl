% By Aaditya Lamichhane

% --- GCD first ---
gcd(A, 0, A) :- A > 0.
gcd(A, B, G) :-
    B > 0,
    R is A mod B,
    gcd(B, R, G).

% --- LCM using GCD ---
lcm(A, B, LCM) :-
    gcd(A, B, G),
    LCM is (A * B) // G.

% --- Interactive version ---
lcm_calc :-
    write('Enter first number: '), read(A),
    write('Enter second number: '), read(B),
    lcm(A, B, LCM),
    write('LCM of '), write(A), write(' and '), write(B),
    write(' is '), write(LCM), nl.


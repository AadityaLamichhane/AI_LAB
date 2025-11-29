#! /usr/bin/perl
% addition.pl
% By Aaditya lamichhane

% Rule to add two numbers
add_numbers(X, Y, Sum) :-
    Sum is X + Y.

% Start rule to take input and show output
start :-
    write('Enter first number (X): '), flush_output(current_output), read(X),
    write('Enter second number (Y): '), flush_output(current_output), read(Y),
    add_numbers(X, Y, Sum),
    write('The sum of '), write(X), write(' and '), write(Y),
    write(' is: '), write(Sum), nl.


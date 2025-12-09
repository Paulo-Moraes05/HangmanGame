-module(simple_script).
-export([hello_world/0, factorial/1]).

% Function to print "Hello, World!"
hello_world() ->
    io:format("Hello, World!~n").

% Recursive function to compute factorial of N
factorial(0) ->
    1;
factorial(N) when N > 0 ->
    N * factorial(N - 1).

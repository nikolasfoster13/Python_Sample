# Fuel Gauge
Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

fuel.py is a program that prompts the user for a fraction formatted as "x/y", wherein x is a non-negative integer and y is a positive integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, the program outputs "E" instead to indicate that the tank is essentially empty. If 99% or more remains, teh program outputs "F" to indicate that the tank is essentially full.

If, though, x or y is not an integer, x is greater than y, or y is 0, the program reprompts the user. 
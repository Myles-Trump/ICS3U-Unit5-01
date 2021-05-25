#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program converts celsius into fahrenheit


def celsius_to_fahrenheit():

    celsius = int(input("Please enter the temperature (°C): "))

    fahrenheit = (9 / 5) * celsius + 32

    print("\nIt is {0}°F".format(fahrenheit))


def main():
    # this function calls other functions
    # call fucntions
    celsius_to_fahrenheit()


if __name__ == "__main__":
    main()

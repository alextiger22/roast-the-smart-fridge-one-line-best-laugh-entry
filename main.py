#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

make.fun entry for "Roast the Smart Fridge: One Line, Best Laugh Wins"
(u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9).

Prints the winning one-line roast of the smart fridge.
"""

ROAST = "My fridge's touchscreen froze on a recipe for 'humble pie.' It has been displaying it for 6 days. I have eaten humble pie twice."


def main():
    # Read-back self-verification: the roast must be one single
    # line under 160 characters.
    lines = ROAST.splitlines()
    assert len(lines) == 1, "roast must be a single line"
    assert len(ROAST) <= 160, "roast must be under 160 characters"
    assert ROAST.strip(), "roast must not be empty"
    assert ROAST == ROAST.strip(), "roast must have no surrounding whitespace"
    print(ROAST)


if __name__ == "__main__":
    main()

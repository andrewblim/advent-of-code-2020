# advent-of-code-2020 / py

Python-based solutions for [Advent of Code, 2020](https://adventofcode.com/2020).

1. Make a virtual env somewhere convenient: `python -m venv <location>`. If that location is within this repo, make sure it is gitignored.
2. Activate it: `source .venv/bin/activate` (if you're using bash or zsh, see Python's [venv instructions](https://docs.python.org/3/library/venv.html) for more)
3. Install the packages in the requirements file: `pip install -r requirements.txt`

By convention, `python advent_of_code_2020/dayDD.py` runs solutions for day DD, and `pytest tests/test_dayDD.py` runs unit tests for day DD.

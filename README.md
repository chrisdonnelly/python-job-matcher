# python-job-matcher

A basic project to parse JSON data and output job recommendations.

## Install

- Python 3.10+ - the best way to install it is [pyenv installer](https://github.com/pyenv/pyenv-installer#readme)

- Make sure you have Python 3.10:

```bash
$ python --version
```

You will also need a system-wide installation of [poetry](https://python-poetry.org/):

```bash
# Create a virtualenv.
$ python -m venv .venv
# We now have to activate it:
$ source .venv/bin/activate
# Install Python package dependencies etc.
$ poetry install
```

## Tooling
```bash
# Format files 
$ black src
# Type checking
$ mypy src
```

## Run
To run the script...
```bash
$ poetry run python src/main.py
```

## Notes

This is simple implementation given the parameters of the exercise.  There are some
considerations to bear in mind.

* I've approached the question as through we are dealing with a real application and tried to consider the data
in that context.

* We'll use Black to ensure consistent formatting and MyPy for static type checking.

* There are key basic steps in the application:
  * Retrieve our JSON data via an api call.
  * Process that data from raw JSON to some values that more closely align with our domain that the application can understand.
  * Use our domain data to perform some comparisons and operations to arrive at a result set. 

* We ideally would not want to capture data in the form of strings as exemplified by the members 
biographies.  Here our users are providing key values we need to perform our operations hidden
in lengthy string objects.  Ideally we want our users to be supplying us with pre-defined values captired by our FE that the
application expects and understands.

* We would then want to store these values in appropriate tables in a database to allow better quering and analysis.  

* It's difficult to extract meaning and values from long strings thus we perform some 
operations on the strings to make them more alike, easier to compare and to extract some meaningful values that the application
can understand.

* In this example I've opted to implement a very simple 'scoring' system for each job, based 
on the values we can extract from our member bios and how those value match against the data held in our job profiles.

* The current scoring function/algorithm has not been optimised for performance.  We have
a number of nested of loops that could be extracted and optimised with more time.

* The recommendations algorithm does not account for members having a preference of one location
over another, where such information has been provided in the biography.  It's not possible for the
application to interpret the biography and understand the members intention when naming more than one location
and expressing a preference.  This is the kind of data we would want our FE client to collect in a more
meaningful way, preferably using some shared values our BE application understands.

* Therefore, our member Daisy's recommendations include a job in her current location despite her looking to relocate.

* A note on testing - ideally we should unit test our functions using pytest or a similar testing tool.  Unit tests would
help us iterate towards a more comprehensive and performative solution. 

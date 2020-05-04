# Python Guidelines

Python guides below are based off of the source [The Hitchhiker’s Guide to Python](https://docs.python-guide.org/writing/style/)
and the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide. Please visit their website for additional examples to the below information.

## *Python Rules and Examples*

Below are a list of items from the two sources mentioned above that are important examples and rules to follow for the project.

### Indentation

Spaces are the preferred indentation method over tabs. Please use 4 spaces per indentation level.

Limit all lines to a maximum of 79 characters.
The preferred way of wrapping long lines is by using Python's implied line continuation inside parentheses, brackets and braces

Below is an example of indentation aligned with opening delimiter:

```python
foo = example_function_name(variable_one, variable_two,
                         variable_three, variable_four)
```

Add a level to hanging indents:
```python
foo = example_function_name(
    variable_one, variable_two,
    variable_three, variable_four)
```

Break **before** binary operators:
```python
rating_sum = (
           + rating_one
           + rating_two
           - rating_takeaway)
```

You can close braces, brackets, and parenthesis to line up under the first non-whitespace character
of the last line in the list or you may line it up under the first character of the line in the construct.
Also, trailing commas are optional, but when you need to include them:

```python
# Example 1
my_list_one = [
    1, 2, 3,
    4, 5, 6,
    ]

# Example 2
my_list_two = [
    1, 2, 3,
    4, 5, 6,
]   
```

### Imports

Place imports at the top of the file after module comments and docstrings, but before globals and constants.
They should also be grouped in the following order: Standard library imports, related third party imports, and local 
application/library specific imports.

Please separate imports accordingly:
```python
# Correct:
import os
import sys

# Incorrect:
import sys, os
```

Module level dunder names with two leading and two trailing underscores
shall be placed after the module docstring but before any import statements

### Blank Lines

Please follow these general rules for blank lines in the code:
- Top-level function and class definitions shall have **two** blank lines.
- Method definitions inside a class shall be surrounded by **one** blank line.
- Use extra blank lines sparingly to divide groups of related functions.
- Blank lines can be omitted if between many related one lined implementations.
- Always surround binary operators with a **one** space on both sides: 
assignment, augmented assignment, comparisons, and booleans.
- Do **NOT** use spaces around the = sign to make a keyword argument.
- If an assignment has a right hand side, then the equality sign should have exactly **one** space on both sides.

```Python
# Correct
class Point:
    coords: Tuple[int, int]
    label: str = '<unknown>'
```


### Commenting

Please follow these general rules for commenting in the code:
- All comments shall be written in **English**.
- After a sentence-ending period, use **two** spaces to start a new sentence.
- Do not contradict comments with the code. Update comments when code updates!
- Make comments in complete sentences. Use capitalization and periods.
- For block comments:
  - Each line of a block comment shall start with a # and a single space.
  - Separate paragraphs by using one #.
- Use inline comments sparingly.
- Do not make comments to just state the obvious! e.g:
```python
x = x + 1                 # Increment x
```

### Documentation
Please use docstrings for all public modules, functions, classes, and methods.
The """ that ends a multiline docstring should be on a line by itself. For one liner docstrings, 
please keep the closing """ on the same line.

Example:
```Python
"""Return a movie_type

Additional docstring commentation here
"""
```

### Naming Convention

- Do not use the following characters solely as variable names: 'l' (lowercase letter el), 
'O' (uppercase letter oh), or 'I' (uppercase letter eye)
- Modules shall have all lowercase names. Underscores can be used for a module name.
- Python packages shall have all lowercase names. Do not use underscores if possible.
- Class names shall use CapWords naming convention.
- Type variables shall be CapWords naming convention.
- For exceptions, use CapWords naming convention with the suffix "Error" on the exception name.
- Variable names shall be lowercase with words separated by underscores. The use of mixedCase for naming convention 
is also permitted.
- Function names shall be lowercase with words separated by underscores.
  - Arguments shall use self for the first argument for instance methods.
  - Arguments shall use cls for the first argument for class methods.
  - When argument name is in violation with another reserved name, append with a single trailing underscore.
- For method names and instance variables:
  - Use lowercase words separated by underscores.
  - Use one leading underscore only for non-public methods and instance variables.
  - Use two leading underscores to avoid clashes with subclasses.
- Constant names shall be in all capital letters with underscores separating words.
- For inheritance naming convention:
  - Public attributes shall not have any leading underscores.
  - Use a single trailing underscore added to the attribute name if it clashes with a reserved word.
  - If subclass, use double leading underscores and no trailing underscore for attributes.

### Statement and Expressions
In general, do not keep disjointed statements on one line. Please separate them!
```python
 print 'statement one'
 print 'statement two'
 
 if x == 1:
     print 'statement one'
 
 condition1 = <complex comparison>
 condition2 = <other complex comparison>
 if condition1 and condition2:
     # do something
```

Comparisons to singletons like None should always be done with is or is not, never the equality operators. Use is not 
operator rather than not ... is. 
```python
# Correct:
if foo is not None:
# Incorrect:
if not foo is None:
```

Use the most the explicit and straightforward manner in statements
```python
# Correct:
def make_complex(x, y):
    return {'x': x, 'y': y}
# Incorrect:
def make_complex(*args):
    x, y = args
    return dict(**locals())
```

Do not compare boolean values to True or False using ==
```python
# Correct:
if greeting:
# Incorrect:
if greeting == True:
# Incorrect:
if greeting is True:
```


### Functions

Either all return statements in a function should return an expression, 
or none of them should. If any return statement returns an expression, 
any return statements where no value is returned should explicitly state this as return None, 
and an explicit return statement should be present at the end of the function (if reachable):

```Python
# Correct:

def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)
```


## *Sources Cited*

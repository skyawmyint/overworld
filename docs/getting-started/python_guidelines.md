# Python Guidelines

Python guides below are based off of the source [The Hitchhiker’s Guide to Python](https://docs.python-guide.org/writing/style/)
and the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide. Please visit their website for additional examples to the below information.

## *Python Rules and Examples*

Below are a list of items from the two sources mentioned above that are important examples and rules to follow for the project.

### Indentation

Spaces are the preferred indentation method over tabs. Please use 4 spaces per indentation level.

Limit all lines to a maximum of 79 characters.
The preferred way of wrapping long lines is by using line continuation inside parentheses, brackets and braces.

Below is an example of indentation aligned with opening delimiter:

```python
example_delimiter = example_function_name(variable_one, variable_two,
                         variable_three, variable_four)
```

Add a level to hanging indents:
```python
example_hanging = example_function_name(
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

Module level dunder names that have two leading and two underscores after it
shall be placed **after** the module docstring but before any import statements.

### Blank Lines

Please follow these general rules for blank lines in the code:
- Top-level function and class definitions shall have **two** blank lines.
- Method definitions inside a class shall be surrounded by **one** blank line.
- Use extra blank lines sparingly to divide groups of related functions.
- Blank lines can be omitted if between many related one lined implementations.
- Always surround binary operators with a **one** space on both sides: 
assignment, augmented assignment, comparisons, and booleans.
```python
# Correct:
if movie_score == 10: print movie_score, movie_average; movie_score, movie_average = movie_average, movie_score
```
- Do **NOT** use spaces around the = sign to make a keyword argument.
```python
# Correct:
func(1, 2, movie_name='Kill Bill', rating=5, duration=120)
```
- If an assignment has a right hand side, then the equality sign should have exactly **one** space on both sides.
```Python
# Correct
class Movie:
    coords: Tuple[int, int]
    label: str = '<unknown>'
```

### Commenting

Please follow these general rules for commenting in the code:
- All comments shall be written in **English**.
- After a sentence-ending period, use **two** spaces to start a new sentence.
- Do not contradict comments with the code. Update comments when code updates!
```Python
# Incorrect
# The below code adds together ratings
rating_sum = (rating_one
          - rating_two
          - rating_three
          - rating_four)
```
- Make comments in complete sentences. Use capitalization and periods.
```Python
# Incorrect
# the Following code beloW adds together ratings for the Movies

# Correct
# The following code below adds together ratings for the movies.
```

- For block comments:
  - Each line of a block comment shall start with a # and a single space.
  - Separate paragraphs by using one #.
```Python
# Correct
# This is the first line of the block comment.
# This is he second line of the block comment.
# The below line is used to separate paragraphs.
#
# This is the second paragraph for the block comment.
```
- Use inline comments sparingly.
- Do not make comments to just state the obvious! e.g:
```python
# Incorrect:
x = x + 1                 # Increment x
```

### Documentation
Please use docstrings for all public modules, functions, classes, and methods.
The """ that ends a multiline docstring should be on a line by itself. For one liner docstrings, 
please keep the closing """ on the same line.
```Python
"""Return a movie_type

Additional docstring commentation here
"""
```

### Naming Convention

- Do not use the following characters solely as variable names: 'l' (lowercase letter el), 
'O' (uppercase letter oh), or 'I' (uppercase letter eye)
```Python
# Incorrect
l = 100
O = 50
I = 50
```
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

From https://google.github.io/styleguide/pyguide.html#316-naming, please see the naming convention examples below:
```Python
# Correct naming conventions below from:
# module_name, package_name, ClassName, method_name, ExceptionName, 
# function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, 
# function_parameter_name, local_var_name
```

### Statement and Expressions
In general, do not keep disjointed statements on one line. Please separate them!
```python
 print 'I like this movie'
 print 'I do not like this movie'
 
 if x == 1:
     print 'I like this movie'
 
 condition1 = <complex comparison>
 condition2 = <other complex comparison>
 if condition1 and condition2:
     # do something
```
Comparisons to singletons like None should always be done with is or is not, never the equality operators. Use is not 
operator rather than not ... is. 
```python
# Correct:
if like is not None:
# Incorrect:
if not like is None:
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
For more on function guidelines, see [PEP 484](https://www.python.org/dev/peps/pep-0484/)

### Variable Annotations

Local and global variable annotations can be as follow:
```python
some_number: int           # variable without initial value
some_list: List[int] = []  # variable with initial value
```
You can omit the initial value of variables assigned in conditional branches:
```python
good_review: bool
if movie_score >= 8:
    good_review = True
else:
    good_review = False
```
Type annotations shall be used to annotate class and instance variables in class bodies and methods.
```python
class BasicMovie:
    movie: str = 'Frozen'                 # instance variable with default
    review_score: int                     # instance variable without default
    stats: ClassVar[Dict[str, int]] = {}  # class variable
```
For more on variable annotation guidelines, see [PEP 526](https://www.python.org/dev/peps/pep-0526/)

## *Sources Cited*
1. Van Rossum, Guido. Warsaw, Barry. Coghlan, Nick. https://www.python.org/dev/peps/pep-0008/. 
PEP 8 -- Style Guide for Python Code. 05-Jul-2001
2. Van Rossum, Guido. Lehtosalo, Jukka. Langa, Łukasz. https://www.python.org/dev/peps/pep-0484/.
PEP 484 -- Type Hints. 29-Sep-2014
3. Gonzalez, Ryan. House, Philip. Levkivskyi, Ivan. Roach, Lisa. Van Rossum, Guido.
https://www.python.org/dev/peps/pep-0526/.
PEP 526 -- Syntax for Variable Annotations. 09-Aug-2016
4. Reitz, Kenneth. Real Python. https://docs.python-guide.org/writing/style/
The Hitchhiker’s Guide to Python. 2011-2020
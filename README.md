![Redex logo](https://github.com/TimoKats/medium_articles/blob/af07ef68b66154dda45badd530592cd28296af98/img/RedexLogo.png)

Redex is a Python library that aims to be a readable and scalable replacement of regular expressions (regex). It uses boolean operators and built-in functionalities to create expressions.

### Installation
Redex can be installed through the Python package installer (PyPi). It doesn't have any dependencies outside of the standard Python library. It requires Python 3.8 as a minimum Python version.

```python
pip3 install python-redex
```

Next, importing redex is suggested to do as follows.

```python
import redex as rd
```

### Usage and examples
Redex has three main actions: has (returns boolean), find (returns strings/locations/tuples) and count (returns int). For example, a Redex query that finds all words that start with an uppercase character and contain an hyphen can be formulated as follows.

```python
rd.find('startswith:*upper and contains:-', string)
```

Next, a Redex query that checks for the occurence of characters on specific locations and max proximity of upper- and lowercase characters can be formulated as follows.

```python
rd.find('(location:{o,1} or location:{a,1}) and proximity:{*upper,*lower}3', string)
```

Finally, a (commonly used) Redex query that finds email addresses in text can be formulated as follows. 

```python
rd.find('sequence:{*alpha,@,.com} or sequence:{*alpha,@,.co.uk}', string)
```

A complete tutorial/list of examples can be found in `demo.ipynb` (see files of this repository). 

### Docs
This section documents the different components of Redex. Namely, the splitter, the built-in actions, the wildcards and the multi-threaded searching.

#### Split
The splitter creates subqueries (often words or sentences) to conduct the Redex queries on. By default, this is set to a space (' ') with a granularity of 1. Setting multiple splitting characters can be done through adding a list. For example, adding punctuation: `split=['.',',',' ']`. 

Next, the granularity refers to the amount of splitting characters needed to actually split the string in subqueries. By default, this is set to 1 (and it can only be **in**creased). For example, findings substrings where two consecutive words start with an uppercase character can be formulated as follows `rd.find('count:{*upper,2}', string, granularity=2)` 

#### Actions
Redex has a number of built-in functionalities that can be used in a boolean expression/Redex query. This subsection gives an overview of these functionalities.

| Name                                            | Description                                                                    |
|-------------------------------------------------|--------------------------------------------------------------------------------|
| startswith:*substring*                          | Return True if string starts with substring                                    |
| endswith:*substring*                            | Return True if string ends with substring                                      |
| contains:*substring*                            | Return True if string contains substring                                       |
| count:{*substring*,*int*}                       | Return True if string contains at least *n* occurences of the substring        |
| proximity:{*substring1*, *substring2*,...}*int* | Return True if max proximity between substring is less than the threshold/int  |
| sequence:{*substring1*,*substring2*,...}        | Return True if sequence of substrings exists in string                         |
| location:{*substring*,*location*}               | Return True if substring occurs on location                                    |


#### Wildcards
By default, the substrings can be implemented using the following wildcards. Note, you can add wildcards yourself. For example, say you want to add a wildcard for countries that you can do that as follows: `rd.wildcard['*country'] = ['United States','Canada','United Kingdom']`.

| Name     | Description                |
|----------|----------------------------|
| *        | Any *thing*                |
| *num     | Any *number*               |
| *alpha   | Any *alphabetic character* |
| *upper   | Any *uppercase character*  |
| *lower   | Any *lowercase character*  |
| *special | Any *special character*    |
| *space   | Any *whitespace*           |
| *punt    | Any *punctuation*          |

#### Multi-threaded searching
The search operations can be executed conurrently. This allows Redex to scale better than regular expressions. However, finding the optimal number of threads can be a tedious process, since it requires knowledge of your CPU (cores/threads). Hence, as a general rule of thumb, don't touch this unless you really know what you're doing.

```python
# increases the search operations executed concurrently to 4
rd.find('count:{*upper,2}', string, granularity=2, threads=4)
```

### Contact and future updates
This library is maintained by Timo Kats as a **side** project. If you have any suggestions feel free to reach out or fork the repository.  

Future updates
- Error handling
- Multiple wildcards

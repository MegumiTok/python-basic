# re — Regular expression operations[^1]

## `.` (Dot.)

In the default mode, this matches any character except a newline. <br>
If the DOTALL flag has been specified, this matches any character including a newline.

## `^`(Caret.)

Matches the start of the string, and in `MULTILINE` mode also matches immediately after each newline.

## `$`

Matches the end of the string or just before the newline at the end of the string, and in `MULTILINE` mode also matches before a newline.

など***多数***あるので詳しくは[公式ドキュメントに詳しい](https://docs.python.org/3/library/re.html)

## `\b`

Matches the empty string, but only at the beginning or end of a word.
>(Note that \b is used to represent word boundaries, and means “backspace” only inside character classes.)

## `\B`

Matches the empty string, but only when it is ***not*** at the beginning or end of a word.

## `\Z`

Matches only at the end of the string.

## `[]`

Used to indicate a set of characters. In a set:

- Characters can be listed individually, e.g. `[amk]` will match 'a', 'm', or 'k'.

- Special characters lose their special meaning inside sets.
For example, `[(+*)]` will match any of the literal characters '(', '+', '*', or ')'.

参考記事: [re.findall("\w+[\s$]", "green pears")の出力](https://stackoverflow.com/questions/12763548/python-regex-why-does-end-of-string-and-z-not-work-with-group-expressions)

## `(?:...)`

A non-capturing version of regular parentheses. Matches whatever regular expression is inside the parentheses, but the substring matched by the group cannot be retrieved after performing a match or referenced later in the pattern.

# Lookahead and Lookbehind

| Lookaround | Name|Description |
| --- | --- |--- |
| (?=foo)| Lookahead| Asserts that what immediately ***follows*** the current position in the string is foo|
| (?<=foo)| Lookbehind| Asserts that what immediately ***precedes*** the current position in the string is foo|
| (?!foo)| Negative Lookahead| Asserts that what immediately follows the current position in the string is ***not*** foo|
| (?<!foo)| Negative Lookbehind| Asserts that what immediately precedes the current position in the string is ***not*** foo|

# Functions

## re.search(pattern, string, flags=0)

Scan through string looking for the first location where the regular expression pattern produces a match, and return a corresponding match object.

## re.match(pattern, string, flags=0)

If zero or more characters at the beginning of string match the regular expression pattern, return a corresponding match object.

Note that even in MULTILINE mode, re.match() will only match at the beginning of the string and not at the beginning of each line.

If you want to locate a match anywhere in string, use search() instead

## search() vs. match()[^2]

- `re.match()` checks for a match only at the beginning of the string

- `re.search()` checks for a match anywhere in the string (this is what Perl does by default)

- `re.fullmatch()` checks for entire string to be a match

[^1]:https://docs.python.org/3/library/re.html

[^2]:https://docs.python.org/3/library/re.html#search-vs-match

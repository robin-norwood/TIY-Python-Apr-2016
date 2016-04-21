### String formatting!


In [1]: name = "Robin"

In [2]: print("Hello, " + name)
Hello, Robin

In [3]: greeting = "Hello, "

In [4]: print(greeting + name + "!")
Hello, Robin!

In [5]: greet = "Hello, {0}. How are you {1}?"

In [6]: greet
Out[6]: 'Hello, {0}. How are you {1}?'

In [7]: print(greet)
Hello, {0}. How are you {1}?

In [8]: print(greet.format("Robin", "today"))
Hello, Robin. How are you today?

In [9]: greet = "Hello, {1}. How are you {0}?"

In [10]: print(greet.format("Robin", "today"))
Hello, today. How are you Robin?

In [11]: greeting = "Hello, {name}, how are you {day}?"

In [12]: greeting.format(name="Robin", day="Today")
Out[12]: 'Hello, Robin, how are you Today?'

In [13]: def format_string(thestring, *args, **kwargs):
KeyboardInterrupt

In [13]: print("hello, %s", "robin")
hello, %s robin

In [14]: print("hello, %s" % "robin")
hello, robin

In [15]: print("hello, {0}" % "robin")
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-15-e4c3f3745325> in <module>()
----> 1 print("hello, {0}" % "robin")

TypeError: not all arguments converted during string formatting

In [16]: import math

In [17]: math.pi
Out[17]: 3.141592653589793

In [18]: print("Today, pi is approximately {pi}".format(pi=math.pi))
Today, pi is approximately 3.141592653589793

In [19]: print("Today, pi is approximately {pi:.2f}".format(pi=math.pi))
Today, pi is approximately 3.14

In [20]:

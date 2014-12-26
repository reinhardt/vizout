vizout
======

Constructs a graphviz representation of a hierarchy of [buildout](http://www.buildout.org) configuration files referenced by "extends"

Usage
-----

<code>$ python vizout.py [filename]</code>

Looks for the "extends" option in _filename_ and recursively in referenced files, constructing a graphviz diagram of the references. Filename defaults to "buildout.cfg".

You can use the output with graphviz as you see fit. A simple example that makes a png image:

<code>$ python vizout.py | dot -Tpng > buildout.png</code>

ToDo
----

* follow web links

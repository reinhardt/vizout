vizout
======

Constructs a graphviz representation of buildout files referenced by "extends"

Usage
-----

  python vizout.py [filename]

Looks for the "extends" option in _filename_ and recursively in referenced files, constructing a graphviz diagram of the references. Filename defaults to "buildout.cfg".

You can use the output with graphviz as you see fit. A simple example that makes a png image:

  python vizout.py > buildout.gv && dot -Tpng buildout.gv > buildout.png

ToDo
----

* follow web links

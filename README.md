Dydra.com Software Development Kit (SDK) for Python
===================================================

This is the official Python software development kit (SDK) for
[Dydra.com][], the cloud-hosted RDF & SPARQL database service.

<https://github.com/dydra/dydra-py>

Dependencies
------------

* [Python](http://python.org/) (>= 2.6)
* [RDFLib](http://pypi.python.org/pypi/rdflib) (>= 3.0.0)

Note: the instructions in this README, and the operation of the library
itself, implicitly assume a Unix system (Mac OS X, Linux, or *BSD) at
present. Patches improving Windows support are most welcome.

Installation
------------

The recommended installation method is via [PIP][].
To install the latest official release of the SDK, do:

    $ [sudo] pip install dydra

Should you wish to remove the SDK from your system, do:

    $ [sudo] pip uninstall dydra

Download
--------

To get a local working copy of the development repository, do:

    $ git clone git://github.com/dydra/dydra-py.git

Mailing List
------------

* <http://groups.google.com/group/dydra>

Authors
-------

* [Arto Bendiken](https://github.com/bendiken) - <http://dydra.com/bendiken>

Contributing
------------

* Do your best to adhere to the existing coding conventions and idioms.
* Don't use hard tabs, and don't leave trailing whitespace on any line.
* Don't touch the `setup.py`, `VERSION`, or `AUTHORS` files. If you need to
  change them, do so on your private branch only.
* Do feel free to add yourself to the `CREDITS` file and the corresponding
  list in the `README`. Alphabetical order applies.

License
-------

This is free and unencumbered public domain software. For more information,
see <http://unlicense.org/> or the accompanying `UNLICENSE` file.

[Python]:     http://python.org/
[PIP]:        http://www.pip-installer.org/
[RDF]:        http://www.w3.org/RDF/
[RDFLib]:     http://www.rdflib.net/
[PDD]:        http://unlicense.org/#unlicensing-contributions
[Dydra.com]:  http://dydra.com/

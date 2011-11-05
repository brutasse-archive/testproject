Test Project
============

This aims at providing a sample project for testing CI tools.

This should provide:

* Successful builds
* Failing builds
* Builds failing for a specific configuration

Running the tests
-----------------

::

    virtualenv test --python pythonX.Y --no-site-packages
    source test/bin/activate
    pip install nose coverage
    nosetests [<nose opts>] project.py

XUnit test output
`````````````````

::

    nosetests --with-xunit project.py

The report is written to ``nosetests.xml``.

Cobertura coverage reports
``````````````````````````

::

    nosetests --with-coverage --cover-package=project project.py
    coverage xml

The coverage file is available as ``coverage.xml``

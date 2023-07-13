# Getting Started 

This project is using Mozio API in testing environment for performe core operations. 

run the next script to install the requiered packages

```pip3 install -r requirements.txt```

# Project structure

BaseClient - encapsulates the core HTTP methods
MozioClient - Inherents from BaseClient to perform HTTP operations to Mozio API
TestMozioClient - perform unittest and integration tests to MozioClient 

# Run tests

In order to run tests use ```python -m unittest unittests.py```



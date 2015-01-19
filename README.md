# Tabular Validator Web

[![Build Status](https://api.shippable.com/projects/54b903605ab6cc135288d4de/badge?branchName=master)](https://app.shippable.com/projects/54b903605ab6cc135288d4de/builds/latest)

A web API for validating data tables against a validation pipeline.

This package is part of a suite of table validation tools, providing a lightweight web interface to [Tabular Validator](https://github.com/okfn/tabular-validator).

See the [documentation](http://tabular-validator.readthedocs.org/en/latest/web.html) for more information.


Built around Flask, Celery, and SQL Alchemy.

# Start

```
# run a local server
python main.py

# run the tests
python -m unittest tests
```
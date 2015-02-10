# Tabular Validator Web

[![Travis Build Status](https://travis-ci.org/okfn/tabular-validator-web.svg?branch=master)](https://travis-ci.org/okfn/tabular-validator-web)
[![Coverage Status](https://coveralls.io/repos/okfn/tabular-validator-web/badge.svg)](https://coveralls.io/r/okfn/tabular-validator-web)

A web API for validating data tables against a validation pipeline.

This package is part of a suite of table validation tools, providing a lightweight web interface to [Tabular Validator](https://github.com/okfn/tabular-validator).

## Runtime support

Planned support for Python 2.7, 3.3 and 3.4. Some tests currently fail on 2.7. Development is proceeding on 3.4.

## Quickstart

* Clone the repository into a virtual environment
* Install dependencies: `pip install -r requirements/local.txt`
* Run a server: `python main.py`
* Run the tests: `./test.sh`

## What we've got

### `/` (Home)

* A home page with some orientation to what is going on
* A form to submit data for validation manually *WIP*

### `/api` (API Index)

* A JSON object with an `endpoints` property that describes the available endpoints

### `api/run` (Task Runner)

* POST to validate data
* GET to validate data *WIP*

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

## Supported configuration parameters

The API and UI support a subset of all parameters available in a [Tabular Validator](https://github.com/okfn/tabular-validator) pipeline. All possible arguments to a pipeline and individual validators can be found in the [Tabular Validator docs](http://tabular-validator.readthedocs.org/en/latest/).

### UI

The UI is a simple form for validation data, with an option schema, from either an URL or an uploaded file.

* One of `data_url` or `data_file`: This gets turned into the `data` argument to the pipeline.
* One of `schema_url` or `schema_file`: This is a convenience for the `options['schema']['schema']` argument that is passed to the schema validator.
* Additional defaults are passed into the pipeline constructor. You can see the defaults at [`tvweb.config.defaults.TVWEB_PIPELINE_DEFAULT_CONFIG`](https://github.com/okfn/tabular-validator-web/blob/master/tvweb/config/default.py)

### API

* `data`: (required) Any file, URL to a file, or string of data
* `schema`: (default. None) This is a convenience for the `options['schema']['schema']` argument that is passed to the schema validator
* `report_limit`: (default. 1000, max. 1000) An integer that sets a limit on the amount of report results a validator can generate. Validation will cease of this amount is reached
* `row_limit`: (default. 20000, max. 30000) An integer that sets a limit on the amount of rows that will be processed. Iteration over the data will stop at this amount.

## Examples

### Data

You can find example data [here](https://github.com/okfn/tabular-validator-web/tree/master/examples) and [here](https://github.com/okfn/tabular-validator/tree/master/examples).

You can also use the CLI to run some basic checks. The CLI entry point is `tv` if you've installed from PyPI, otherwise `python main/cli.py`:

```
python main/cli.py examples http://tabulator.okfnlabs.org one

python main/cli.py examples http://tabulator.okfnlabs.org two

python main/cli.py examples http://tabulator.okfnlabs.org three
```

Similar requests can be made with cURL. For example:

```
curl --data "data=https%3a%2f%2fraw.githubusercontent.com%2fokfn%2ftabular-validator%2fmasteres%2fcontacts%2fpeople.csv&schema=https%3a%2f%2fraw.githubusercontent.com%2fokfn%2ftabular-validator%2fmaster%2fexamples%2fcontacts%2fschema_valid.json" http://127.0.0.1:5000/api/run
```

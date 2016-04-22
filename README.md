# Good Tables Web

[![Travis Build Status](https://travis-ci.org/frictionlessdata/goodtables.io.svg?branch=master)](https://travis-ci.org/frictionlessdata/goodtables.io)
[![Coverage Status](https://coveralls.io/repos/frictionlessdata/goodtables.io/badge.svg)](https://coveralls.io/r/frictionlessdata/goodtables.io)

A web API for validating data tables against a validation pipeline.

This package is part of a suite of table validation tools, providing a lightweight web interface to [Good Tables](https://github.com/okfn/goodtables).

## Runtime support

Planned support for Python 2.7, 3.3 and 3.4. Some tests currently fail on 2.7. Development is proceeding on 3.4.

## Quickstart

* Clone the repository into a virtual environment
* Install dependencies: `pip install -r requirements.txt`
* Run a server: `python main.py`
* Run the tests: 
  * `pip install -r requirements/test.txt && pip install -r requirements/local.txt`
  * `./test.sh`

## What we've got

### `/` (Home)

* A web form for manually adding data for validation

### `/api` (API Index)

* Via XHR, a JSON object with an `endpoints` property that describes the available endpoints
* Via browser, a documentation page for the API

### `api/run` (Task Runner)

* POST to validate data
* GET to validate data

## Supported configuration parameters

The API and UI support a subset of all parameters available in a [Good Tables](https://github.com/okfn/goodtables) pipeline.

All possible arguments to a pipeline and individual processors can be found in the [Good Tables docs](http://goodtables.readthedocs.org/en/latest/).

### API

* `data`: (required) Any file, URL to a file, or string of data
* `schema`: (default. None) This is a convenience for the `options['schema']['schema']` argument that is passed to the schema validator
* `report_limit`: (default. 1000, max. 1000) An integer that sets a limit on the amount of report results a validator can generate. Validation will cease of this amount is reached
* `row_limit`: (default. 20000, max. 30000) An integer that sets a limit on the amount of rows that will be processed. Iteration over the data will stop at this amount.
* `fail_fast`: (default True) A boolean to set whether the run will fail on first error, or not.
* `format`: (default 'csv') 'csv' or 'excel' - the format of the file.
* `ignore_empty_rows`: (default False) A boolean to set whether empty rows should raise errors, or be ignored.
* `ignore_duplicate_rows`: (default False) A boolean to set whether duplicate rows should raise errors, or be ignored.
* `encoding`: (default None) A string that indicates the encoding of the data. Overrides automatic encoding detection.

#### Example

```
# make a request
curl http://goodtables.okfnlabs.org/api/run --data "data=https://raw.githubusercontent.com/okfn/goodtables/master/examples/row_limit_structure.csv&schema=https://raw.githubusercontent.com/okfn/goodtables/master/examples/test_schema.json"

# the response will be like
{
    "report": {
        "summary": {
            "bad_row_count": 1,
            "total_row_count": 10,
            ...
        },
        "results": [
            {
            "result_id": "structure_001", # the ID of this result type
            "result_level": "error", # the severity of this result type (info/warning/error)
            "result_message": "Row 1 is defective: there are more cells than headers", # a message that describes the result
            "result_name": "Defective Row", # a human-readable title for this result
            "result_context": ['38', 'John', '', ''], # the row values from which this result triggered
            "row_index": 1, # the idnex of the row
            "row_name": "", # If the row has an id field, this is displayed, otherwise empty
            "column_index": 4, # the index of the column
            "column_name": "" # the name of the column (the header), if applicable
            },
            ...
        ]
    }
}
```

### UI

The UI is a simple form to add data, with an option schema, from either URLs or uploaded files.

#### Example

<img src="https://dl.dropboxusercontent.com/u/13029373/okfn/ui.gif" />

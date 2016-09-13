This field is a [unique field](http://specs.frictionlessdata.io/json-table-schema/#field-constraints) but it contains a value that has been used in another row.

Things you can try:
- If you know the correct value, update the data.
- If the data is correct, then the values in this column are not unique. Remove the `"unique": true` constraint from your schema, or change it to `"unique": false`.

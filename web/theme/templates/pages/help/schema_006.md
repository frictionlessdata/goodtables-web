This field is a [unique field](http://specs.frictionlessdata.io/json-table-schema/#field-constraints), but it contains a value that has been used in another row.

- If you know the correct field value, update the data.
- If the data in this column is not unique, remove the `"unique": true` constraint from your schema, or change it to `"unique": false`.

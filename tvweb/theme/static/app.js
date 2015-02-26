var $form = $('#run_form'),
    $withSchema = $('#with_schema'),
    $schemaFields = $('.form-wrap-schema-fields'),
    $schemaUrlGroup = $('.form-group-schema_url'),
    $schemaFileGroup = $('.form-group-schema_file'),
    $dataUrlGroup = $('.form-group-data_url'),
    $dataFileGroup = $('.form-group-data_file'),
    $dataFieldToggle = $('.data-field-toggle'),
    $schemaFieldToggle = $('.schema-field-toggle');


function formUX() {

    // toggle display of schema forms
    $withSchema.on('click', function(){
        if ($withSchema.is(':checked')) {
            $schemaFields.show();
        } else {
            $schemaFields.hide();
        }
    });

    // toggle data fields
    $dataFieldToggle.change(function() {
        if ($dataFieldToggle.is(':checked')) {
            $dataUrlGroup.show();
            $dataFileGroup.hide();
        } else {
            $dataUrlGroup.hide();
            $dataFileGroup.show();
        }
    });

    // toggle schema fields
    $schemaFieldToggle.change(function() {
        if ($schemaFieldToggle.is(':checked')) {
            $schemaUrlGroup.show();
            $schemaFileGroup.hide();
        } else {
            $schemaUrlGroup.hide();
            $schemaFileGroup.show();
        }
    });


}

formUX();

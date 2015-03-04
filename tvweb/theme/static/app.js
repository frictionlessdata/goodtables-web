var $form = $('#run_form'),
    $withSchema = $('#with_schema'),
    $schemaFields = $('.form-wrap-schema-fields'),
    $schemaUrlGroup = $('.form-group-schema_url'),
    $schemaUrlInput = $schemaUrlGroup.children('input'),
    $schemaFileGroup = $('.form-group-schema_file'),
    $schemaFileInput = $schemaFileGroup.children('input'),
    $dataUrlGroup = $('.form-group-data_url'),
    $dataUrlInput = $dataUrlGroup.children('input'),
    $dataFileGroup = $('.form-group-data_file'),
    $dataFileInput = $dataFileGroup.children('input'),
    $dataFieldRadio = $('.data-field-url, .data-field-file'),
    $dataFieldUrl = $('.data-field-url'),
    $dataFieldFile = $('.data-field-file'),
    $schemaFieldRadio = $('.schema-field-url, .schema-field-file'),
    $schemaFieldUrl = $('.schema-field-url'),
    $schemaFieldFile = $('.schema-field-file'),
    $schemaEg = $('#schema_eg');


function formUX() {

    // toggle display of schema forms
    $withSchema.on('click', function(){
        if ($withSchema.is(':checked')) {
            $schemaFields.show();
        } else {
            $schemaFileInput.val('');
            $schemaUrlInput.val('');
            $schemaFields.hide();
        }
    });

    // toggle data fields
    $dataFieldRadio.on('change', function() {
        if ($dataFieldUrl.is(':checked')) {
            $dataUrlGroup.show();
            $dataFileInput.val('');
            $dataFileGroup.hide();
        }

        if ($dataFieldFile.is(':checked')) {
            $dataUrlInput.val('');
            $dataUrlGroup.hide();
            $dataFileGroup.show();
        }
    });

    // toggle schema fields
    $schemaFieldRadio.on('change', function() {
        if ($schemaFieldUrl.is(':checked')) {
            $schemaUrlGroup.show();
            $schemaFileInput.val('');
            $schemaFileGroup.hide();
        }

        if ($schemaFieldFile.is(':checked')) {
            $schemaUrlInput.val('');
            console.log('here');
            $schemaEg.selectpicker('val', '');
            $schemaUrlGroup.hide();
            $schemaFileGroup.show();
        }
    });

    // manage schema presets
    $schemaEg.on('change', function() {
        var $this = $(this);
        $schemaUrlGroup.show();
        $schemaFieldUrl.prop('checked', true);
        $schemaFileGroup.hide();
        $schemaFileInput.val('');
        $schemaUrlInput.val($this.val());
    });

}

function tableUX() {
    // stick the result table header
    $("#results-sample thead").stick_in_parent({"offset_top": 50});
}

function urlState() {
    // put the GETable query onto the URL for copy-pasters ;)
    if (reportUrlState) {
        console.log('YEP');
        if (history.pushState) {
            history.pushState({}, 'reports', 'reports' + reportUrlState);
        }
    }

}

formUX();
tableUX();
urlState();

var $form = $('#run_form'),
    $withSchema = $('#with_schema'),
    $schemaFields = $('.display-schema-fields'),
    $hideSchemaFields = $('.hide-schema-fields'),
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
    $schemaEg = $('#schema_eg'),
    $runForm = $('#run_form'),
    getableReportParams = '#data_url, #schema_url, #encoding, #format, #fail_fast, #ignore_empty_rows, #ignore_duplicate_rows';


function formUX() {

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
            $schemaEg.val('');
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

function dynamicFormAction() {

    $runForm.submit(function(){
        var baseAction = $runForm.attr('action'),
            params = '?' + $(this).find(getableReportParams).serialize(),
            dynamicAction = baseAction + params;
        $runForm.attr('action', dynamicAction);
    });

}

(function($) {
  // disable ribbon clickthrough
  if ( $(document).width() > 767) {
    $('.navbar .open-knowledge').click(function(e) {e.preventDefault();
  }); }

  // default class
  $('.navbar .open-knowledge').addClass('collapsed');

})(jQuery);


/*!
 * equalize.js
 * Author & copyright (c) 2012: Tim Svensen
 * Dual MIT & GPL license
 *
 * Page: http://tsvensen.github.com/equalize.js
 * Repo: https://github.com/tsvensen/equalize.js/
 */
!function(i){i.fn.equalize=function(e){var n,t,h=!1,c=!1;return i.isPlainObject(e)?(n=e.equalize||"height",h=e.children||!1,c=e.reset||!1):n=e||"height",i.isFunction(i.fn[n])?(t=0<n.indexOf("eight")?"height":"width",this.each(function(){var e=h?i(this).find(h):i(this).children(),s=0;e.each(function(){var e=i(this);c&&e.css(t,""),e=e[n](),e>s&&(s=e)}),e.css(t,s+"px")})):!1}}(jQuery);


$('.pricing-panels').equalize({children: '.pricing-panel > div > div', equalize: 'outerHeight'});

$('.set-example-url').on('click',function(event){
  event.preventDefault();
  $('#data_url').fadeOut(100).val($(this).data('example-url')).fadeIn(100); 
  if ($(this).data('set-schema')) {
    $("#data-field-1").prop("checked", true).change();
    $("#schema_eg").val($(this).data('set-schema')).change();
    $("#schema_url").fadeOut(100).fadeIn(100);
  } else {
    $("#data-field-1").prop("checked", true).change();
    $("#schema_eg").val("").change();
    $("#schema_url").fadeOut(100).fadeIn(100);
  }
});

formUX();
dynamicFormAction();

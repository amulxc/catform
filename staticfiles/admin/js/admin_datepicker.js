(function($) {
    $(document).ready(function() {
        if ($.fn.datepicker) {  // Check if datepicker is available
            $('.datepicker').datepicker({
                dateFormat: 'yy-mm-dd',
                changeMonth: true,
                changeYear: true,
                yearRange: "-100:+0"
            });
        } else {
            console.error("jQuery UI Datepicker is not loaded.");
        }
    });
})(django.jQuery);

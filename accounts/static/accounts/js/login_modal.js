$(function () {
    var dialog, form;

        dialog = $("#dialog-form").dialog({
            autoOpen: false,
            height: 225,
            width: 350,
            modal: true,
            close: function () {
                form[0].reset();
                allFields.removeClass("ui-state-error");
            }
        });

    form = dialog.find("form").on("submit", function (event) {
        event.preventDefault();
    });

    $("#login").button().on("click", function () {
        dialog.dialog("open");
    });
});
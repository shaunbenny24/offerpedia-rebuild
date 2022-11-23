function ShowSnackBar() {
    var x = document.getElementById("snackbar");
    x.className = "show";
    setTimeout(function () {
        x.className = x.className.replace("show", "");
    }, 3000);
}

function show_loader() {
    $('.popup-bg').show();
    $('.popup-box').remove();
    $('body').append('<div class="popup-box"><div class="preloader pl-xxl"><svg viewBox="25 25 50 50" class="pl-circular"><circle r="20" cy="50" cx="50" class="plc-path"/></svg></div></div><span class="popup-bg"></span>');
}

function remove_popup() {
    $('.popup-box,.popup-bg').remove();
}

function modalHight() {
    let modal_hei = $("section#model").outerHeight(true);
    modal_hei = 0 - modal_hei - 10;
    $("section#model").css("top", modal_hei);
    $("#overlay_page").css("display", "none");
}

// ajax : form submitions and action buttons
$(document).on("submit", "form.ajax", function (e) {
    e.preventDefault();
    var $this = $(this);

    $this.validate({
        rules: {
            required_field: "required",
            password1: "required",
            password2: {
                equalTo: "#id_password1"
            }
        }
    });
    var valid = $this.valid();
    if (valid) {
        var url = $this.attr("action");
        var method = $this.attr("method");
        var isReload = $this.hasClass("reload");
        var isRedirect = $this.hasClass("redirect");
        var data = $this.serialize();

        show_loader();

        jQuery.ajax({
            type: method,
            url: url,
            dataType: "json",
            data: new FormData(this),
            cache: false,
            contentType: false,
            processData: false,
            success: function (data) {
                remove_popup();

                var message = data["message"];
                var status = data["status"];
                var title = data["title"];
                var redirect = data["redirect"];
                var redirect_url = data["redirect_url"];
                var stable = data["stable"];
                var pk = data["pk"];

                if (status == "true") {
                    if (title) {
                        title = title;
                    } else {
                        title = "Success";
                    }

                    function doAfter() {
                        if (isRedirect && redirect == "true") {
                            window.location.href = redirect_url;
                        }
                        if (isReload) {
                            window.location.reload();
                        }
                    }

                    swal(
                        {
                            title: title,
                            text: message,
                            type: "success"
                        },
                        function () {
                            doAfter();
                        }
                    );
                } else {
                    if (title) {
                        title = title;
                    } else {
                        title = "An Error Occurred";
                    }

                    swal(title, message, "error");

                    if (stable != "true") {
                        window.setTimeout(function () { }, 2000);
                    }
                }
            },
            error: function (data) {
                remove_popup();

                var title = "An error Occurred";
                var message = "An error Occurred. Please try again later.";
                swal(title, message, "error");
            }
        });
    }
});

$(document).on('click', '.action-button', function (e) {
    e.preventDefault();
    $this = $(this);
    var text = $this.attr('data-text');
    var type = "warning";
    var confirmButtonText = "Yes";
    var confirmButtonColor = "#DD6B55";
    var id = $this.attr('data-id');
    var url = $this.attr('href');
    var title = $this.attr('data-title');
    if (!title) {
        title = "Are you sure?";
    }
    var isReload = $this.hasClass('reload');
    var isRedirect = $this.hasClass('redirect');
    var showAlert = $this.hasClass('with_alert');
    var isRemove = $this.hasClass('remove');
    var noResponsePopup = $this.hasClass('no-response-popup');
    var downloadFile = $this.hasClass('download-file');

    swal({
        title: title,
        text: text,
        type: type,
        showCancelButton: true,
        confirmButtonColor: confirmButtonColor,
        confirmButtonText: confirmButtonText,
        closeOnConfirm: true,
        closeOnCancel: true
    }, function (isConfirm) {
        if (isConfirm) {
            show_loader();

            window.setTimeout(function () {
                jQuery.ajax({
                    type: 'GET',
                    url: url,
                    dataType: 'json',
                    data: {
                        pk: id
                    },
                    success: function (data) {
                        var message = data['message'];
                        var status = data['status'];
                        var redirect = data['redirect'];
                        var redirect_url = data['redirect_url'];
                        var stable = data['stable'];
                        var title = data['title'];
                        var file_url = data['file_url']

                        remove_popup();

                        if (status == 'true') {
                            if (title) {
                                title = title;
                            } else {
                                title = "Success";
                            }
                            if (!noResponsePopup) {
                                swal({
                                    title: title,
                                    text: message,
                                    type: "success"
                                }, function () {
                                    if (isRemove) {
                                        var row_length = $this.parents('tbody').find('tr').length;
                                        $this.parents('tr').remove();
                                        var end = parseInt($('.current_end_status').html());
                                        var total = parseInt($('.total_count').html());
                                        $('.total_count').html(total - 1);
                                        $('.current_end_status').html(end - 1);
                                        if (row_length <= 1) {
                                            window.location.reload();
                                        }
                                    }

                                    if (stable != "true") {
                                        if (isRedirect && redirect == 'true') {
                                            window.location.href = redirect_url;
                                        }
                                        if (isReload) {
                                            window.location.reload();
                                        }
                                    }
                                });
                            }

                            if (downloadFile) {
                                window.location.href = file_url;
                            }

                        } else {
                            if (title) {
                                title = title;
                            } else {
                                title = "An Error Occurred";
                            }

                            swal(title, message, "error");

                            if (stable != "true") {
                                window.setTimeout(function () {
                                }, 2000);
                            }
                        }
                    },
                    error: function (data) {
                        remove_popup();

                        var title = "An error occurred";
                        var message = "An error occurred. Please try again later.";
                        swal(title, message, "error");
                    }
                });
            }, 100);

        }
    });
});

$(document).on('click', '.success-button', function (e) {
    e.preventDefault();
    $this = $(this);
    var type = "success";
    var id = $this.attr('data-id');
    var url = $this.attr('href');
    var isReload = $this.hasClass('reload');
    var isRedirect = $this.hasClass('redirect');
    var button_checked = "false";
    if ($('div.cashback span.cashbackApply .cashback-button').is(':checked')) {
        button_checked = "true";
    }
    show_loader();

    jQuery.ajax({
        type: 'GET',
        url: url,
        dataType: 'json',
        data: {
            pk: id,
            button_checked: button_checked
        },
        success: function (data) {
            var message = data['message'];
            var status = data['status'];
            var redirect = data['redirect'];
            var redirect_url = data['redirect_url'];
            var stable = data['stable'];
            var title = data['title'];

            if (status == "false"){
                type = "error";
            }
            swal({
                title: title,
                text: message,
                type: type,
           
            }, function () {
                if (stable != "true") {
                    if (isRedirect && redirect == 'true') {
                        window.location.href = redirect_url;
                    }
                    if (isReload) {
                        window.location.reload();
                    }
                }
            });

            remove_popup();
        },
        error: function (data) {
            remove_popup();

            var title = "An error occurred";
            var message = "An error occurred. Please try again later.";
            swal(title, message, "error");
        }
    });
});
(function() {
    'use strict';
    var 
        form_data,
        confirm_rsvp_callback = function (data, XHR) {
            var email = "james.m.stevenson";
            $("#attend a").attr('href', 'mailto:' + email + "@gmail.com");
            $("form").fadeOut(400, function () {
                $("#" + ((form_data.attending) ? "attend" : "skip")).fadeIn();
            });
            $("h1").html("Thanks!");
        },
        show_field_error = function(field, message) {
            var err = $('<ul class="errorlist"><li>' + message + '</li></ul>');
            field.after(err);
        }
    // Setup page.
    $(".confirm").hide();
    $("#page").css("height", "540px");
    $("button").click(function (evt) {
        evt.preventDefault();
        $(".errorlist").remove();
        // Assemble data, validate and post.
        form_data = {
            name: $("#id_name").val(),
            attending: !!$("#id_attending").attr("checked"),
            guests: $("#id_guests").val(),
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
        }
        if (!form_data.name) {
            show_field_error($("#id_name"), "Please enter your name.");
            return;
        }
        if (form_data.attending && !form_data.guests) {
            show_field_error($("#id_guests"), "Please enter 1 or more guests.");
            return;
        }
        $.ajax({
            type: 'POST',
            url: window.location.href,
            data: form_data,
            success: confirm_rsvp_callback
        });
        
    });
    
})();
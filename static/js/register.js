/* eslint-disable no-undef */
$(document).ready(() => {
  var form = $('#register');

  form.submit((event) => {
    event.preventDefault();

    $.ajax({
      type: 'POST',
      url: `http://donde-estas.herokuapp.com/person?${form.serialize()}`,
      // data: jQuery.param(form),
      success: function (data) {
        console.log("Success");
        console.log(JSON.parse(JSON.stringify(data)));
      },
      error: function(data) {
        console.log(JSON.parse(JSON.stringify(data)));
      }
    });
    return false;
  });

});

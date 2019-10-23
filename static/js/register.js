/* eslint-disable no-undef */
$(document).ready(() => {

  var frm = $('#register');

  var form = {}

  jQuery.each(frm.serializeArray(), function() {
    form[this.name] = this.value;
  });

  console.log(form);

  frm.submit((event) => {
    event.preventDefault();
    $.ajax({
      type: 'POST',
      url: 'http://donde-estas.herokuapp.com/missing',
      data: form,
      success: function (data) {
        console.log("Success");
        console.log(JSON.parse(data.responseText));
      },
      error: function(data) {
        console.log("Mi vieja mula ya no es lo que era");
        console.log(JSON.parse(data.responseText));
      }
    });
    return false;
  });

});

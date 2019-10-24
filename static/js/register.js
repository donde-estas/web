/* eslint-disable no-undef */
$(document).ready(() => {
  // const container = $('div#register');
  const form = $('#register');

  form.submit((event) => {
    event.preventDefault();

    function onSuccess(data) {
      console.log('success');
      console.log(data);
    }

    function onError(data) {
      console.log('error');
      console.log(data);
    }

    $.ajax({
      type: 'POST',
      headers: {
        'Access-Control-Allow-Origin': '*',
      },
      url: 'http://donde-estas.herokuapp.com/missing',
      dataType: 'jsonp',
      data: form.serialize(),
      success: onSuccess,
      error: onError,
    });
  });
});

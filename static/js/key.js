$(document).ready(() => {
  const keyError = $('#key-error');
  const keySuccess = $('#key-success');
  const keyForm = $('#key-form');
  const keyButton = $('#key-button');
  const timeInterval = $('#time-left');
  const auto = $('#auto');

  keyForm.submit((event) => {
    event.preventDefault();
    keyButton.addClass('is-loading');

    const datum = keyForm.serializeArray();
    if (auto.length) {
      datum[1].value = auto.text();
    }

    $.ajax({
      type: 'POST',
      url: keyForm.attr('action'),
      data: datum,
      success: (data) => {
        if (data.success) {
          keyError.hide();
          keySuccess.show();
          keyForm.hide();
          window.setInterval(() => {
            const timeLeft = parseInt(timeInterval.html(), 10);
            if (!timeLeft) {
              window.location = (data.url);
            } else {
              timeInterval.html(timeLeft - 1);
            }
          }, 1000);
        } else if (auto.length) {
          window.location = (data.url);
          // eslint-disable-next-line no-alert
          alert('Algo ha salido mal, por favor ingrese el código manualmente ó intente nuevamente');
        } else {
          keyError.show();
          keySuccess.hide();
          keyForm.show();
        }
        keyButton.removeClass('is-loading');
      },
      error: () => {
        keyError.show();
        keySuccess.hide();
        keyForm.show();
      },
    });
  });

  if (auto.length) {
    keyForm.submit();
  }
});

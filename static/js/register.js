$(document).ready(() => {
  const registrationError = $('#registration-error');
  const registrationSuccess = $('#registration-success');
  const registrationForm = $('#registration-form');
  const registrationButton = $('#registration-button');

  registrationForm.submit((event) => {
    event.preventDefault();
    registrationButton.addClass('is-loading');

    $.ajax({
      type: 'POST',
      url: registrationForm.attr('action'),
      data: registrationForm.serialize(),
      success: (data) => {
        if (data.success) {
          registrationError.hide();
          registrationSuccess.show();
          registrationForm.hide();
        } else {
          registrationError.show();
          registrationSuccess.hide();
          registrationForm.show();
        }
      },
      error: () => {
        registrationError.show();
        registrationSuccess.hide();
        registrationForm.show();
      },
    });

    registrationButton.removeClass('is-loading');
  });

  (document.querySelectorAll('.notification .delete') || []).forEach(($delete) => {
    const notification = $delete.parentNode;
    $delete.addEventListener('click', () => {
      notification.parentNode.removeChild(notification);
    });
  });
});

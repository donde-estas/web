const moment = require('moment');

moment.locale('Es');

$(document).ready(() => {
  $('[class=time-placeholder]').each((i, old) => {
    $(old).text((_, text) => moment(new Date(text)).format('hh:mm [del día] D [de] MMMM YYYY'));
  });
});

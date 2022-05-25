$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (key) {
  $('DIV#hello').text(key.hello);
});

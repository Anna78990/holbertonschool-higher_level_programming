$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (index, sw) {
    $('UL#list_movies').append('<li>' + sw.title + '</li>');
  });
});

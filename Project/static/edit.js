$(document).ready(function () {

  const oneDay = 24 * 60 * 60 * 1000; // hours*minutes*seconds*milliseconds
  var sd = {{itn.start_date|tojson}};
  var ed = {{itn.end_date|tojson}};
  var startDate = new Date(sd);
  const endDate = new Date(ed);
  const numDays = Math.round(Math.abs((startDate - endDate) / oneDay));

  startDate.setDate(startDate.getDate());
  var year = new Intl.DateTimeFormat('en', { year: 'numeric' }).format(startDate);
  var mth = new Intl.DateTimeFormat('en', { month: 'short' }).format(startDate);
  var date = new Intl.DateTimeFormat('en', { day: '2-digit' }).format(startDate);
  var day = new Intl.DateTimeFormat('en', { weekday: 'short' }).format(startDate);

  var listName = (`${day} ${date} ${mth} ${year}`)

   var $clone = $($('#orders').html());
   $('.start_date', $clone).text("hello");
       $("#orders").append(
      '<div class="column">' +
        '<div class="itnbox" data-title="' +
        listName +
        '">' +
        '<div class="header">' +
        "    " +
        listName +
        "</div>" +
        '<div class="body">' +
        '    <ul id="sortable3" class="droptrue">' +
        "    </ul>" +
        "</div></div></div>"

    );

  for (var i = 0; i < numDays ; i++) {

      startDate.setDate(startDate.getDate() + 1);
      var year = new Intl.DateTimeFormat('en', { year: 'numeric' }).format(startDate);
      var mth = new Intl.DateTimeFormat('en', { month: 'short' }).format(startDate);
      var date = new Intl.DateTimeFormat('en', { day: '2-digit' }).format(startDate);
      var day = new Intl.DateTimeFormat('en', { weekday: 'short' }).format(startDate);

      var listName = (`${day} ${date} ${mth} ${year}`)

       var $clone = $($('#orders').html());
       $('.start_date', $clone).text("hello");
           $("#orders").append(
          '<div class="column">' +
            '<div class="itnbox" data-title="' +
            listName +
            '">' +
            '<div class="header">' +
            "    " +
            listName +
            "</div>" +
            '<div class="body">' +
            '    <ul id="sortable3" class="droptrue">' +
            "    </ul>" +
            "</div></div></div>"

        );
  }

  var options = "<option>Sort</option>";
  var startDate = new Date(sd);

  startDate.setDate(startDate.getDate());
  var year = new Intl.DateTimeFormat('en', { year: 'numeric' }).format(startDate);
  var mth = new Intl.DateTimeFormat('en', { month: 'short' }).format(startDate);
  var date = new Intl.DateTimeFormat('en', { day: '2-digit' }).format(startDate);
  var day = new Intl.DateTimeFormat('en', { weekday: 'short' }).format(startDate);

  var listName = (`${day} ${date} ${mth} ${year}`)
  options += "<option>"+ listName +"</option>";

  for (var list = 0; list < numDays ; list++) {

  startDate.setDate(startDate.getDate() + 1);
  const year = new Intl.DateTimeFormat('en', { year: 'numeric' }).format(startDate);
  const mth = new Intl.DateTimeFormat('en', { month: 'short' }).format(startDate);
  const date = new Intl.DateTimeFormat('en', { day: '2-digit' }).format(startDate);
  const day = new Intl.DateTimeFormat('en', { weekday: 'short' }).format(startDate);

  var listName = (`${day} ${date} ${mth} ${year}`)
  options += "<option>"+ listName +"</option>";
  }
  document.getElementById("list").innerHTML = options;

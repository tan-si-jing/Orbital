$(document).ready(function () {

	const oneDay = 24 * 60 * 60 * 1000; // hours*minutes*seconds*milliseconds
	var sd = {{itn.start_date|tojson}};
	console.log(sd)
	var startDate = new Date(sd);
	console.log(startDate)
	const endDate = new Date(2020, 7, 4);
	const numDays = Math.round(Math.abs((startDate - endDate) / oneDay));

	var listName = startDate;
	var alpha= $('div.column').clone();

	for (var i = 0; i < numDays ; i++) {

			startDate.setDate(startDate.getDate() + 1);
	    const year = new Intl.DateTimeFormat('en', { year: 'numeric' }).format(startDate);
			const mth = new Intl.DateTimeFormat('en', { month: 'short' }).format(startDate);
			const date = new Intl.DateTimeFormat('en', { day: '2-digit' }).format(startDate);
			const day = new Intl.DateTimeFormat('en', { weekday: 'short' }).format(startDate);

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
});

function Delete(currentEl){
  currentEl.parentNode.parentNode.removeChild(currentEl.parentNode);
    $.ajax({
        type: "DELETE",
        url: '/delete_activity' + currentEl,
        success: function () {
            $('li').remove(currentEl);
        }
    }).then(res => console.log(res));
  }

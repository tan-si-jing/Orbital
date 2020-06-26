// This part here is the 100% correct code to update the date that
// the loop can access and then update the correct title

const oneDay = 24 * 60 * 60 * 1000; // hours*minutes*seconds*milliseconds
const startDate = new Date(2008, 1, 12);
const endDate = new Date(2008, 1, 22);

const numDays = Math.round(Math.abs((startDate - endDate) / oneDay));

var arrayDiv = new Array();
for (var i = 0; i < numDays; i++)
{
   arrayDiv[i] = document.createElement('div');
   arrayDiv[i].id = 'block' + i;
   arrayDiv[i].className = 'block' + (i+1);
   arrayDiv[i].textContent = "day " + (i+1) + " " + startDate;
   startDate.setDate(startDate.getDate() + 1);
   document.body.appendChild(arrayDiv[i]);
}


// The problem starts HERE 

// The jquery code is similar to the Add Day button, but yet it the loop
// doesn't create the required lists

for (var i = 0; i < numDays; i++)
{ addList();
}

   function addList() {
              bodyWidth = $("body").width();
              nextWidth = bodyWidth + 300;
              $('body').css('width', nextWidth + 'px');

              var listName = startDate.getDate();

              $("div.orders").append("<div class=\"column\">" +
                      "<div class=\"box\" data-title=\"" + listName + "\">" +
                      "<div class=\"header\">" +
                      "    " + listName +
                      "</div>" +
                      "<div class=\"body\">" +
                      "    <ul id=\"sortable3\" class=\"droptrue\">" +
                      "    </ul>" +
                      "</div>" +
                      "</div></div>");

              initSortable();

          }




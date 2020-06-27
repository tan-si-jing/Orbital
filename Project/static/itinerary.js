$(document).ready(function () {
    $(function () {
        function initSortable() {
            $(".column").sortable({
                connectWith: ".column",
                handle: ".header",
                tolerance: 'intersect'
//                    cancel: ".header"
//                    placeholder: "portlet-placeholder ui-corner-all"
            });


            $("ul.droptrue").sortable({
                connectWith: "ul",
                tolerance: 'intersect'
            });

            $("ul.dropfalse").sortable({
                connectWith: "ul",
                tolerance: 'intersect'
//                    dropOnEmpty: false
            });

            $("#sortable1, #sortable2, #sortable3").disableSelection();
        }

        initSortable();

        $(".btn")
                .button()
                .click(function (event) {
                    event.preventDefault();
                });

        function addOrder() {
            var itnName = $('#itnName').val();
            var country = $('#form-control gds-cr').val();
            var startDate = $('#startDate').val();
            var endDate = $('#endDate').val();
            console.log(country, startDate, endDate);
            $.ajax({
              type: 'POST',
              data: {
                name:itnName,
                country:country,
                start_date:startDate,
                end_date:endDate,
              },
              url: "/newItn"
            })
            dialog.dialog("close");
            return true;
        }

        dialog = $("#dialog-form").dialog({
            autoOpen: false,
            height: 410,
            width: 550,
            modal: true,
            buttons: {
                "Create itinerary": addOrder,
            },

        });


        //this didn't seem to affect code physically
        form = dialog.find("form").on("submit", function (event) {
            event.preventDefault();
            addOrder();
        });

        form = dialog.find("#formList").on("submit", function (event) {
            event.preventDefault();
            addList();
        });
// to this part, even if deleted. Not sure what data it MAY affect
        $("#btnCreateNewOrder").button().on("click", function () {
            dialog.dialog("open");
        });

    });
});

$(document).ready(function () {
    $(function () {
        $(".btn")
                .button()
                .click(function (event) {
                    event.preventDefault();
                });

        function addOrder() {
            var itnName = $('#itnName').val();
            var country = $('#country option:selected').val();
            var startDate = $('#startDate').val();
            var endDate = $('#endDate').val();
            var data = {
              name:itnName,
              country:country,
              start_date:startDate,
              end_date:endDate,
            };
            fetch('/newItn', {
              method: "POST",
              credentials: "include",
              body: JSON.stringify(data),
              headers: new Headers({
                "content-type": "application/json"
              })
            })
            .then(response => {
              if (response.redirected) {
                window.location.href = response.url;
              }
            });
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


        form = dialog.find("form").on("submit", function (event) {
            event.preventDefault();
            addOrder();
        });

        $("#btnCreateNewOrder").button().on("click", function () {
            dialog.dialog("open");
        });

    });
});

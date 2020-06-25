
    $(function () {
        function initSortable() {
            $(".column").sortable({
                connectWith: ".column",
                handle: ".header",
//                    cancel: ".header"
//                    placeholder: "portlet-placeholder ui-corner-all"
            });


            $("ul.droptrue").sortable({
                connectWith: "ul"
            });

            $("ul.dropfalse").sortable({
                connectWith: "ul",
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
            var valid = true;

            if (valid) {
                selectedList = $('#list').find(":selected").text();
                box = $('div').find("[data-title='" + selectedList + "']");
                boxList = box.find('ul');

                var itnName = $('#itnName').val();
                var country = $('#country').val();

                boxList.append("<li class=\"ui-state-highlight\">" + itnName + " - " + country + "</li>");


                dialog.dialog("close");
            }
            return valid;
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

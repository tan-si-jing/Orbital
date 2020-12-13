$(function () {

    function share() {
      var email = $('#email').val();
      var perm = $('#perm option:selected').val();
      var itnum = {{itn.id|tojson}};
      var data = {
        email:email,
        perm:perm,
        itnum:itnum
      };
      if (perm == "Edit") {
        fetch('/share_edit', {
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
      } else {
        fetch('/share_view', {
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
        dialogshare.dialog("close");
        alert("Shared succesfully!");
    }

    dialogshare = $("#share").dialog({
        autoOpen: false,
        height: 250,
        width: 350,
        modal: true,
        buttons: {
            "Share": share,
            Cancel: function () {
                dialogshare.dialog("close");
            }
        },
        close: function () {
          $("#share")[0].reset();
          allFields.removeClass("ui-state-error");
        }
    });

    form = dialog.find("#shareform").on("submit", function (event) {
        event.preventDefault();
        share();
    });

    $("#sharebtn").button().on("click", function () {
        dialogshare.dialog("open");
    });
});

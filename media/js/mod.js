<script type="text/javascript">
    function toggle_hide(show_id) {
        var path = "/mod/toggle/" + show_id;
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState != 4) { return; }
            var response = JSON.parse(xhr.responseText);
            if (response.success === true) {
                $('#hide').html("Hidden: " + Boolean(response.val))
            }
        }
        xhr.open('GET', path, true);
        xhr.send(null);
    }
</script>
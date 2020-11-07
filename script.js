$(document).ready(function() {
    $.ajax({
        method: "GET",
        url: "data.json",
        success: function(hospitals) {
            $.each(hospitals, function(i, hospital) {
                $("#location-data").append("<h1>"+ hospital[0].doc.location + "</h1>");
            });
        },
        error: function() {
            alert("Error loading data");
        }
    });
});
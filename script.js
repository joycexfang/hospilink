$(document).ready(function() {
    $.ajax({
        method: "GET",
        url: "data.json",
        success: function(data) {
            $("#location-data").append("<h1>"+ data.doc.location + "</h1>");
        },
        error: function() {
            alert("Error loading data");
        }
    });
});
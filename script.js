$(document).ready(function() {
    $.ajax({
        method: "GET",
        url: "data.json",
        success: function(hospitals) {
            $.each(hospitals, function(i, hospital) {
                $("#results").append('<div class="row hospital-entry"">\
                <div class="col-sm">' +
                    hospital[0].doc.hospitalname +
                '</div>\
                <div class="col-sm">' +
                    hospital[0].doc.location +
                '</div>\
                <div class="col-sm">' +
                    hospital[0].doc.quantity +
                '</div>\
                <div class="col-sm">\
                    <button type="button" class="btn btn-light request-button">Request</button>\
                </div>\
            </div>');
                $("#location-data").append("<h1>"+ hospital[0].doc.location + "</h1>");
            });
        },
        error: function() {
            alert("Error loading data");
        }
    });

});

{/* <div class="row hospital-entry"">
    <div class="col-sm">
        Hospital Name 1
    </div>
    <div class="col-sm">
        Bronx, NY
    </div>
    <div class="col-sm">
        89
    </div>
    <div class="col-sm">
        <button type="button" class="btn btn-light request-button">Request</button>

    </div>
</div> */}

/*{
    "_id": "f74f46c8c2a24948500e280a375bdab4",
    "_rev": "1-ea2498574104169e9d7e85fb6ecbc5aa",
    "firstName": "John",
    "lastName": "Smith",
    "role": "doctor",
    "hospital": "Samaritan",
    "city": "Troy",
    "state": "New York",
    "phoneNumber": 9000012342
  }
*/

function getSignUpData() {
    var new_accout = []
    new_account.push("Kiwi");
    
    var fname = document.getElementById("fname").value;
    var lname = document.getElementById("lname").value;
    var role = document.getElementById("role").value
    var hospital = document.getElementById("hospital name").value;
    var city = document.getElementById("city").value;
    var state = document.getElementById("state").value;
    var phone = document.getElementById("phone").value;

    

}
$(document).ready(function() {
    $.ajax({
        method: "GET",
        url: "data",
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
                    hospital[0].doc.resources["gloves"] +
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

    new_account.push(document.getElementById("fname").value);
    new_account.push(document.getElementById("lname").value);
    new_account.push(document.getElementById("role").value);
    new_account.push(document.getElementById("hospital name").value);
    new_account.push(document.getElementById("city").value);
    new_account.push(document.getElementById("state").value);
    new_account.push(document.getElementById("phone").value);
}

$.ajax({
    type: "POST",
    url: "accounts.py",
    data: { param: array}
  }).done(function( o ) {
     // do something
  });
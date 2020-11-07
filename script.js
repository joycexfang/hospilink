var location = document.getElementById("location-data");

var obj = JSON.parse("data.json");
location.innerHTML = obj.location;
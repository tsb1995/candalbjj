// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();

jQuery(document).ready(function( $ ) {
    $("#google-reviews").googlePlaces({
            placeId: 'ChIJe-_o2Sgp3YARE02PnQhDX2A' //Find placeID @: https://developers.google.com/places/place-id
        , render: ['reviews']
        , min_rating: 4
        , max_rows:4
    });
});
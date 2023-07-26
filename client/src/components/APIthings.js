const photosFetch = (location) => {
    const response = await fetch()
}

// text search:
maps.googleapis.com/maps/api/place/textsearch/json?query=san%20francisco&view&key=

// details search: (returns up to ten photos in an array) requires 
maps.googleapis.com/maps/api/place/details/json
  ?fields=photo
  &place_id=ChIJIQBpAG2ahYAR_6128GcTUEo

// find place: 1st fetch to get place_id
maps.googleapis.com/maps/api/place/findplacefromtext/json
?input={locationInput}
&inputtype=textquery
&fields=place_id
&key={APIkey}



// search static variables
const maps1Url = maps.googleapis.com/maps/api/place/findplacefromtext/json?input=




//  placeID
  const sfPlaceID = ChIJIQBpAG2ahYAR_6128GcTUEo
  const psPlaceID = ChIJs-Xb_9Qa24ARfHntwodp5aE

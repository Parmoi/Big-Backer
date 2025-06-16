// Function to find the geolocation of current user
function findGeolocation() {
    // Checks if the browers allows geolocation API access
    if (navigator.geolocation) {
        console.log("Geolocation available");

        navigator.geolocation.getCurrentPosition(success)

        // async only continues if it gets back something from await
        async function success(position) {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;

            console.log("lat: "+ lat + " lon: " + lon);
            
            const response = await fetch('/save_location', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ latitude: lat, longitude: lon})
            });

            const result = await response.json();
            console.log(result)
        }
    }
}

// Gets geolocation from session
async function getGeolocation() {
    console.log("Attempting to find geolocation of user");

    // Find element with 'geolocation' id inside document
    const geolocation = document.getElementById('geolocation');

    // Call the get_location route to get saved lat/lon from session
    const response = await fetch('/get_location');

    if (response.ok) {
        // API call returns an "ok" (everything works fine)
        // Find lat/lon and set text in document to it
        const result = await response.json();
        const text = `Latitude: ${result.latitude}, Longitude: ${result.longitude}`;
        geolocation.textContent = text;
    } else {
        // API call returns some error
        geolocation.textContent = "Location not set.";
    }
}
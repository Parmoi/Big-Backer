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
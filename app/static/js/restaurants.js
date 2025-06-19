async function getRestaurants() {
    console.log("Starting to find nearby restaurants");

    const response = await fetch('/get_restaurants');
    
    if (response.ok) {
        const result = await response.json();

        console.log(result);
    }
}
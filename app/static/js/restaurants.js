async function getRestaurants() {
    console.log("Starting to find nearby restaurants");

    const response = await fetch('/get_restaurants');
    
    if (response.ok) {
        const result = await response.json();

        console.log(result);
    }
}

async function getGoogleRestaurants() {
    console.log("Finding places from Google");

    const response = await fetch('/search_places');

    if (response.ok) {
        const result = await response.json();

        console.log(result);
    }
}

async function findFilteredRestaurants() {
    console.log("Getting data from filters");

    // Extract values from the html page
    const query = document.getElementById("query").value;
    const min_rating = document.getElementById("min-rating").value;
    const open_time = document.getElementById("open-time").value;
    const close_time = document.getElementById("close-time").value;

    console.log(`We are trying to find ${query} with minimum rating: ${min_rating}, opens at ${open_time} and closes at ${close_time}`);

    // POST from Javascript frontend to Python backend
    const response = await fetch('/find_filtered_places', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            query: query, 
            min_rating: min_rating,
            open_time: open_time,
            close_time: close_time
        })
    });

    if (response.ok) {
        const result = await response.json();

        console.log("Found the following places:");
        console.log(result);

        // We want to add the places to the table on the html
        const tableBody = document.querySelector('#resultsTable tbody');
        tableBody.innerHTML = ""; // Clear previous results

        // Add a table row for each of the restaurants
        result.place_ids.forEach(restaurant => {
            const row = document.createElement("tr");

            row.innerHTML = `
            <td>${restaurant['id']}</td>
            <td>${restaurant['name']}</td>
            <td>${restaurant['rating']}</td>
            `
            
            tableBody.appendChild(row);
        });

    }
}
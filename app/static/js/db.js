async function addStore() {
    console.log("Trying to add store to db");

    const response = await fetch('/add');

    if (response.ok) {
        const result = await response.json();

        console.log(result);
    }
}

async function returnStores() {
    console.log("Finding stored stores");

    const response = await fetch('/find_stores');

    if (response.ok) {
        const result = await response.json();

        console.log(result);
    }
}
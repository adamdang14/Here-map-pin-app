document.addEventListener('DOMContentLoaded', function () {
    // Initialize HERE map
    const platform = new H.service.Platform({
        apikey: 'BbJHF8nfHAlKOPpqBhMH0EYVrWORPnkVtFUt6p7ON8c' // Replace with your actual API key
    });

    const defaultLayers = platform.createDefaultLayers();
    const map = new H.Map(
        document.getElementById('mapContainer'),
        defaultLayers.vector.normal.map,
        {
            center: { lat: 40.7128, lng: -74.0060 },
            zoom: 5
        }
    );

    // Enable map interactions
    const mapEvents = new H.mapevents.MapEvents(map);
    const behavior = new H.mapevents.Behavior(mapEvents);
    const ui = H.ui.UI.createDefault(map, defaultLayers);

    // Function to add a pin to the map
    function addPinToMap(latitude, longitude, title, description) {
        const marker = new H.map.Marker({ lat: latitude, lng: longitude });
        map.addObject(marker);

        // Add an info bubble when the pin is clicked
        marker.addEventListener('tap', function () {
            const bubble = new H.ui.InfoBubble(
                { lat: latitude, lng: longitude },
                { content: `<b>${title}</b><br>${description}` }
            );
            ui.addBubble(bubble);
        });
    }

    // Fetch pins from the database and display on the map
    fetch('/pins')
        .then(response => response.json())
        .then(pins => {
            pins.forEach(pin => {
                addPinToMap(pin.latitude, pin.longitude, pin.title, pin.description);
            });
        })
        .catch(error => console.error('Error:', error));
});

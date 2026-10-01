// =====================================
// ASTRA GRID - DASHBOARD JAVASCRIPT
// =====================================

// Get sensor data from Flask
async function updateDashboard() {

    try {

        const response = await fetch("/api/data");

        const data = await response.json();


        // -----------------------------
        // TEMPERATURE
        // -----------------------------

        document.getElementById("temperature").textContent =
            Number(data.temperature).toFixed(1);


        // -----------------------------
        // HUMIDITY
        // -----------------------------

        document.getElementById("humidity").textContent =
            Number(data.humidity).toFixed(1);


        // -----------------------------
        // LDR / LIGHT LEVEL
        // -----------------------------

        document.getElementById("ldr").textContent =
            data.ldr;


        // -----------------------------
        // OCCUPANCY
        // -----------------------------

        const occupancyElement =
            document.getElementById("occupancy");

        const decisionOccupancy =
            document.getElementById("decisionOccupancy");


        if (data.occupancy === true) {

            occupancyElement.textContent = "DETECTED";
            decisionOccupancy.textContent = "Detected";

        } else {

            occupancyElement.textContent = "NO MOTION";
            decisionOccupancy.textContent = "No Motion";
        }


        // -----------------------------
        // LIGHTING
        // -----------------------------

        const lightingElement =
            document.getElementById("lighting");

        const decisionLighting =
            document.getElementById("decisionLighting");


        if (data.lighting === true) {

            lightingElement.textContent = "ON";
            decisionLighting.textContent = "ON";

        } else {

            lightingElement.textContent = "OFF";
            decisionLighting.textContent = "OFF";
        }


        // -----------------------------
        // COOLING
        // -----------------------------

        const coolingElement =
            document.getElementById("cooling");

        const decisionCooling =
            document.getElementById("decisionCooling");


        if (data.cooling === true) {

            coolingElement.textContent = "REQUIRED";
            decisionCooling.textContent = "Required";

        } else {

            coolingElement.textContent = "NOT REQUIRED";
            decisionCooling.textContent = "Not Required";
        }


        // -----------------------------
        // SYSTEM STATUS
        // -----------------------------

        document.getElementById("systemStatus").textContent =
            data.system;


        // -----------------------------
        // LAST UPDATED
        // -----------------------------

        const now = new Date();

        document.getElementById("lastUpdated").textContent =
            "Last updated: " + now.toLocaleTimeString();

    }

    catch (error) {

        console.error(
            "Astra Grid connection error:",
            error
        );

    }
}


// Run immediately when dashboard opens
updateDashboard();


// Update every 2 seconds
setInterval(updateDashboard, 2000);
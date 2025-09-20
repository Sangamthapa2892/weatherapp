// DOM Elements
const searchInput = document.getElementById("search-input");
const searchBtn = document.getElementById("search-btn");
const citiesGrid = document.querySelector(".cities-grid");

// Get cities from Django context (assumes it's injected as JSON)
const cities = JSON.parse(
  document.getElementById("popular-cities-data").textContent.trim()
);

// Initialize the app
function initApp() {
  displayCities(cities);

  searchBtn.addEventListener("click", handleSearch);
  searchInput.addEventListener("keyup", (e) => {
    if (e.key === "Enter") handleSearch();
  });
}

// Display city cards
function displayCities(cityList) {
  citiesGrid.innerHTML = "";

  cityList.forEach((city) => {
    const card = document.createElement("div");
    card.className = "city-card";
    card.innerHTML = `
                    <img src="${city.image}" alt="${city.city}" class="city-image">
                    <div class="city-info">
                        <h3 class="city-name">${city.city}</h3>
                        <div class="city-temp">${city.temp}°C</div>
                        <div class="city-weather">${city.desc}</div>
                        <img src="http://openweathermap.org/img/wn/${city.icon}@2x.png" alt="Weather icon">
                    </div>
                `;
    card.addEventListener("click", () => updateCurrentWeather(city.city));
    citiesGrid.appendChild(card);
  });
}

// Search functionality
function handleSearch() {
  const searchTerm = searchInput.value.trim().toLowerCase();

  if (searchTerm) {
    const filtered = cities.filter((city) =>
      city.city.toLowerCase().includes(searchTerm)
    );

    if (filtered.length > 0) {
      displayCities(filtered);
      updateCurrentWeather(filtered[0].city);
    } else {
      citiesGrid.innerHTML =
        '<p class="no-results">No cities found. Try another search.</p>';
    }
  } else {
    displayCities(cities);
  }
}

// Dummy function for updating weather (you can hook this to Django or AJAX)
function updateCurrentWeather(cityName) {
  console.log("Update weather for:", cityName);
  // You could trigger a form submission or AJAX call here
}

window.addEventListener("load", initApp);

//const weatherContainer = document.querySelector('.weather-container');
//const searchInput = document.getElementById('search-input');
//const searchBtn = document.getElementById('search-btn');
//
//// Replace 'YOUR_API_KEY' with your actual API key
//
//const apiKey = 'YOUR_API_KEY';
//let city = 'Izhevsk';
//
//function displayWeatherData(data) {
//    weatherContainer.innerHTML = '';
//
//    for (let i = 0; i < 7; i++) {
//        const dayElement = document.createElement('div');
//        dayElement.classList.add('weather-day');
//
//        const dayName = document.createElement('h2');
//        dayName.classList.add('day-name');
//        dayName.textContent = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][i];
//        dayElement.appendChild(dayName);
//
//        const weatherIcon = document.createElement('div');
//        weatherIcon.classList.add('weather-icon');
//        weatherIcon.innerHTML = '<i class="fas fa-sun"></i>';
//        dayElement.appendChild(weatherIcon);
//
//        const temperature = document.createElement('p');
//        temperature.classList.add('temperature');
//        temperature.innerHTML = `
//            <span class="temp-avg">${data[i].temp.avg.toFixed(1)}</span>°C
//            <span class="temp-max">${data[i].temp.max.toFixed(1)}</span>°C
//            <span class="temp-min">${data[i].temp.min.toFixed(1)}</span>°C
//        `;
//        dayElement.appendChild(temperature);
//
//        const feelsLike = document.createElement('p');
//        feelsLike.classList.add('feels-like');
//        feelsLike.innerHTML = `Feels like: <span class="temp-feels">${data[i].feelsLike.toFixed(1)}</span>°C`;
//        dayElement.appendChild(feelsLike);
//
//        weatherContainer.appendChild(dayElement);
//    }
//}
//
//const sampleData = [
//    { temp: { avg: 20, max: 25, min: 15 }, feelsLike: 18 },
//    { temp: { avg: 18, max: 22, min: 14 }, feelsLike: 16 },
//    { temp: { avg: 17, max: 21, min: 13 }, feelsLike: 15 },
//    { temp: { avg: 19, max: 23, min: 15 }, feelsLike: 17 },
//    { temp: { avg: 21, max: 26, min: 16 }, feelsLike: 19 },
//    { temp: { avg: 22, max: 27, min: 17 }, feelsLike: 20 },
//    { temp: { avg: 20, max: 25, min: 15 }, feelsLike: 18 }
//];
//
//displayWeatherData(sampleData);
//
//searchBtn.addEventListener('click', () => {
//    city = searchInput.value;
//    // Fetch weather data using the API and call displayWeatherData()
//});

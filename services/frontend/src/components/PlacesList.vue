<template>

    <span v-if="showLoader" class="loader"></span>

    <div v-if="!showLoader" :key="box" class="box">
      <div class="place-list"
           v-if="showPlaces === false">
        <a class="active"
            @click="back()"
        >
          Back
        </a>
      </div>

      <div class="place-list"
           v-if="showPlaces === false">
        <a
            @click="updateSelected(place)"
            v-for="(place, index) in places"
            :key="index">
          {{place.country}}: {{place.name}}
        </a>
      </div>
    </div>

    <div v-if="showPlaces">
      <PlaceDetail
          v-on:return-back="this.showPlaces = false;"
          :place="selectedPlace"
          :weather="weather"
          :weather-on-week="weathersOnWeek"
          :weather-icons="weatherIcons"
      />
    </div>

</template>

<script>
import PlaceDetail from "@/components/PlaceDetail";
import axios from "axios";

export default {
  name: "PlacesList",
  emits: ["hide-search-box", "show-search-box"],
  components: {
    PlaceDetail
  },
  data() {
    return {
      showPlaces: false,
      showLoader: false,
      selectedPlace: {},

      weather: {},
      weatherForecast: {},
      weathersOnWeek: [],
      weatherIconsConvert: {
        'Drizzle': 'cloud-drizzle',
        'Thunderstorm': 'cloud-lightning',
        'Rain': 'cloud-rain',
        'Snow': 'cloud-snow',
        'Clouds': 'cloud',
        'Clear': 'sun'
      },
      weatherIcons: [
        'alert-triangle',
        'alert-triangle',
        'alert-triangle',
        'alert-triangle',
        'alert-triangle'
      ],
    }
  },
  props: {
    places: Array
  },
  methods: {
    back () {
      this.$emit('show-search-box');
    },
    async updateSelected (selectedItem) {
      this.$emit('hide-search-box');
      this.showLoader = true;
      let weatherCurrentData = await axios.get('/weather/current', {
        params: {
          lat: selectedItem.point.lat,
          lon: selectedItem.point.lng
        }
      });
      this.weather = weatherCurrentData.data;

      let weatherForecastData = await axios.get('/weather/forecast', {
        params: {
          lat: selectedItem.point.lat,
          lon: selectedItem.point.lng
        }
      });
      this.weatherForecast = weatherForecastData.data;

      this.weatherIcons[0] = this.weatherIconsConvert[this.weather.weather[0].main];

      this.weathersOnWeek = [];
      for (let i in this.weatherForecast.list) {
        let date = new Date(this.weatherForecast.list[i].dt * 1000);
        if (date.getHours() === 13) {
          this.weathersOnWeek.push(this.weatherForecast.list[i])
        }
      }

      console.log(selectedItem)
      console.log(this.weather)

      for (let i = 0; i < this.weathersOnWeek.length; i++) {
        this.weatherIcons[i + 1] = this.weatherIconsConvert[this.weathersOnWeek[i].weather[0].main];
      }

      this.selectedPlace = selectedItem;
      this.showPlaces = true;
      this.showLoader = false;
    }
  }
}
</script>

<style scoped>

body {
  margin: 0;
  padding: 0;
  font-family: 'Montserrat', sans-serif;
  font-size: 12px
}

.list-group-item {
  display: block;
  text-decoration: none;
  margin: 1em 0.2em;
  color: #ffffff;
}

.list-group-item:hover {
  color: #646464;
}

.place-list {
  border-radius: 10px;
  -webkit-box-shadow: 0 0 50px -5px rgba(0, 0, 0, 0.25);
  box-shadow: 0 0 50px -5px rgba(0, 0, 0, 0.25);
  margin: 10px 35px;
}

.place-list>a {
  display: block;
  text-decoration: none;

  padding: 15px;
  cursor: pointer;
  -webkit-transition: 200ms ease;
  -o-transition: 200ms ease;
  transition: 200ms ease;
  border-radius: 10px;
  color: #ffffff;
}

.place-list>a.active {
  background: #fff;
  color: #222831;
  border-radius: 10px;
}

.place-list>a:hover {
  -webkit-transform: scale(1.1);
  -ms-transform: scale(1.1);
  transform: scale(1.1);
  background: #fff;
  color: #222831;
  -webkit-box-shadow: 0 0 40px -5px rgba(0, 0, 0, 0.2);
  box-shadow: 0 0 40px -5px rgba(0, 0, 0, 0.2)
}

.box {
  position: relative;
  height:auto;

  animation: fadeIn 3s;
  -webkit-animation: fadeIn 3s;
  -moz-animation: fadeIn 3s;
  -o-animation: fadeIn 3s;
  -ms-animation: fadeIn 3s;
}

@keyframes fadeIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}

@-moz-keyframes fadeIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}

@-webkit-keyframes fadeIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}

@-o-keyframes fadeIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}

@-ms-keyframes fadeIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}

</style>
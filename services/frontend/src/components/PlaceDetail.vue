<template>
  <div class="container">
    <div class="weather-side">
      <div class="weather-gradient"></div>
      <div class="date-container">
        <h2 class="date-dayname">{{ this.currentDayName }}</h2>
        <span class="date-day">{{ this.currentDate }}</span>
        <i class="location-icon" data-feather="map-pin"></i>
        <span class="location">{{this.place.name}}</span>
      </div>
      <div class="weather-container">
        <i class="weather-icon" :data-feather="weatherIcons[0]"></i>
        <h1 class="weather-temp">{{ kelvinToCelsius(weather.main.temp) }}°C</h1>
        <h3 class="weather-desc">{{ iconsWeatherConvert[weatherIcons[0]] }}</h3>
      </div>
    </div>
    <div class="info-side">
      <div class="today-info-container">
        <div class="today-info">
          <div class="humidity">
            <span class="title">HUMIDITY</span>
            <span class="value">{{weather.main.humidity}} %</span>
            <div class="clear"></div>
          </div>
          <div class="wind">
            <span class="title">WIND</span>
            <span class="value">{{weather.wind.speed}} m/s</span>
            <div class="clear"></div>
          </div>
          <div class="feels_like">
            <span class="title">FEELS LIKE</span>
            <span class="value">{{kelvinToCelsius(weather.main.feels_like)}}°C</span>
            <div class="clear"></div>
          </div>
        </div>
      </div>
      <div class="week-container">
        <ul class="week-list">
          <li class="active">
            <i class="day-icon" :data-feather="weatherIcons[1]"></i>
            <span class="day-name">{{ nextDaysNames[0] }}</span>
            <span class="day-temp">{{kelvinToCelsius(weatherOnWeek[0].main.temp)}}°C</span>
          </li>

          <li>
            <i class="day-icon" :data-feather="weatherIcons[2]"></i>
            <span class="day-name">{{ nextDaysNames[1] }}</span>
            <span class="day-temp">{{kelvinToCelsius(weatherOnWeek[1].main.temp)}}°C</span>
          </li>

          <li>
            <i class="day-icon" :data-feather="weatherIcons[3]"></i>
            <span class="day-name">{{ nextDaysNames[2] }}</span>
            <span class="day-temp">{{kelvinToCelsius(weatherOnWeek[2].main.temp)}}°C</span>
          </li>

          <li>
            <i class="day-icon" :data-feather="weatherIcons[4]"></i>
            <span class="day-name">{{ nextDaysNames[3] }}</span>
            <span class="day-temp">{{kelvinToCelsius(weatherOnWeek[3].main.temp)}}°C</span>
          </li>

          <div class="clear"></div>
        </ul>
      </div>
      <div class="location-container">
        <button class="location-button" v-on:click="returnBack">
          <i data-feather="map-pin"></i>
          <span>Change location</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import feather from 'feather-icons'

export default {
  name: "PlaceDetail",
  data() {
    return {
      iconsWeatherConvert: {
        'cloud-drizzle': 'Drizzle' ,
        'cloud-lightning': 'Thunderstorm',
        'cloud-rain': 'Rain' ,
        'cloud-snow': 'Snow' ,
        'cloud': 'Clouds',
        'sun': 'Clear'
      },
      currentDayName: '',
      nextDaysNames: [],
      currentDate: '',
    }
  },
  props: {
    place: JSON,
    weather: JSON,
    weatherIcons: Array,
    weatherOnWeek: Array
  },
  methods: {
    returnBack() {
      this.$emit('return-back');
    },
    getNameOfDay(d, isAbbr) {
      if (isAbbr) {
        let daysAbbr = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
        return daysAbbr[d.getDay()];
      }
      let daysNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
      return daysNames[d.getDay()];
    },
    getMonthName(d) {
      const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
      return monthNames[d.getMonth()];
    },
    kelvinToCelsius(t) {
      return Math.round((t - 273.15))  ;
    }
  },
  computed: {
  },
  async mounted() {
    let date = new Date();
    this.currentDayName = this.getNameOfDay(date, false);
    this.currentDate = date.getUTCDate() + ' ' + this.getMonthName(date) + ' ' + date.getFullYear();

    for (let i = 0; i < 4; i++) {
      date.setDate(date.getDate() + 1);
      this.nextDaysNames.push(this.getNameOfDay(date, true));
    }


    feather.replace();
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css?family=Montserrat:400,700,900&display=swap');

:root {
  --gradient: linear-gradient( 135deg, #72EDF2 10%, #5151E5 100%);
}

* {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  line-height: 1.25em;
}

.clear {
  clear: both;
}

body {
  margin: 0;
  width: 100%;
  height: 100vh;
  font-family: 'Montserrat', sans-serif;
  background-color: #343d4b;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
}

.container {
  animation: fadeIn 3s;
  -webkit-animation: fadeIn 3s;
  -moz-animation: fadeIn 3s;
  -o-animation: fadeIn 3s;
  -ms-animation: fadeIn 3s;

  border-radius: 25px;
  -webkit-box-shadow: 0 0 70px -10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 0 70px -10px rgba(0, 0, 0, 0.2);
  background-color: #222831;
  color: #ffffff;
  height: 400px;
}

.weather-side {
  position: relative;
  height: 100%;
  border-radius: 25px;
  width: 300px;
  -webkit-box-shadow: 0 0 20px -10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 0 20px -10px rgba(0, 0, 0, 0.2);
  -webkit-transition: -webkit-transform 300ms ease;
  transition: -webkit-transform 300ms ease;
  -o-transition: transform 300ms ease;
  transition: transform 300ms ease;
  transition: transform 300ms ease, -webkit-transform 300ms ease;
  -webkit-transform: translateZ(0) scale(1.02) perspective(1000px);
  transform: translateZ(0) scale(1.02) perspective(1000px);
  float: left;
}

.weather-side:hover {
  -webkit-transform: scale(1.1) perspective(1500px) rotateY(10deg);
  transform: scale(1.1) perspective(1500px) rotateY(10deg);
}

.weather-gradient {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  background-image: var(--gradient);
  border-radius: 25px;
  opacity: 0.8;
}

.date-container {
  position: absolute;
  top: 25px;
  left: 25px;
}

.date-dayname {
  margin: 0;
}

.date-day {
  display: block;
}

.location {
  display: inline-block;
  margin-top: 10px;
}

.location-icon {
  display: inline-block;
  height: 0.8em;
  width: auto;
  margin-right: 5px;
}

.weather-container {
  position: absolute;
  bottom: 25px;
  left: 25px;
}

.weather-icon.feather {
  height: 60px;
  width: auto;
}

.weather-temp {
  margin: 0;
  font-weight: 700;
  font-size: 4em;
}

.weather-desc {
  margin: 0;
}

.info-side {
  position: relative;
  float: left;
  height: 100%;
  padding-top: 25px;
}

.today-info {
  padding: 15px;
  margin: 0 25px 25px 25px;
  /* 	box-shadow: 0 0 50px -5px rgba(0, 0, 0, 0.25); */
  border-radius: 10px;
}

.today-info>div:not(:last-child) {
  margin: 0 0 10px 0;
}

.today-info>div .title {
  float: left;
  font-weight: 700;
}

.today-info>div .value {
  float: right;
}

.week-list {
  list-style-type: none;
  padding: 0;
  margin: 10px 35px;
  -webkit-box-shadow: 0 0 50px -5px rgba(0, 0, 0, 0.25);
  box-shadow: 0 0 50px -5px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
}

.week-list>li {
  float: left;
  padding: 15px;
  cursor: pointer;
  -webkit-transition: 200ms ease;
  -o-transition: 200ms ease;
  transition: 200ms ease;
  border-radius: 10px;
}

.week-list>li:hover {
  -webkit-transform: scale(1.1);
  -ms-transform: scale(1.1);
  transform: scale(1.1);
  background: #fff;
  color: #222831;
  -webkit-box-shadow: 0 0 40px -5px rgba(0, 0, 0, 0.2);
  box-shadow: 0 0 40px -5px rgba(0, 0, 0, 0.2)
}

.week-list>li.active {
  background: #fff;
  color: #222831;
  border-radius: 10px;
}

.week-list>li .day-name {
  display: block;
  margin: 10px 0 0 0;
  text-align: center;
}

.week-list>li .day-icon {
  display: block;
  height: 30px;
  width: auto;
  margin: 0 auto;
}

.week-list>li .day-temp {
  display: block;
  text-align: center;
  margin: 10px 0 0 0;
  font-weight: 700;
}

.location-container {
  padding: 25px 35px;
}

.location-button {
  outline: none;
  width: 100%;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  border: none;
  border-radius: 25px;
  padding: 10px;
  font-family: 'Montserrat', sans-serif;
  background-image: var(--gradient);
  color: #ffffff;
  font-weight: 700;
  -webkit-box-shadow: 0 0 30px -5px rgba(0, 0, 0, 0.25);
  box-shadow: 0 0 30px -5px rgba(0, 0, 0, 0.25);
  cursor: pointer;
  -webkit-transition: -webkit-transform 200ms ease;
  transition: -webkit-transform 200ms ease;
  -o-transition: transform 200ms ease;
  transition: transform 200ms ease, -webkit-transform 200ms ease;
}

.location-button:hover {
  -webkit-transform: scale(0.95);
  -ms-transform: scale(0.95);
  transform: scale(0.95);
}

.location-button .feather {
  height: 1em;
  width: auto;
  margin-right: 5px;
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
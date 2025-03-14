<template>
  <div>
    <DatePicker v-if="step === 1" @next="handleDateSelect" />

    <UserData
      v-if="step === 2"
      :selectedDate="selectedDate"
      :user="user"
      @share="handleShare"
    />

    <ShareData v-if="step === 3" :shareLink="shareLink" @back="handleBack" />

    <div v-if="step === 4">
      <h1>Данные пользователя</h1>
      <p>Дата: {{ selectedDate }}</p>
      <p>Имя: {{ user.firstName }}</p>
      <p>Фамилия: {{ user.lastName }}</p>
      <p>Username: {{ user.username }}</p>
    </div>

    <div v-if="step === 0">
      <h1>Error</h1>
      <p>Здесь ничего нет, потому что ты не через бота, да и ссылка видимо не та :\ @Poni_Ponibot</p>
    </div>
  </div>
</template>

<script>
import DatePicker from "./components/DatePicker.vue";
import UserData from "./components/BirthdayCountdown.vue";
import ShareData from "./components/BirthdayCountdownShared.vue";

export default {
  components: {
    DatePicker,
    UserData,
    ShareData,
  },
  data() {
    return {
      step: 1,
      selectedDate: null,
      user: null,
      shareLink: null,
    };
  },
  mounted() {
    const urlParams = new URLSearchParams(window.location.search);

    if (urlParams.has("firstName")) {
      this.user = {
        firstName: urlParams.get("firstName"),
        lastName: urlParams.get("lastName"),
        username: urlParams.get("username"),
      };
      this.selectedDate = urlParams.get("selectedDate");
      this.step = 4;
    } else {
      const tg = window.Telegram.WebApp;
      if (tg.initDataUnsafe.user) {
        this.user = {
          firstName: tg.initDataUnsafe.user.first_name || "Не указано",
          lastName: tg.initDataUnsafe.user.last_name || "Не указано",
          username: tg.initDataUnsafe.user.username || "Не указано",
        };
      } else {
        this.step = 0;
      }
    }
  },
  methods: {
    handleDateSelect(date) {
      this.selectedDate = date;
      this.fetchUserData();
      this.step = 2;
    },

    fetchUserData() {
      const tg = window.Telegram.WebApp;
      if (tg.initDataUnsafe.user) {
        this.user = {
          firstName: tg.initDataUnsafe.user.first_name || "Не указано",
          lastName: tg.initDataUnsafe.user.last_name || "Не указано",
          username: tg.initDataUnsafe.user.username || "Не указано",
        };
      }
    },

    handleShare() {
      const baseUrl = window.location.origin + window.location.pathname;
      const queryParams = new URLSearchParams({
        firstName: this.user.firstName,
        lastName: this.user.lastName,
        username: this.user.username,
        selectedDate: this.selectedDate,
      }).toString();

      this.shareLink = `${baseUrl}?${queryParams}`;

      navigator.clipboard.writeText(this.shareLink).then(() => {
        alert("Ссылка скопирована в буфер обмена!");
      });

      this.step = 3;
    },

    handleBack() {
      this.step = 2;
    },
  },
};
</script>
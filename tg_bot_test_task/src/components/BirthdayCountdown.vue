<template>
  <div>
    <h1>Ваши данные</h1>
    <p>Дата: {{ selectedDate }}</p>
    <p>Имя: {{ user.firstName }}</p>
    <p>Фамилия: {{ user.lastName }}</p>
    <p>Username: {{ user.username }}</p>
    <button @click="onShare">Поделиться</button>
  </div>
</template>

<script>
export default {
  props: {
    selectedDate: String,
    user: Object,
  },
  methods: {
    onShare() {
      this.$emit("share");
    },
  },
};
</script>
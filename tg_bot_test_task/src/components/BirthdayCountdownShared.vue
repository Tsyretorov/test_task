<template>
  <div>
    <h1>Поделиться данными</h1>
    <p>Ссылка: <a :href="shareLink" target="_blank">{{ shareLink }}</a></p>
    <button @click="onBack">Назад</button>
  </div>
</template>

<script>
export default {
  props: {
    shareLink: String,
  },
  methods: {
    onBack() {
      this.$emit("back");
    },
  },
};
</script>
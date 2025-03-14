<template>
  <div class="home">
    <h1>Выберите дату</h1>
    <DatePicker />
  </div>
</template>

<script setup>
import DatePicker from '@/components/DatePicker.vue';
</script>

<style>
.home {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background: linear-gradient(135deg, #ff9ff3, #f368e0); /* Розово-фиолетовый градиент */
  color: white;
}
</style>
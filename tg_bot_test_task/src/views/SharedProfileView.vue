<template>
  <div class="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-pink-400 to-purple-600 text-white">
    <div class="w-full max-w-md bg-white/10 rounded-xl p-6 backdrop-blur-lg">
      <h1 class="text-2xl font-bold mb-6 text-center">Профиль пользователя</h1>
      
      <!-- Данные из Telegram -->
      <div class="space-y-4 mb-8">
        <div>
          <label class="text-sm opacity-75">Имя</label>
          <div class="text-lg font-medium">{{ userStore.firstName }}</div>
        </div>
        
        <div>
          <label class="text-sm opacity-75">Фамилия</label>
          <div class="text-lg font-medium">{{ userStore.lastName }}</div>
        </div>
        
        <div>
          <label class="text-sm opacity-75">Юзернейм</label>
          <div class="text-lg font-medium">@{{ userStore.username }}</div>
        </div>
      </div>

      <!-- Выбранная дата -->
      <div class="bg-white/20 rounded-lg p-4 text-center">
        <div class="text-sm opacity-75 mb-2">Дата рождения:</div>
        <div class="text-2xl font-bold">
          {{ userStore.selectedDay }} {{ userStore.selectedMonth }} {{ userStore.selectedYear }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/userStore';
import { onMounted } from 'vue';
import { useRoute } from 'vue-router';

const userStore = useUserStore();
const route = useRoute();

// Загружаем данные по ID из URL
onMounted(() => {
  const shareId = route.params.id;
  if (shareId) {
    userStore.loadSharedData(shareId);
  }
});
</script>
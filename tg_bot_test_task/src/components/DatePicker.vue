<template>
  <div class="main_container">
    <h1 class="text_date">Введи свою дату рождения</h1>
    
    <div class="container_choose_date">
      <div class="wheel-container">
        <div class="wheel" ref="dayWheel" @scroll="handleScroll('day')">
          <div 
            v-for="(day, index) in tripledDays" 
            :key="index" 
            class="wheel-item"
          >
            {{ day }}
          </div>
        </div>
      </div>

      <div class="wheel-container">
        <div class="wheel" ref="monthWheel" @scroll="handleScroll('month')">
          <div 
            v-for="(month, index) in tripledMonths" 
            :key="index" 
            class="wheel-item"
          >
            {{ month }}
          </div>
        </div>
      </div>

      <div class="wheel-container">
        <div class="wheel" ref="yearWheel" @scroll="handleScroll('year')">
          <div 
            v-for="(year, index) in tripledYears" 
            :key="index" 
            class="wheel-item"
          >
            {{ year }}
          </div>
        </div>
      </div>
    </div>

    <button class="button_choose_date button_choose_date_color" @click="onNext">
      Продолжить
    </button>
  </div>
</template>

<script setup>
import { ref, onMounted} from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/userStore.ts'

const router = useRouter()
const userStore = useUserStore()
const selectedDate = ref('')

const days = Array.from({ length: 31 }, (_, i) => i + 1);
const months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'];
const years = Array.from({ length: 100 }, (_, i) => new Date().getFullYear() - i);

const tripledDays = [...days, ...days, ...days, ...days];
const tripledMonths = [...months, ...months, ...months, ...months];
const tripledYears = [...years, ...years, ...years, ...years];

const dayWheel = ref(null);
const monthWheel = ref(null);
const yearWheel = ref(null);

const selectedDay = ref(1);
const selectedMonth = ref('Январь');
const selectedYear = ref(new Date().getFullYear());

onMounted(() => {
  const initScroll = (element, values, initialValue) => {
    const middleIndex = values.length * 1;
    element.scrollTop = middleIndex * 50 + values.indexOf(initialValue) * 50;
  };

  initScroll(dayWheel.value, days, 1);
  initScroll(monthWheel.value, months, 'Январь');
  initScroll(yearWheel.value, years, new Date().getFullYear());
});

const handleScroll = (type) => {
  const wheel = {
    day: dayWheel.value,
    month: monthWheel.value,
    year: yearWheel.value
  }[type];

  const items = {
    day: tripledDays,
    month: tripledMonths,
    year: tripledYears
  }[type];

  const originalItems = {
    day: days,
    month: months,
    year: years
  }[type];

  const scrollPosition = wheel.scrollTop;
  const selectedIndex = Math.floor(scrollPosition / 50) % originalItems.length;

  const safeZone = originalItems.length * 50;
  if (scrollPosition < safeZone || scrollPosition > safeZone * 2) {
    wheel.scrollTop = safeZone + selectedIndex * 50;
  }

  const centerIndex = Math.floor((scrollPosition + 150) / 50) % originalItems.length;

  if (type === 'day') {
    selectedDay.value = originalItems[centerIndex];
  } else if (type === 'month') {
    selectedMonth.value = originalItems[centerIndex];
  } else if (type === 'year') {
    selectedYear.value = originalItems[centerIndex];
  }
};

// const handleContinue = () => {
//   alert(`Выбрана дата: ${selectedDay.value} ${selectedMonth.value} ${selectedYear.value}`);
//   userStore.setSelectedDate(selectedDay.value, selectedMonth.value, selectedYear.value);
//   router.push('/profile')
// };

const emit = defineEmits(['next']);

const onNext = () => {
  if (!selectedDay.value || !selectedMonth.value || !selectedYear.value) {
    alert("Пожалуйста, заполните все поля даты");
    return;
  }

  const selectedDate = `${selectedYear.value}-${String(selectedMonth.value).padStart(2, '0')}-${String(selectedDay.value).padStart(2, '0')}`;
  emit('next', selectedDate);
};

</script>

<style scoped>

.main_container{
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-image: linear-gradient(to bottom right, #053742, #053742, #8B5CF6);
  color: white;
}

.text_date {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 3rem;
}

.container_choose_date {
  display: flex;
  gap: 2rem;
  position: relative;
}

.button_choose_date {
  margin-top: 3rem;
  padding: 0.75rem 2rem;
  background-color: white;
  color: black;
  border-radius: 0.75rem;
  font-size: 1.125rem;
  font-weight: 700;
}

.button_choose_date_color:hover {
    background-color: rgba(255, 255, 255, 0.9);
}

.wheel-container {
  height: 350px;
  width: 120px;
  overflow: hidden;
  position: relative;
}

.wheel {
  height: 350px;
  overflow-y: scroll;
  scroll-snap-type: y mandatory;
  scroll-behavior: smooth;
}

.wheel::-webkit-scrollbar {
  display: none;
}

.wheel-item {
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  scroll-snap-align: start;
  transition: all 0.2s;
}

.wheel-item:hover {
  transform: scale(1.1);
}
</style>
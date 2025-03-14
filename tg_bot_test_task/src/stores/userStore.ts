import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import { v4 as uuidv4 } from 'uuid';

export const useUserStore = defineStore('user', () => {
  const firstName = ref('');
  const lastName = ref('');
  const username = ref('');

  const selectedDay = ref(0);
  const selectedMonth = ref('');
  const selectedYear = ref(0);

  const shareId = ref('');

  const ts = computed(() => {
    return `${firstName.value} ${lastName.value}`;
  });

  const initFromTelegram = () => {
    if (window.Telegram?.WebApp?.initDataUnsafe?.user) {
      const user = window.Telegram.WebApp.initDataUnsafe.user;
      firstName.value = user.first_name || '';
      lastName.value = user.last_name || '';
      username.value = user.username || '';
    }
  };

  const setSelectedDate = (day: number, month: string, year: number) => {
    selectedDay.value = day;
    selectedMonth.value = month;
    selectedYear.value = year;
  };

  const generateShareLink = () => {
    const id = uuidv4();
    shareId.value = id;

    localStorage.setItem(`sharedData_${id}`, JSON.stringify({
      firstName: firstName.value,
      lastName: lastName.value,
      username: username.value,
      selectedDay: selectedDay.value,
      selectedMonth: selectedMonth.value,
      selectedYear: selectedYear.value,
    }));

    return `${window.location.origin}/share/${id}`;
  };

  const loadSharedData = (id: string) => {
    const data = localStorage.getItem(`sharedData_${id}`);
    if (data) {
      const parsedData = JSON.parse(data);
      firstName.value = parsedData.firstName;
      lastName.value = parsedData.lastName;
      username.value = parsedData.username;
      selectedDay.value = parsedData.selectedDay;
      selectedMonth.value = parsedData.selectedMonth;
      selectedYear.value = parsedData.selectedYear;
    }
  };

  return {
    firstName,
    lastName,
    username,
    selectedDay,
    selectedMonth,
    selectedYear,
    shareId,
    ts,
    initFromTelegram,
    setSelectedDate,
    generateShareLink,
    loadSharedData,
  };
});
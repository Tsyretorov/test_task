import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import BirthdayCountdown from '../components/BirthdayCountdown.vue';
import BirthdayCountdownShared from '../components/BirthdayCountdownShared.vue';

const routes = [
  {
    path: '/',
    component: HomeView
  },
  {
    path: '/profile',
    component: BirthdayCountdown
  },
  {
    path: '/share/:id',
    component: BirthdayCountdownShared,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router
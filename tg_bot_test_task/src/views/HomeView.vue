<script>
import DatePicker from '@/components/DatePicker.vue';

export default {
  components: {
    DatePicker
  }
};
</script>

<template>
  <div>
    <DatePicker />
  </div>
</template>

<style>
body {
  position: relative;
}

body::before,
body::after {
  content: "";
  position: absolute;
  left: 21%;
  width: 60%;
  height: 1px;
  background-color: white;
  z-index: 1;
}

body::before {
  top: 47%;
}

body::after {
  bottom: 48%;
}
</style>
<template>
  <div>
    <h1>Activity Guidelines Website</h1>
    <h2>Guidelines</h2>

    <ul>
      <li v-for="item in guidelines" :key="item.id">
        <strong>{{ item.age_group }}</strong> – {{ item.label }}: {{ item.point }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const guidelines = ref([])

onMounted(async () => {
  const response = await fetch('https://activity-guidelines-api-dwgghmfahygthbgb.australiaeast-01.azurewebsites.net')
    
  // const response = await fetch('http://127.0.0.1:8000/guidelines')
  const json = await response.json()
  guidelines.value = json.data
})
</script>


<style scoped>
body {
  font-family: Arial, sans-serif;
}
</style>

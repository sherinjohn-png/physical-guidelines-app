<template>
    <div>
      <h2>Guidelines</h2>
      <ul v-if="guidelines.length">
        <li v-for="item in guidelines" :key="item.id">
          <strong>{{ item.label }}</strong>: {{ item.point }}
        </li>
      </ul>
      <p v-else>Loading...</p>
    </div>
  </template>
  
  <script setup>
  import { onMounted, ref } from 'vue'
  
  const guidelines = ref([])
  
  onMounted(async () => {
    try {
      const res = await fetch('http://127.0.0.1:8000/guidelines')
      const data = await res.json()
      guidelines.value = data.data
    } catch (error) {
      console.error('Failed to load guidelines:', error)
    }
  })
  </script>
  
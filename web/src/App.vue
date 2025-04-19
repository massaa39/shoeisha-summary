<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl mb-4">記事要約システム</h1>
    <textarea v-model="inputText" placeholder="要約したい記事を入力" class="w-full h-40 p-2 border"></textarea>
    <button @click="summarize" class="mt-2 px-4 py-2 bg-blue-600 text-white rounded">要約生成</button>
    <div v-if="summary" class="mt-4">
      <h2 class="text-xl">要約結果</h2>
      <p>{{ summary.text }}</p>
      <h3 class="text-lg mt-2">タイトル</h3>
      <p>{{ summary.title }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return { inputText: '', summary: null };
  },
  methods: {
    async summarize() {
      const res = await axios.post('/api/summarize', { text: this.inputText });
      this.summary = res.data;
    }
  }
};
</script>
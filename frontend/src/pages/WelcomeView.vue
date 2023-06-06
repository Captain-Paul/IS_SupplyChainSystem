<template>
  <el-container>
    <el-main>
      <el-card class="el-card">
        <p>Welcome, {{ username }}!</p>
      </el-card>
    </el-main>
  </el-container>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  created() {
    this.username = localStorage.getItem('username');
    this.password = localStorage.getItem('password');
  }
};
</script>

<style scoped>

.el-card {
  margin: 10px auto;
  width: 400px;
  padding: 20px;
  text-align: center;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
</style>

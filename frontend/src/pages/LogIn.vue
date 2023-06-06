<template>
  <div class="login-container">
    <el-form
      ref="loginForm"
      :model="loginForm"
      class="login-form"
      :rules="rules"
    >
      <h2 class="login-title">登录</h2>

      <el-form-item label="用户名" prop="username">
        <el-input 
        v-model="loginForm.username" 
        placeholder="请输入用户名"
        prefix-icon="el-icon-user"
        ></el-input>
      </el-form-item>

      <el-form-item label="密码" prop="password">
        <el-input
          v-model="loginForm.password"
          type="password"
          placeholder="请输入密码"
          show-password
          prefix-icon="el-icon-lock"
        ></el-input>
      </el-form-item>

      <el-form-item label="登录角色" prop="role">
        <el-select v-model="loginForm.role" placeholder="请选择登录角色">
          <el-option
            v-for="option in options"
            :key="option.choice"
            :label="option.label"
            :value="option.choice"
          ></el-option>
        </el-select>
      </el-form-item>

      <el-form-item class="button-group">
        <el-button type="primary" @click="submitForm">登录</el-button>
        <el-button @click="resetForm('loginForm')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      loginForm: {
        username: '',
        password: '',
        role: ''
      },
      options: [
        { choice: 'sale', label: '销售管理员' },
        { choice: 'st', label: '库存管理员' },
        { choice: 'hr', label: '人事管理员' },
        { choice: 'trans', label: '运输管理员' },
        { choice: 'fin', label: '财务管理员' }
      ],
      rules: {
        username: [{ required: true, message: '请输入用户名', trigger: 'blur' },],
        password: [{ required: true, message: '请输入密码', trigger: 'blur' }],
      },
    };
  },
  methods: {
    submitForm() {
      // 发送登录请求
      axios.get('http://127.0.0.1:8000/user/login?username=' + this.loginForm.username + '&pw=' + this.loginForm.password + '&role=' + this.loginForm.role, {
        auth: {
          username: this.loginForm.username,
          password: this.loginForm.password
      }
    }).then(response => {
        // 登录成功，处理响应数据
        console.log('登录成功:', response.data);
        if (this.loginForm.role == 'sale'){this.$router.push('/salemanager')}
        if (this.loginForm.role == 'st'){this.$router.push('/storemanager')}
        if (this.loginForm.role == 'hr'){this.$router.push('/hrmanager')}
        if (this.loginForm.role == 'trans'){this.$router.push('/transportmanager')}
        if (this.loginForm.role == 'fin'){this.$router.push('/financialmanager')}
        // 进行页面跳转或其他操作
      })
      .catch(error => {
        // 登录失败，处理错误信息
        console.error('登录失败:', error.response.data);
      });
      console.log('登录表单：', this.loginForm);
      
      
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  background-color: skyblue;
  justify-content: center;
  align-items: center;
  height: 100vh;
  overflow: hidden;
}

.login-form {
  width: 350px;
  margin: 150px auto;
  background-color: burlywood;
  padding: 30px;
  border-radius: 20px;
}

.login-title {
  text-align: center;
  margin-bottom: 20px;
}

.button-group {
  display: flex;
  justify-content: space-between;
}
</style>

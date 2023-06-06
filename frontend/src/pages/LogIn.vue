<template>
  <div class="login-container">
    <!-- <h1>生鲜供应链后台管理系统</h1> -->
    <transition name="slide-down">
      
      <el-form
      ref="loginForm"
      :model="loginForm"
      class="login-form"
      :rules="rules"
      v-show="showForm"
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
    </transition>
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
        { choice: 'store', label: '库存管理员' },
        { choice: 'hr', label: '人事管理员' },
        { choice: 'trans', label: '运输管理员' },
        { choice: 'fin', label: '财务管理员' }
      ],
      rules: {
        username: [{ required: true, message: '请输入用户名', trigger: 'blur' },],
        password: [{ required: true, message: '请输入密码', trigger: 'blur' }],
      },showForm: false,
    };
  },mounted() {
    setTimeout(() => {
      this.showForm = true;
    }, 500);
  },
  methods: {
    submitForm() {
      axios.get('http://127.0.0.1:8000/user/login?username=' + this.loginForm.username + '&pw=' + this.loginForm.password + '&role=' + this.loginForm.role, {
        auth: {username: this.loginForm.username,password: this.loginForm.password}
    }).then(response => {
        localStorage.setItem("username", this.loginForm.username);
        localStorage.setItem("password", this.loginForm.password);
        if (response.data==='指定的用户不存在.' || response.data==='指定的部门不存在.'){this.$message.error(response.data);return false}
        if (this.loginForm.role == 'sale'){this.$router.push('/salemanager')}
        if (this.loginForm.role == 'store'){this.$router.push('/storemanager')}
        if (this.loginForm.role == 'hr'){this.$router.push('/hrmanager')}
        if (this.loginForm.role == 'trans'){this.$router.push('/transportmanager')}
        if (this.loginForm.role == 'fin'){this.$router.push('/financialmanager')}
      })
      .catch(error => {this.$message.error('登录失败:', error.response.data);});      
      
    },
    resetForm(formName) {this.$refs[formName].resetFields();},
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  background-image: url('@/assets/bg.jpg');
  background-size: cover;
  justify-content: center;
  align-items: center;
  height: 100vh;
  overflow: hidden;
}

.login-form {
  width: 350px;
  margin: 150px auto;
  background-color: rgba(230, 216, 94, 0.767);
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
/* 定义过渡动画的样式 */
.slide-down-enter-active,
.slide-down-leave-active {
  transition: transform 2s;
}

.slide-down-enter,
.slide-down-leave-to {
  transform: translateY(-100%);
}
</style>

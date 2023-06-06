<template>
    <div>
      <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="80px">
        <el-row>
          <el-col :span="18" :offset="4">
            <el-form-item label="仓库编号" prop="wh_id" required>
              <el-input v-model="ruleForm.wh_id" placeholder="请输入四个大写字母+四个数字"></el-input>
            </el-form-item>
            <el-form-item label="仓库位置" prop="wh_loc" required>
              <el-input v-model="ruleForm.wh_loc"></el-input>
            </el-form-item>
            <el-form-item label="仓库名称" prop="wh_name" required>
              <el-input v-model="ruleForm.wh_name"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-col :span="20" :offset="2" class="button-row">
          <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">添加</el-button>
            <el-button @click="resetForm('ruleForm')">重置</el-button>
          </el-form-item>
        </el-col>
      </el-form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data() {
      return {
        ruleForm: {
          wh_id:'',
          wh_name: '',
          wh_loc:''
        },
        nowadays: '',
        rules: {
          wh_id: [{ required: true, message: '请输入仓库编号', trigger: 'blur' },
          { pattern: /^[A-Z]{4}\d{4}$/, message: '仓库编号必须为四个大写字母和四个数字的组合', trigger: 'blur' }],
          wh_loc: [{required: true, message: '请输入仓库位置', trigger: 'blur' }],
          wh_name: [{ required: true, message: '请输入仓库名称', trigger: 'blur' }],
        },
        username: '',password: '',gOptions: [],whOptions:[],
      };
    },
    created() {
      this.username = localStorage.getItem('username');
      this.password = localStorage.getItem('password');
    },
    methods: {
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            const data = this.ruleForm;
            const basicAuth = 'Basic ' + btoa(this.username + ':' + this.password);
            axios
              .post('http://127.0.0.1:8000/fresh/warehouse/list/',data,{headers:{Authorization: basicAuth}})
              .then((response) => {
                this.$message.success('数据提交成功');
                console.log('数据提交成功', response.data);
              })
              .catch((error) => {
                this.$message.error('数据提交失败', error);
              });
          } else {this.$message.error('数据提交失败,请重新检查表单');return false;}
        });
      },
      resetForm(formName) {this.$refs[formName].resetFields();},
    },
  };
  </script>
  
  <style scoped>
  .button-row {
    text-align: center;
    margin-top: 20px;
  }
  </style>
  
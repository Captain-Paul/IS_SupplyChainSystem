<template>
    <div>
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="80px">
        <el-row>
            <el-col :span="18" :offset="4">
                <el-form-item label="货物编号" prop="g_id" required>
                  <el-select v-model="ruleForm.g_id" placeholder="请选择">
                    <el-option
                      v-for="item in gOptions"
                      :key="item"
                      :label="item"
                      :value="item"
                    ></el-option>
                  </el-select>
                </el-form-item>
                <el-form-item label="货物品牌" prop="g_brand">
                    <el-input v-model="ruleForm.g_brand"></el-input>
                </el-form-item>
                <el-form-item label="货物种类" prop="g_category">
                    <el-input v-model="ruleForm.g_category"></el-input>
                </el-form-item>
                <el-form-item label="货物名称" prop="g_name">
                    <el-input v-model="ruleForm.g_name"></el-input>
                </el-form-item>
                <el-form-item label="保质期" prop="g_life">
                    <el-input v-model="ruleForm.g_life"></el-input>
                </el-form-item>
                <el-form-item label="地址" prop="g_loc">
                    <el-input v-model="ruleForm.g_loc"></el-input>
                </el-form-item>
                <el-form-item label="供应商" prop="g_vendor">
                    <el-input v-model="ruleForm.g_vendor"></el-input>
                </el-form-item>
                <el-form-item label="储存温度" prop="g_tempreture">
                    <el-input v-model="ruleForm.g_tempreture"></el-input>
                </el-form-item>
                <el-form-item label="储存湿度" prop="g_humidity">
                    <el-input v-model="ruleForm.g_humidity"></el-input>
                </el-form-item>
            </el-col>
        </el-row>
        <el-col :span="20" :offset="2" class="button-row">
          <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
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
            g_id: '',
            g_brand: '',
            g_category: null,
            g_name: null,
            g_life: '',
            g_loc: '',
            g_vendor: '',
            g_tempreture: '',
            g_humidity: '',
          },
          nowadays:'',
          rules: {g_id: [{ required: true, message: '请选择货物编号', trigger: 'blur' },],},
          username:"",password:"",gOptions:[]
        };
      },
    created() {
      // 从路由参数中获取用户名和密码
      this.Initialize();
    },mounted(){
      this.fetchOrder();
    },
      methods: {
        Initialize(){
          this.username = localStorage.getItem("username");
          this.password = localStorage.getItem("password");
          const ba = 'Basic ' + btoa(this.username + ':' + this.password);
          axios
          .get('http://127.0.0.1:8000/fresh/goods/list', {headers:{Authorization:ba}})
          .then((response) => {
            if (response.status === 200) {this.gOptions = response.data.results.map((item) => item.g_id);
            } else {this.$message.error('获取后端数据失败');}
          }).catch((error) => {console.log(error);return false;});
        },
        fetchOrder(){
          this.username = localStorage.getItem("username");
          this.password = localStorage.getItem("password");
          const ba = 'Basic ' + btoa(this.username + ':' + this.password);
          axios
          .get('http://127.0.0.1:8000/fresh/goods/detail/?function=id&g_id='+this.ruleForm.g_id, {headers:{Authorization:ba}})
          .then((response) => {
            if (response.status === 200) {
              this.ruleForm.g_brand = response.data.g_brand;
              this.ruleForm.g_category = response.data.g_category;
              this.ruleForm.g_name = response.data.g_name;
              this.ruleForm.g_life = response.data.g_life;
              this.ruleForm.g_loc = response.data.g_loc;
              this.ruleForm.g_vendor = response.data.g_vendor;
              this.ruleForm.g_tempreture = response.data.g_tempreture;
              this.ruleForm.g_humidity = response.data.g_humidity;
            } else {this.$message.error('获取后端数据失败');}
          }).catch((error) => {console.log(error);return false;});
        },
        submitForm(formName) {
          this.$refs[formName].validate((valid) => {
            if (valid) {        
                const data = this.ruleForm;
                const basicAuth = 'Basic '+btoa(this.username+':'+this.password)
                axios
                  .put('http://127.0.0.1:8000/fresh/goods/detail/',data,{headers: {Authorization: basicAuth}})
                  .then((response) => {
                    this.$message.success('数据提交成功')
                    console.log('数据提交成功', response.data);
                  })
                  .catch((error) => {this.$message.error('数据提交失败', error);});
            } else {
              this.$message.error('添加失败，请重新检查')
              return false;
            }
          });
        },
        resetForm(formName) {
          this.$refs[formName].resetFields();
        }
      },watch:{
        'ruleForm.g_id': function(newVal) {
      if (newVal) {this.fetchOrder();}}
    }
  }
  </script>

  <style scoped>
  .button-row {
  text-align: center;
  margin-top: 20px;
  }
  </style>
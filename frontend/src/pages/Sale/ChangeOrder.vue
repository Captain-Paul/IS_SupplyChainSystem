<template>
  <div>
  <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="80px">
      <el-row>
          <el-col :span="18" :offset="4">
              <el-form-item label="订单编号" prop="order_id" required>
                <el-select v-model="ruleForm.order_id" placeholder="请选择">
                  <el-option
                    v-for="item in order_idOptions"
                    :key="item"
                    :label="item"
                    :value="item"
                  ></el-option>
                </el-select>
              </el-form-item>

              <el-form-item label="订单数量" prop="order_quantity">
                  <el-input-number v-model="ruleForm.order_quantity" :min="0" :max="9999"></el-input-number>
                  <span>单位:斤</span> 
              </el-form-item>

              <el-form-item label="实际售价" prop="order_realprice">
                  <el-input-number v-model="ruleForm.order_realprice" :min="0" :max="9999"></el-input-number>
                  <span>单位:元</span> 
              </el-form-item>
              
              <el-form-item label="客户姓名" prop="client_name">
                  <el-input v-model="ruleForm.client_name"></el-input>
              </el-form-item>
              <el-form-item label="客户电话" prop="client_tel">
                  <el-input v-model="ruleForm.client_tel"></el-input>
              </el-form-item>

              <el-form-item label="客户地址" prop="client_addr">
              <el-select v-model="ruleForm.client_addr" placeholder="请选择客户地址">
                  <el-option label="海淀" value="海淀"></el-option>
                  <el-option label="昌平" value="昌平"></el-option>
                  <el-option label="朝阳" value="朝阳"></el-option>
                  <el-option label="西城" value="西城"></el-option>
                  <el-option label="大兴" value="大兴"></el-option>
                  <el-option label="顺义" value="顺义"></el-option>
              </el-select>
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
          order_id: '',
          order_quantity: null,
          order_realprice: null,
          client_name: '',
          client_addr: '',
          client_tel: '',
        },
        nowadays:'',
        rules: {order_id: [{ required: true, message: '请选择订单id', trigger: 'blur' },],},
        username:"",password:"",order_idOptions:[]
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
        .get('http://127.0.0.1:8000/fresh/order/list', {headers:{Authorization:ba}})
        .then((response) => {
          if (response.status === 200) {this.order_idOptions = response.data.map((item) => item.order_id);
          } else {this.$message.error('获取后端数据失败');}
        }).catch((error) => {console.log(error);return false;});
      },
      fetchOrder(){
        this.username = localStorage.getItem("username");
        this.password = localStorage.getItem("password");
        console.log(this.ruleForm.order_id)
        const ba = 'Basic ' + btoa(this.username + ':' + this.password);
        axios
        .get('http://127.0.0.1:8000/fresh/order/detail/?function=id&order_id='+this.ruleForm.order_id, {headers:{Authorization:ba}})
        .then((response) => {
          if (response.status === 200) {
            this.ruleForm.order_quantity = response.data.order_quantity;
            this.ruleForm.order_realprice = response.data.order_realprice;
            this.ruleForm.client_name = response.data.client_name;
            this.ruleForm.client_addr = response.data.client_addr;
            this.ruleForm.client_tel = response.data.client_tel;
          } else {this.$message.error('获取后端数据失败');}
        }).catch((error) => {console.log(error);return false;});
      },
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
              // 构建要发送的数据对象
              const data = this.ruleForm;
              const basicAuth = 'Basic '+btoa(this.username+':'+this.password)
              // 发送POST请求到Django后端
              axios
                .put('http://127.0.0.1:8000/fresh/order/detail/',data,{headers: {Authorization: basicAuth}})
                .then((response) => {
                  // 处理成功响应
                  this.$message.success('数据提交成功')
                  console.log('数据提交成功', response.data);
                  // 在这里可以执行其他操作，例如重置表单等
                })
                .catch((error) => {
                  // 处理错误响应
                  this.$message.error('数据提交失败', error);
                  // 在这里可以根据需要处理错误，例如显示错误提示等
                });
          } else {this.$message.error('添加失败，请重新检查');return false;}
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      }
    },watch:{
      'ruleForm.order_id': function(newVal) {
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
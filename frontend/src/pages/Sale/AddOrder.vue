<template>
    <div>
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="80px">
        <el-row>
            <el-col :span="18" :offset="4">
                <!-- <el-form-item label="订单编号" prop="order_id" required>
                    <el-input v-model="ruleForm.order_id"></el-input>
                </el-form-item> -->
                <el-form-item label="交易编码" prop="transfer" required>
                  <el-select v-model="ruleForm.transfer" placeholder="请选择">
                    <el-option
                      v-for="item in transferOptions"
                      :key="item"
                      :label="item"
                      :value="item"
                    ></el-option>
                  </el-select>
                </el-form-item>

                <el-form-item label="出库编号" prop="out" required>
                  <el-select v-model="ruleForm.out" placeholder="请选择">
                    <el-option
                      v-for="item in outOptions"
                      :key="item"
                      :label="item"
                      :value="item"
                    ></el-option>
                  </el-select>
                </el-form-item>

                <el-form-item label="货物编码" prop="g" required>
                  <el-select v-model="ruleForm.g" placeholder="请选择">
                    <el-option
                      v-for="item in gOptions"
                      :key="item"
                      :label="item"
                      :value="item"
                    ></el-option>
                  </el-select>
                </el-form-item>

                <el-form-item  label="生效时间" prop="order_time">
                <el-date-picker type="date" placeholder="选择日期" v-model="ruleForm.order_time"></el-date-picker>
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
            <el-button type="primary" @click="submitForm('ruleForm')">添加</el-button>
            <el-button @click="resetForm('ruleForm')">重置</el-button>
          </el-form-item>
        </el-col>

  </el-form>
    </div>
</template>

  <script>
import axios from 'axios';
import moment from 'moment';
    export default {
      data() {
        return {
          ruleForm: {
            order_id: 'ORDER01',
            transfer: '',
            out: '',
            g: '',
            order_time: '',
            order_quantity: null,
            order_realprice: null,
            client_name: '',
            client_addr: '',
            client_tel: '',
          },
          nowadays:'',
          rules: {
            // order_id: [
            //   { required: true, message: '请输入订单id', trigger: 'blur' },
            //   { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
            // ],
            transfer: [{ required: true, message: '请输入交易编码', trigger: 'blur' },],
            out: [{ required: true, message: '请输入出库编号', trigger: 'blur' }],
            g: [{ required: true, message: '请输入货物编码', trigger: 'blur' }],
            client_addr: [{ required: true, message: '请选择目的地', trigger: 'blur' }],
          },
          username:"",password:"",transferOptions:[],outOptions:[],gOptions:[]
        };
      },
    created() {this.Initialize();},
      methods: {
        Initialize(){
          this.username = localStorage.getItem("username");
          this.password = localStorage.getItem("password");
          const ba = 'Basic ' + btoa(this.username + ':' + this.password);
          axios
          .get('http://127.0.0.1:8000/fresh/transfer/list', {headers:{Authorization:ba}})
          .then((response) => {
            if (response.status === 200) {this.transferOptions = response.data.map((item) => item.transfer_id);
            } else {this.$message.error('获取后端数据失败');}
          }).catch((error) => {console.log(error);return false;});
          axios
          .get('http://127.0.0.1:8000/fresh/outbound/list', {headers:{Authorization:ba}})
          .then((response) => {
            if (response.status === 200) {this.outOptions = response.data.results.map((item) => item.out_id);
            } else {this.$message.error('获取后端数据失败');}
          }).catch((error) => {console.log(error);return false;});
          axios
          .get('http://127.0.0.1:8000/fresh/goods/list', {headers:{Authorization:ba}})
          .then((response) => {
            if (response.status === 200) {this.gOptions = response.data.results.map((item) => item.g_id);
            } else {this.$message.error('获取后端数据失败');}
          }).catch((error) => {console.log(error);return false;});
      },
        submitForm(formName) {
          this.$refs[formName].validate((valid) => {
            if (valid) {
                // 构建要发送的数据对象
                if (this.ruleForm.order_time!=''){
                this.ruleForm.order_time=moment(this.ruleForm.order_time).format('YYYY-MM-DD')
              }else{this.ruleForm.order_time=null}
                const data = this.ruleForm;
                const basicAuth = 'Basic '+btoa(this.username+':'+this.password)
                // 发送POST请求到Django后端
                axios
                  .post('http://127.0.0.1:8000/fresh/order/list/',data,{headers: {Authorization: basicAuth}})
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
            } else {
              this.$message.error('添加失败，请重新检查')
              console.log('error submit!!');
              return false;
            }
          });
        },
        resetForm(formName) {
          this.$refs[formName].resetFields();
        }
      }
    }
  </script>

<style scoped>
.button-row {
  text-align: center;
  margin-top: 20px;
}
</style>
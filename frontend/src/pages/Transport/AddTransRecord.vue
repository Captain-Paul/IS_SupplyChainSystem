<template>
    <div>
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px">
        <el-row>
            <el-col :span="18" :offset="4">
              
                <!-- <el-form-item label="运输编码" prop="transport_id" required>
                    <el-input v-model="ruleForm.transport_id"></el-input>
                </el-form-item> -->
                <el-form-item label="订单编号" prop="order_id" required>
                  <el-select v-model="ruleForm.order_id" placeholder="请选择">
                    <el-option
                      v-for="item in orderOptions"
                      :key="item"
                      :label="item"
                      :value="item"
                    ></el-option>
                  </el-select>
                </el-form-item>

                <el-form-item label="载具编号" prop="transportation">
                  <el-select v-model="ruleForm.transportation" placeholder="请选择">
                    <el-option
                      v-for="item in trOptions"
                      :key="item"
                      :label="item"
                      :value="item"
                    ></el-option>
                  </el-select>
                </el-form-item>

                <el-form-item label="仓库编码" prop="wh">
                  <el-select v-model="ruleForm.wh" placeholder="请选择">
                    <el-option
                      v-for="item in whOptions"
                      :key="item"
                      :label="item"
                      :value="item"
                    ></el-option>
                  </el-select>
                </el-form-item>
                <el-form-item label="目的地" prop="transport_to">
                    <el-input v-model="ruleForm.transport_to"></el-input>
                </el-form-item>
                <el-form-item  label="预计送达时间" prop="transport_predicatedtime">
                <el-date-picker type="date" placeholder="预计送达时间" v-model="ruleForm.transport_predicatedtime"></el-date-picker>
                </el-form-item>
                <el-form-item  label="实际送达时间" prop="transport_realtime">
                <el-date-picker type="date" placeholder="实际送达时间" v-model="ruleForm.transport_realtime"></el-date-picker>
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
            // transport_id: '',
            order_id: '',
            transportation: '',
            wh: '',
            transport_to: '',
            transport_predicatedtime: '',
            transport_realtime: '',
          },
          nowadays:'',
          rules: {
            // transport_id: [{ required: true, message: '请输入运输编码', trigger: 'blur' },],
            order_id: [{ required: true, message: '请输入交易编码', trigger: 'blur' },],
          },orderOptions:[],whOptions:[],trOptions:[]
        };
      },created() {
      this.username = localStorage.getItem('username');
      this.password = localStorage.getItem('password');
      const ba = 'Basic ' + btoa(this.username + ':' + this.password);
        axios
        .get('http://127.0.0.1:8000/fresh/warehouse/list', {headers:{Authorization:ba}})
        .then((response) => {
            if (response.status === 200) {this.whOptions = response.data.map((item) => item.wh_id);
            } else {alert('获取后端数据失败');}
        }).catch((error) => {console.log(error);return false;});
        axios
        .get('http://127.0.0.1:8000/fresh/transportation/list', {headers:{Authorization:ba}})
        .then((response) => {
            if (response.status === 200) {this.trOptions = response.data.map((item) => item.transportation_id);
            } else {alert('获取后端数据失败');}
        }).catch((error) => {console.log(error);return false;});
        axios
        .get('http://127.0.0.1:8000/fresh/order/list', {headers:{Authorization:ba}})
        .then((response) => {
            if (response.status === 200) {this.orderOptions = response.data.map((item) => item.order_id);
            } else {alert('获取后端数据失败');}
        }).catch((error) => {console.log(error);return false;});
        },
      methods: {
        submitForm(formName) {
          this.$refs[formName].validate((valid) => {
            if (valid) {
              if (this.ruleForm.transport_predicatedtime!='' && this.ruleForm.transport_realtime!=''){
            this.ruleForm.transport_predicatedtime=moment(this.ruleForm.transport_predicatedtime).format('YYYY-MM-DD')
          this.ruleForm.transport_realtime=moment(this.ruleForm.transport_realtime).format('YYYY-MM-DD')
          }else{this.ruleForm.transport_predicatedtime=null;this.ruleForm.transport_realtime=null}
              const data = this.ruleForm;
              const basicAuth = 'Basic ' + btoa(this.username + ':' + this.password);
              console.log(data);
              axios
                .post('http://127.0.0.1:8000/fresh/transport/list/', data, { headers: { Authorization: basicAuth } })
                .then((response) => {
                  this.$message.success('数据提交成功');
                  console.log('数据提交成功', response.data);
                })
                .catch((error) => {
                  this.$message.error('数据提交失败', error);
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
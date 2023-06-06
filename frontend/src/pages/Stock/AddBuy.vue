<template>
  <div>
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="80px">
      <el-row>
        <el-col :span="18" :offset="4">

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

          <el-form-item label="仓库编码" prop="wh" required>
            <el-select v-model="ruleForm.wh" placeholder="请选择">
              <el-option
                v-for="item in whOptions"
                :key="item"
                :label="item"
                :value="item"
              ></el-option>
            </el-select>
          </el-form-item>

          <el-form-item label="批次编码" prop="buy_id" required>
            <el-input v-model="ruleForm.buy_id"></el-input>
          </el-form-item>

          <el-form-item label="采购数量" prop="buy_quantity">
            <el-input-number v-model="ruleForm.buy_quantity" :min="0" :max="9999"></el-input-number>
            <span>单位:斤</span>
          </el-form-item>
          <el-form-item label="到达日期" prop="buy_intime">
            <el-date-picker type="date" placeholder="选择日期" v-model="ruleForm.buy_intime"></el-date-picker>
          </el-form-item>
          <el-form-item label="生产日期" prop="buy_pdate">
            <el-date-picker type="date" placeholder="选择日期" v-model="ruleForm.buy_pdate"></el-date-picker>
          </el-form-item>

          <el-form-item label="采购价格" prop="buy_price">
            <el-input-number v-model="ruleForm.buy_price" :min="0" :max="9999"></el-input-number>
            <span>单位:元/斤</span>
          </el-form-item>

          <!-- <el-form-item label="是否生效" prop="buy_valid">
            <el-switch
              v-model="ruleForm.buy_valid"
              active-color="#13ce66"
              inactive-color="#ff4949"
            ></el-switch>
          </el-form-item> -->

          <el-form-item label="退货原因" prop="return_reason">
            <el-input type="textarea" :autosize="{ minRows: 5}" v-model="ruleForm.return_reason"></el-input>
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
        g:'',
        wh: '',
        buy_id: '',
        buy_quantity: 10,
        buy_intime: '',
        buy_pdate: '',
        buy_price: '',
        // buy_valid: true,
        return_reason: '',
      },
      nowadays: '',
      rules: {
        buy_id: [{ required: true, message: '请输入批次编码', trigger: 'blur' }],
        wh: [{ required: true, message: '请输入仓库编码', trigger: 'blur' }],
        g: [{ required: true, message: '请输入货物编码', trigger: 'blur' }],
      },
      username: '',password: '',gOptions: [],whOptions:[],
    };
  },
  created() {
    this.username = localStorage.getItem('username');
    this.password = localStorage.getItem('password');
    const ba = 'Basic ' + btoa(this.username + ':' + this.password);
    axios
      .get('http://127.0.0.1:8000/fresh/goods/list', {headers:{Authorization:ba}})
      .then((response) => {
        if (response.status === 200) {this.gOptions = response.data.results.map((item) => item.g_id);
        } else {alert('获取后端数据失败');}
      }).catch((error) => {console.log(error);return false;});
    axios
    .get('http://127.0.0.1:8000/fresh/warehouse/list', {headers:{Authorization:ba}})
      .then((response) => {
        if (response.status === 200) {this.whOptions = response.data.map((item) => item.wh_id);
        } else {alert('获取后端数据失败');}
      }).catch((error) => {console.log(error);return false;});
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          if (this.ruleForm.buy_intime!='' && this.ruleForm.buy_pdate!=''){
            this.ruleForm.buy_intime=moment(this.ruleForm.buy_intime).format('YYYY-MM-DD')
          this.ruleForm.buy_pdate=moment(this.ruleForm.buy_pdate).format('YYYY-MM-DD')
          }else{this.ruleForm.buy_intime=null;this.ruleForm.buy_pdate=null}
          
          const data = this.ruleForm;
          const basicAuth = 'Basic ' + btoa(this.username + ':' + this.password);
          axios
            .post('http://127.0.0.1:8000/fresh/buy/list/', data, { headers: { Authorization: basicAuth } })
            .then((response) => {
              this.$message.success('数据提交成功');
              console.log('数据提交成功', response.data);
            })
            .catch((error) => {
              this.$message.error('数据提交失败', error);
            });
        } else {
          this.$message.error('添加失败，请重新检查');
          console.log('error submit!!');
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
  },
};
</script>

<style scoped>
.button-row {
  text-align: center;
  margin-top: 20px;
}
</style>

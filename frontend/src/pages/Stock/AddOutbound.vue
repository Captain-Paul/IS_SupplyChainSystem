<template>
    <div>
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="80px">
        <el-row>
            <el-col :span="18" :offset="4">
                <el-form-item label="出库编号" prop="out_id" required>
                    <el-input v-model="ruleForm.out_id"></el-input>
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

                
                <el-form-item  label="出库时间" prop="out_time">
                <el-date-picker type="date" placeholder="选择日期" v-model="ruleForm.out_time"></el-date-picker>
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
  import axios from 'axios'
  import moment from 'moment'
    export default {
      data() {
        return {
          ruleForm: {
            out_id: '',
            wh: '',
            g: '',
            out_time: '',
          },
          nowadays:'',
          rules: {
            out_id: [{ required: true, message: '请输入出库编号', trigger: 'blur' }],
            wh: [{ required: true, message: '请输入仓库编码', trigger: 'blur' },],
            g: [{ required: true, message: '请输入货物编码', trigger: 'blur' }],
          },username:'',password:'',gOptions:[],whOptions:[]
        };
      },created() {
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
              if (this.ruleForm.out_time!=''){
                this.ruleForm.out_time=moment(this.ruleForm.out_time).format('YYYY-MM-DD')
              }else{this.ruleForm.out_time=null}

              const data = this.ruleForm;
              const basicAuth = 'Basic ' + btoa(this.username + ':' + this.password);
              console.log(data);
              axios
                .post('http://127.0.0.1:8000/fresh/outbound/list/', data, { headers: { Authorization: basicAuth } })
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
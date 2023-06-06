<template>
    <div>
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="80px">
        <el-row>
            <el-col :span="18" :offset="4">
                <el-form-item label="载具编号" prop="transportation_id" required>
                    <el-input v-model="ruleForm.transportation_id"></el-input>
                </el-form-item>

                <el-form-item label="载具类型" prop="transportation_class" required>
                  <el-select v-model="ruleForm.transportation_class" placeholder="请选择">
                    <el-option
                      v-for="item in trOptions"
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
                <el-form-item label="司机姓名" prop="driver_name" required>
                    <el-input v-model="ruleForm.driver_name"></el-input>
                </el-form-item>
                <el-form-item label="司机编号" prop="driver_id" required>
                    <el-input v-model="ruleForm.driver_id"></el-input>
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
    export default {
      data() {
        return {
          ruleForm: {
            transportation_id: '',
            transportation_class: '',
            driver_name: '',
            driver_id: '',
          },
          nowadays:'',
          rules: {
            transportation_id: [{ required: true, message: '请输入载具编号', trigger: 'blur' }],
            transportation_class: [{ required: true, message: '请选择载具类型', trigger: 'blur' },],
            driver_name: [{ required: true, message: '请输入司机姓名', trigger: 'blur' }],
          },username:'',password:'',
          trOptions:['卡车','面包车','冷链货车'],whOptions:[]
        };
      },created() {
      this.username = localStorage.getItem('username');
      this.password = localStorage.getItem('password');
      const ba = 'Basic ' + btoa(this.username + ':' + this.password);
        axios
        .get('http://127.0.0.1:8000/fresh/warehouse/list', {headers:{Authorization:ba}})
        .then((response) => {
            if (response.status === 200) {this.whOptions = response.data.map((item) => item.wh_id);
            } else {this.$message.error('获取后端数据失败');}
        }).catch((error) => {console.log(error);return false;});
        },
      methods: {
        submitForm(formName) {
          this.$refs[formName].validate((valid) => {
            if (valid) {
              const data = this.ruleForm;
              const basicAuth = 'Basic ' + btoa(this.username + ':' + this.password);
              console.log(data);
              axios
                .post('http://127.0.0.1:8000/fresh/transportation/list/', data, { headers: { Authorization: basicAuth } })
                .then((response) => {
                    this.$message.success('数据提交成功');
                  console.log('数据提交成功', response.data);
                })
                .catch((error) => {
                    this.$message.error('数据提交失败', error);
                });
            } else {
                this.$message.error('添加失败，请重新检查表单')
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
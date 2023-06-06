<template>
    <div>
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px">
        <el-row>
            <el-col :span="18" :offset="4">

                <el-form-item label="交易编码" prop="transfer_id" required>
                    <el-input v-model="ruleForm.transfer_id"></el-input>
                </el-form-item>
                
                <el-form-item label="金额" prop="transfer_amount" required>
                    <el-input-number v-model="ruleForm.transfer_amount" :min="0" :max="999999999"></el-input-number>
                    <span>单位:元</span>
                </el-form-item>
                <el-form-item label="收款账户" prop="transfer_inaccount" required>
                    <el-input v-model="ruleForm.transfer_inaccount"></el-input>
                </el-form-item>
                <el-form-item label="付款账户" prop="transfer_outaccount" required>
                    <el-input v-model="ruleForm.transfer_outaccount"></el-input>
                </el-form-item>

                <el-form-item label="业务员编号" prop="transfer_staffid" required>
                  <el-select v-model="ruleForm.transfer_staffid" placeholder="请选择">
                    <el-option
                      v-for="item in staffOptions"
                      :key="item"
                      :label="item"
                      :value="item"
                    ></el-option>
                  </el-select>
                </el-form-item>

                <el-form-item label="转账类型" prop="transfer_class">
                <el-select v-model="ruleForm.transfer_class" placeholder="请选择转账类型">
                    <el-option label="转入" value="in"></el-option>
                    <el-option label="转出" value="out"></el-option>
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
    export default {
      data() {
        return {
          ruleForm: {
            transfer_id: '',
            transfer_amount: 10000,
            transfer_inaccount: '',
            transfer_outaccount: '',
            transfer_class: '',
            transfer_staffid: '',
          },
          nowadays:'',
          rules: {
            transfer_id: [{ required: true, message: '请输入交易编码', trigger: 'blur' }],

          },staffOptions:[]
        };
      },created() {
      // 从路由参数中获取用户名和密码
      this.username = localStorage.getItem("username");
      this.password = localStorage.getItem("password");
      const ba = 'Basic ' + btoa(this.username + ':' + this.password);
      axios
      .get('http://127.0.0.1:8000/user/staff/list', {headers:{Authorization:ba}})
      .then((response) => {
        if (response.status === 200) {this.staffOptions = response.data.results.map((item) => item.s_id);
        } else {this.$message.error('获取后端数据失败');}
      }).catch((error) => {console.log(error);return false;});},
      methods: {
        submitForm(formName) {
          this.$refs[formName].validate((valid) => {
            if (valid) {
                const data = this.ruleForm;
                const basicAuth = 'Basic '+btoa(this.username+':'+this.password)
                console.log(this.username,this.password)
                // 发送POST请求到Django后端
                axios
                  .post('http://127.0.0.1:8000/fresh/transfer/list/',data,{headers: {Authorization: basicAuth}})
                  .then((response) => {this.$message.success('数据提交成功')
                    console.log('数据提交成功', response.data);})
                  .catch((error) => {this.$message.error('数据提交失败', error);});
            } else {
                alert('添加失败，请重新检查')
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
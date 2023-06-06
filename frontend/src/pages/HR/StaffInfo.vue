<template>
  <el-container style="height: 1000px; border: 1px solid #eee">
    <el-main>
      <el-table v-show="showItem" :data="stafflist" style="width: 100%">
          <el-table-column type="expand">
          <template slot-scope="props">
            <el-form label-position="left" inline class="demo-table-expand">
              <el-form-item label="职务">
                <span>{{ props.row.s_job }}</span>
              </el-form-item>
              <el-form-item label="性别">
                <el-tag>{{ props.row.s_gender }}</el-tag>
              </el-form-item>
              <el-form-item label="生日">
                <span>{{ props.row.s_birth }}</span>
              </el-form-item>
              <el-form-item label="上岗日期">
                <span>{{ props.row.s_onboard_date }}</span>
              </el-form-item>
              <el-form-item label="基本工资">
                <span>{{ props.row.s_salary }}</span>
              </el-form-item>
            </el-form>
          </template>
        </el-table-column>
        <el-table-column label="员工编号" prop="s_id"></el-table-column>
        <el-table-column label="员工姓名" prop="s_name"></el-table-column>
        <el-table-column label="邮箱" prop="s_email"></el-table-column>
        <el-table-column label="联系电话" prop="s_tel"></el-table-column>
      </el-table>
    </el-main>
  </el-container>
</template>

<script>
import axios from 'axios';
const username = 'staff0003';
const password = '123456';
const basicAuth = 'Basic ' + btoa(username + ':' + password);
export default {
  data () {
    return {
      input: '',
      showItem:false,
      stafflist: [], //这里是从后端获取的所有数据
    }
  },
  created () {
    this.showtransfer();
  },
  methods:{
    showtransfer(){
      this.showItem = true;
      axios
      .get('http://127.0.0.1:8000/user/staff/list/', {
        headers: { Authorization: basicAuth },
      })
      .then((response) => {
        if (response.status === 200) {
          console.log(response.data.results)
          this.stafflist = response.data.results;}
        else {this.$message.error('获取全部职工信息失败');}})
      .catch((error) => {
        console.log(error);
        this.$message.error('获取全部职工信息失败');
        return false;
      });
    },},
};
</script>

<style>
  .el-pagination__wrapper {
          position: absolute;
          bottom: 0;
          width: 100%;
  }

  .demo-table-expand {
    font-size: 0;
  }
  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
  }
  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
  }

</style>
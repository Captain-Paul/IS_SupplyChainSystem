<template>
    <el-container style="height: 1000px; border: 1px solid #eee">
      <el-main>
        <el-table v-show="showItem" :data="transferlist" style="width: 100%">
            <el-table-column type="expand">
            <template slot-scope="props">
              <el-form label-position="left" inline class="demo-table-expand">
                <el-form-item label="转账类型">
                  <span>{{ props.row.transfer_class }}</span>
                </el-form-item>
                <el-form-item label="业务员编号">
                  <span>{{ props.row.transfer_staffid }}</span>
                </el-form-item>
              </el-form>
            </template>
          </el-table-column>
          <el-table-column label="交易编码" prop="transfer_id"></el-table-column>
          <el-table-column label="交易金额" prop="transfer_amount"></el-table-column>
          <el-table-column label="收款账户" prop="transfer_inaccount"></el-table-column>
          <el-table-column label="付款账户" prop="transfer_outaccount"></el-table-column>
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
        transferlist: [], //这里是从后端获取的所有数据
      }
    },
    created () {
      this.showtransfer();
    },
    methods:{
      showtransfer(){
        this.showItem = true;
        axios
        .get('http://127.0.0.1:8000/fresh/transfer/list/', {
          headers: { Authorization: basicAuth },
        })
        .then((response) => {
          if (response.status === 200) {this.transferlist = response.data;}
          else {this.$message.error('获取全部转账信息失败');}})
        .catch((error) => {
          console.log(error);
          this.$message.error('获取全部转账信息失败');
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
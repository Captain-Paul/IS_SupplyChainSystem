<template>
  <el-container style="height: 2000px; border: 1px solid #eee">

    <!-- <el-header style="text-align: left ;height: 50px">
      <span style="position: relative; top: 0px;">销售订单明细</span>
    </el-header> -->
    <el-backtop target=".page-component__scroll .el-scrollbar__wrap"></el-backtop>
    <el-main>
      
      <el-input v-model="input" placeholder="请输入订单号" style="display:inline-table; width: 30%; float:left">
      </el-input>
      <el-button type="success" @click="showorderdetails">搜索订单信息</el-button>
      <!-- <el-button type="success" @click="showorders">点击查询全部订单信息</el-button> -->
      <el-table v-show="showItem" :data="orderlist" style="width: 100%">
        <el-table-column type="expand">
          <template slot-scope="props">
            <el-form label-position="left" inline class="demo-table-expand">
              <el-form-item label="订单数量">
                <span>{{ props.row.order_quantity }}</span>
              </el-form-item>
              <el-form-item label="实际售价">
                <span>{{ props.row.order_realprice }}</span>
              </el-form-item>
              <el-form-item label="客户姓名">
                <span>{{ props.row.client_name }}</span>
              </el-form-item>
              <el-form-item label="客户地址">
                <span>{{ props.row.client_addr }}</span>
              </el-form-item>
              <el-form-item label="客户电话">
                <span>{{ props.row.client_tel }}</span>
              </el-form-item>
            </el-form>
          </template>
        </el-table-column>
        <el-table-column label="订单编号" prop="order_id"></el-table-column>
        <el-table-column label="交易编码" prop="transfer"></el-table-column>
        <el-table-column label="出库编号" prop="out"></el-table-column>
        <el-table-column label="货物编码" prop="g"></el-table-column>
        <el-table-column label="生效时间" prop="order_time"></el-table-column>
      </el-table>
      <!-- <el-row>
      <el-col style="text-align:right">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="currentpage"
          :page-sizes="[10, 20, 30, 40]"
          :page-size="pagesize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="total">
        </el-pagination>
      </el-col>
    </el-row> -->
    </el-main>

</el-container>

</template>

<script>
import axios from 'axios';

// const axios = require('axios');
const username = 'staff0004';
const password = '123456';
const basicAuth = 'Basic ' + btoa(username + ':' + password);
  export default {
    data () {
      return {
        input: '',
        showItem:false,
        total:0,  //总数据条数
        currentpage:1,  //当前所在页默认是第一页
        pagesize:10,  //每页显示多少行数据 默认设置为10
        orderlist: [],  //这里是从后端获取的所有数据
        pageTicket:[],//分页后的当前页数据

      }
    },
    created () {
      // this.showorderdetails();
      this.showorders();
    },
    methods:{
      showorderdetails() {
        this.orderlist = [];
        this.showItem = true;
        axios.get('http://127.0.0.1:8000/fresh/order/detail/?function=id&order_id=' + this.input, {
          headers: { Authorization: basicAuth }
        })
        .then((response) => {
          if (response.status === 200) {
            this.orderlist = [response.data];
            console.log(response.data);
            // this.total = this.orderlist.length; 
            // this.pageTicket = this.orderlist.slice(
            //   (this.currentpage - 1) * this.pagesize,
            //   this.currentpage * this.pagesize
            // );
          } else {
            this.$message.error('查询订单失败');
            console.log('fail');
          }
        })
        .catch((error) => {
          console.log(error);
          this.$message.error('查询订单失败');
          return {
            "code": 400,
            "message": "对不起，查询订单失败"
          };
        });

      },


      showorders(){
        this.showItem = true;
        axios
        .get('http://127.0.0.1:8000/fresh/order/list/', {
          headers: { Authorization: basicAuth },
        })
        .then((response) => {
          if (response.status === 200) {
            this.orderlist = response.data;
            console.log(this.orderlist);
            // this.total = this.orderlist.length; 
            // this.pageTicket = this.orderlist.slice(
            //   (this.currentpage - 1) * this.pagesize,
            //   this.currentpage * this.pagesize
            // );
          } else {
            this.$message.error('获取全部订单信息失败');
            console.log('fail');
          }
        })
        .catch((error) => {
          console.log(error);
          this.$message.error('获取全部订单信息失败');
          return {
            "code": 400,
            "message": "对不起，获取全部订单信息失败"
          };
        });
      },

      // handleSizeChange(val) {
      //   console.log(`每页 ${val} 条`);
      //   this.pagesize = val;
      //   this.pageTicket = this.orderlist.slice(
      //     (this.currentpage - 1) * val,
      //     this.currentpage * val
      //   );
      // },

      // handleCurrentChange(val) {
      //   console.log(`当前页: ${val}`);
      //   this.currentpage = val;
      //   this.pageTicket = this.orderlist.slice(
      //     (val - 1) * this.pagesize,
      //     val * this.pagesize
      //   );
      // },

  },
};
</script>


<style>
  /* .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 1px;
  } */
  
  /* .el-aside {
    color: #333;
  } */

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
<template>
    <el-container style="height: 1000px; border: 1px solid #eee">
  
      <el-main>
        <el-input v-model="input" placeholder="请输入运输编号" style="display:inline-table; width: 30%; float:left">
        </el-input>
        <el-button type="success" @click="showtransdetails">搜索运输记录</el-button>

        <el-table v-show="showItem" :data="transrecord" style="width: 100%">
          <el-table-column label="订单编号" prop="order"></el-table-column>
          <el-table-column label="运输编号" prop="transport_id"></el-table-column>
          <el-table-column label="载具编号" prop="transportation"></el-table-column>
          <el-table-column label="目的地" prop="transport_to"></el-table-column>
          <el-table-column label="预计送达时间" prop="transport_predicatedtime"></el-table-column>
          <el-table-column label="实际送达时间" prop="transport_realtime"></el-table-column>
        </el-table>
      </el-main>
  
  </el-container>
  
</template>
  
<script>
import axios from 'axios';

// const axios = require('axios');
const username = 'staff0002';
const password = '123456';
const basicAuth = 'Basic ' + btoa(username + ':' + password);

  export default {

    data () {
      return {
        input: '',
        showItem:true,
        total:0,  //总数据条数
        currentpage:1,  //当前所在页默认是第一页
        pagesize:10,  //每页显示多少行数据 默认设置为10
        transrecord: [],  //这里是从后端获取的所有数据
        pageTicket:[],//分页后的当前页数据

      }
    },
    // 在一创建组件的时候就调用这个函数，即打开界面显示全部数据
    created () {
      // this.showorderdetails();
      this.showtransrecord();
    },
    // mounted() {
    //   this.showorders();
    // },
    methods:{
      showtransdetails() {
        this.transrecord = [];
        this.showItem = true;
        axios.get('http://127.0.0.1:8000/fresh/transport/detail/?function=id&out_id=' + this.input, {
          headers: { Authorization: basicAuth }
        })
        .then((response) => {
          if (response.status === 200) {
            this.transrecord = [response.data.results];
            console.log(this.transrecord);
          } else {
            this.$message.error('查询运输记录失败');
            console.log('fail');
          }
        })
        .catch((error) => {
          console.log(error);
          this.$message.error('查询运输记录失败');
          return {"code": 400,"message": "对不起，查询运输记录失败"};})},


      showtransrecord(){
        this.showItem = true;
        axios
        .get('http://127.0.0.1:8000/fresh/transport/list/', {
          headers: { Authorization: basicAuth },
        })
        .then((response) => {
          if (response.status === 200) {
            this.transrecord = response.data;
            console.log(response.data);
          } else {
            this.$message.error('获取全部运输记录失败');
            console.log('fail');
          }
        })
        .catch((error) => {
          console.log(error);
          this.$message.error('获取全部运输记录失败');
          return {
            "code": 400,
            "message": "对不起，获取全部运输记录失败"
          };
        });
      },

  },
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
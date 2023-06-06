<template>
    <el-container style="height: 1000px; border: 1px solid #eee">
  
      <el-main>
        <el-input v-model="input" placeholder="请输入出库编号" style="display:inline-table; width: 30%; float:left">
        </el-input>
        <el-button type="success" @click="showoutbounddetails">搜索出库记录</el-button>
        
        <el-table v-show="showItem" :data="outboundrecord" style="width: 100%">
          <el-table-column label="出库编号" prop="out_id"></el-table-column>
          <el-table-column label="货物编码" prop="g"></el-table-column>
          <el-table-column label="仓库编码" prop="wh"></el-table-column>
          <el-table-column label="出库时间" prop="out_time"></el-table-column>
        </el-table>
  
      </el-main>
  
  </el-container>
  
</template>
  
<script>
import axios from 'axios';

const username = 'staff0005';
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
        outboundrecord: [],  //这里是从后端获取的所有数据
        pageTicket:[],//分页后的当前页数据
      }
    },
    // 在一创建组件的时候就调用这个函数，即打开界面显示全部数据
    created () {
      // this.showorderdetails();
      this.showoutboundrecord();
    },
    // mounted() {
    //   this.showorders();
    // },
    methods:{
      showoutbounddetails() {
        this.outboundrecord = [];
        this.showItem = true;
        axios.get('http://127.0.0.1:8000/fresh/outbound/detail/?function=id&out_id=' + this.input, {
          headers: { Authorization: basicAuth }
        })
        .then((response) => {
          if (response.status === 200) {
            this.outboundrecord = [response.data];
            console.log(response.data);
          } else {
            this.$message.error('查询出库记录失败');
            console.log('fail');
          }
        })
        .catch((error) => {
          console.log(error);
          this.$message.error('查询出库记录失败');
          return {
            "code": 400,
            "message": "对不起，查询出库记录失败"
          };
        });
      },
      showoutboundrecord(){
        this.showItem = true;
        axios
        .get('http://127.0.0.1:8000/fresh/outbound/list/', {
          headers: { Authorization: basicAuth },
        })
        .then((response) => {
          if (response.status === 200) {
            this.outboundrecord = response.data.results;
            console.log(this.outboundrecord);
          } else {
            this.$message.error('获取全部出库记录失败');
            console.log('fail');
          }
        })
        .catch((error) => {
          console.log(error);
          this.$message.error('获取全部出库记录失败');
          return {
            "code": 400,
            "message": "对不起，获取全部出库记录失败"};});},
          
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
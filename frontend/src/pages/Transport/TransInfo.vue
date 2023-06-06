<template>
    <el-container style="height: 1000px; border: 1px solid #eee">
  
      <el-main>
        <!-- <el-row display="margin-top:10px">
        <el-input v-model="input" placeholder="请输入库存信息" style="display:inline-table; width: 30%; float:left">
        </el-input>
        <el-button type="success" @click="showtransportationinfodetails">搜索库存信息</el-button>
        </el-row> -->
        
        <el-table v-show="showItem" :data="translist" style="width: 100%">
          <el-table-column label="载具编号" prop="transportation_id"></el-table-column>
          <el-table-column label="载具类型" prop="transportation_class"></el-table-column>
          <el-table-column label="驾驶人编号" prop="driver_id"></el-table-column>
          <el-table-column label="驾驶人姓名" prop="driver_name"></el-table-column>
        </el-table>
  
        <!-- 以下是对后端返回数据进行分页 -->
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
const username = 'staff0002';
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
        translist: [],  //这里是从后端获取的所有数据
        pageTicket:[],//分页后的当前页数据

      }
    },

    // 在一创建组件的时候就调用这个函数，即打开界面显示全部数据
    created () {
      // this.showorderdetails();
      this.showtransportationinfo();
    },


    // mounted() {
    //   this.showorders();
    // },


    methods:{
    //   showtransportationinfodetails() {
    //     this.translist = [];
    //     this.showItem = true;
    //     axios.get('http://127.0.0.1:8000/fresh/count/detail/?function=id&g=' + this.input, {
    //       headers: { Authorization: basicAuth }
    //     })
    //     .then((response) => {
    //       if (response.status === 200) {
    //         this.translist = [response.data];
    //         console.log(response.data);
            
    //         // this.total = this.orderlist.length; 
    //         // this.pageTicket = this.orderlist.slice(
    //         //   (this.currentpage - 1) * this.pagesize,
    //         //   this.currentpage * this.pagesize
    //         // );
    //       } else {
    //         this.$message.error('查询货物失败');
    //         console.log('fail');
    //       }
    //     })
    //     .catch((error) => {
    //       console.log(error);
    //       this.$message.error('查询货物失败');
    //       return {
    //         "code": 400,
    //         "message": "对不起，查询货物失败"
    //       };
    //     });
    //   },


      showtransportationinfo(){
        this.showItem = true;
        axios
        .get('http://127.0.0.1:8000/fresh/transportation/list/', {
          headers: { Authorization: basicAuth },
        })
        .then((response) => {
          if (response.status === 200) {
            this.translist = response.data;
            console.log(this.translist);
            // this.total = this.orderlist.length; 
            // this.pageTicket = this.orderlist.slice(
            //   (this.currentpage - 1) * this.pagesize,
            //   this.currentpage * this.pagesize
            // );
          } else {
            this.$message.error('获取全部载具详细信息失败');
            console.log('fail');
          }
        })
        .catch((error) => {
          console.log(error);
          this.$message.error('获取全部载具详细信息失败');
          return {
            "code": 400,
            "message": "对不起，获取全部载具详细信息失败"
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
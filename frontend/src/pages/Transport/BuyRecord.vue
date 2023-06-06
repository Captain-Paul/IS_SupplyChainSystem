<template>
    <el-container style="height: 1000px; border: 1px solid #eee">
  
      <el-main>
        <el-input v-model="input" placeholder="请输入采购批次编码" style="display:inline-table; width: 30%; float:left">
        </el-input>
        <el-button type="success" @click="showbuyrecorddetails">搜索采购记录</el-button>
        
        <el-table v-show="showItem" :data="buyrecord" style="width: 100%">
          <el-table-column type="expand">
            <template slot-scope="props">
              <el-form label-position="left" inline class="demo-table-expand">
                <el-form-item label="采购价格">
                  <span>{{ props.row.buy_price }}</span>
                </el-form-item>
                <el-form-item label="采购数量">
                  <span>{{ props.row.buy_quantity }}</span>
                </el-form-item>
                <el-form-item label="退货原因">
                  <span>{{ props.row.return_reason }}</span>
                </el-form-item>
              </el-form>
            </template>
          </el-table-column>

          <el-table-column label="批次编码" prop="buy_id"></el-table-column>
          <el-table-column label="货物编码" prop="g"></el-table-column>
          <el-table-column label="仓库编码" prop="wh"></el-table-column>
          <el-table-column label="到达日期" prop="buy_intime"></el-table-column>
          <el-table-column label="生产日期" prop="buy_pdate"></el-table-column>
          <el-table-column label="是否生效" prop="buy_valid"></el-table-column>
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
        buyrecord: [],  //这里是从后端获取的所有数据
        pageTicket:[],//分页后的当前页数据

      }
    },

    // 在一创建组件的时候就调用这个函数，即打开界面显示全部数据
    created () {
      // this.showorderdetails();
      this.showbuyrecord();
    },


    // mounted() {
    //   this.showorders();
    // },


    methods:{
      showbuyrecorddetails() {
        this.buyrecord = [];
        this.showItem = true;
        axios.get('http://127.0.0.1:8000/fresh/buy/detail/?function=id&buy_id=' + this.input, {
          headers: { Authorization: basicAuth }
        })
        .then((response) => {
          if (response.status === 200) {
            this.buyrecord = [response.data];
            console.log(response.data);
            
            // this.total = this.orderlist.length; 
            // this.pageTicket = this.orderlist.slice(
            //   (this.currentpage - 1) * this.pagesize,
            //   this.currentpage * this.pagesize
            // );
          } else {
            this.$message.error('查询采购记录失败');
            console.log('fail');
          }
        })
        .catch((error) => {
          console.log(error);
          this.$message.error('查询采购记录失败');
          return {
            "code": 400,
            "message": "对不起，查询采购记录失败"
          };
        });

      },


      showbuyrecord(){
        this.showItem = true;
        axios
        .get('http://127.0.0.1:8000/fresh/buy/list/', {
          headers: { Authorization: basicAuth },
        })
        .then((response) => {
          if (response.status === 200) {
            this.buyrecord = response.data;
            console.log(this.buyrecord);
            // this.total = this.orderlist.length; 
            // this.pageTicket = this.orderlist.slice(
            //   (this.currentpage - 1) * this.pagesize,
            //   this.currentpage * this.pagesize
            // );
          } else {
            this.$message.error('获取全部采购记录失败');
            console.log('fail');
          }
        })
        .catch((error) => {
          console.log(error);
          this.$message.error('获取全部采购记录失败');
          return {
            "code": 400,
            "message": "对不起，获取全部采购记录失败"
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
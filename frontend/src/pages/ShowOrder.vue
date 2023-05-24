<template>
    <div class="box">
      <el-form>
        <div>
          <el-input v-model="input" placeholder="请输入订单ID" style="width:300px"></el-input>
          <el-button type="success" @click="showDetail">查询</el-button>
        </div>
        <el-table v-show="showItem" :data="tableData" style="width: 600px;">
          <!-- 表格的列定义 -->
          <el-table-column prop="g_id" label="订单ID" width="180"></el-table-column>
          <el-table-column prop="g_name" label="货物"></el-table-column>
        </el-table>
      </el-form>
    </div>

  </template>
   
<script>
const username = 'zsh';
const password = '123456';
const basicAuth = 'Basic ' + btoa(username + ':' + password);
export default {
    name: 'ShowOrder',
    data () {
      return {
        input: '',
        tableData: [],
        showItem:false
      }
    },
    methods:{
      showDetail () {
        this.showItem=true
        this.$http.get('http://127.0.0.1:8000/fresh/goods/list/', {
          headers: {
          Authorization: basicAuth
        }
      })
          .then((response) => {
            if (response.status === 200) {
              this.tableData=response.data['results']
              // for (let i in response.data) {
              //   this.tableData.push(response.data);
              // }
            console.log(this.tableData)

          } else {
            this.$message.error('查询书籍失败')
            console.log('fail')
            }
        })
        .catch(error =>{
          console.log(error)
        })
    },

    // addOrder () {
    //     this.axios.get('add_order/',{params:{order_id: this.input}})
    //       .then((response) => {
    //           console.log(response.data.msg);
    //           this.showDetail()
    //       })
    //       .catch(function (error) {
    //           console.log(error);
    //       });
    //   }
    }
  }
</script>
   
  <!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.box{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items:center;
}
</style>
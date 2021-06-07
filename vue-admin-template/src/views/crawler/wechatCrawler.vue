<template>
  <el-main>
    <el-input v-model="wechatname" placeholder="请输入内容" />
    <el-button type="primary" icon="el-icon-search" @click="axiosWechatCrawler">搜索</el-button>
    <el-table
      class="dataTable tb-edit"
      :data="wechatTableData.slice((currentPage-1)*pageSize,currentPage*pageSize)"
      style="width: 100%"
      highlight-current-row
      @row-click="handleCurrent"
    >
      <el-table-column label="公众号名">
        <template scope="scope">
          <el-input v-model="scope.row.name" size="small" placeholder="请输入内容" @change="handleEdit(scope.$index, scope.row)" /> <span>{{ scope.row.name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="文章名">
        <template scope="scope">
          <el-input v-model="scope.row.title" size="small" placeholder="请输入内容" @change="handleEdit(scope.$index, scope.row)" /> <span>{{ scope.row.title }}</span>
        </template>
      </el-table-column>
      <el-table-column label="发表时间">
        <template scope="scope">
          <el-input v-model="scope.row.date" size="small" placeholder="请输入内容" @change="handleEdit(scope.$index, scope.row)" /> <span>{{ scope.row.date }}</span>
        </template>
      </el-table-column>
      <el-table-column label="文章作者">
        <template scope="scope">
          <el-input v-model="scope.row.writer" size="small" placeholder="请输入内容" @change="handleEdit(scope.$index, scope.row)" /> <span>{{ scope.row.writer }}</span>
        </template>
      </el-table-column>
      <el-table-column label="文章内容">
        <template scope="scope">
          <el-input v-model="scope.row.content" size="small" placeholder="请输入内容" @change="handleEdit(scope.$index, scope.row)" /> <span>{{ scope.row.content }}</span>
        </template>
      </el-table-column>
      <el-table-column label="文章链接">
        <template scope="scope">
          <el-input v-model="scope.row.url" size="small" placeholder="请输入内容" @change="handleEdit(scope.$index, scope.row)" /> <span>{{ scope.row.url }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template scope="scope">
          <el-button type="primary" size="small" @click="handleUpdate(scope.$index, scope.row)">上传修改</el-button>
          <!--              <el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>-->
        </template>
      </el-table-column>
    </el-table>
    <el-pagination
      class="pagination"
      align="center"
      :current-page="currentPage"
      :page-sizes="[1,5,10,20]"
      :page-size="pageSize"
      layout="total, sizes, prev, pager, next, jumper"
      :total="wechatTableData.length"
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
    />
  </el-main>

</template>

<script>

import { mapGetters } from 'vuex'
import { wechatCrawler } from '@/api/wechatcrawler'
export default {
  computed: {
    ...mapGetters([
      'token'
    ])
  },
  data() {
    return {
      wechatname: '',
      wechatTableData: [],
      currentPage: 1, // 当前页码
      total: 20, // 总条数
      pageSize: 10 // 每页的数据条数
    }
  },
  methods: {
    handleCurrent(row, event, column) {
      // console.log(row, event, column)
    },
    handleEdit(index, row) {
      // console.log(index, row)
    },
    handleUpdate(index, row) {
      console.log(row)
      // var id = row.mongoid
      // var name = row.name
      // var organizationName = row.organizationName
      // var collegeName = row.collegeName
      // var title = row.title
      // var email = row.email
      // var phone = row.phone

      // updateScholar(id, name, organizationName, collegeName, title, email, phone
      // ).then(
      //   this.$message({
      //     message: '修改成功 ' + id + ' ' + name,
      //     type: 'success'
      //   }))
    },
    // 每页条数改变时触发 选择一页显示多少行
    handleSizeChange(val) {
      // console.log(`每页 ${val} 条`)
      this.currentPage = 1
      this.pageSize = val
    },
    // 当前页改变时触发 跳转其他页
    handleCurrentChange(val) {
      // console.log(`当前页: ${val}`)
      this.currentPage = val
    },
    axiosWechatCrawler() {
      wechatCrawler(this.token, this.wechatname).then(response => {
        // console.log(response['data'])

        var str = response['data']
        // console.log(typeof (str))
        this.total = str.length
        console.log(this.total)
        for (var i = 0; i < this.total; i++) {
          this.wechatTableData.push({ name: str[i]['website_name'], title: str[i]['title'], content: str[i]['content'], time: str[i]['time'], url: str[i]['url'], writer: str[i]['writer'] })
        }
      }).catch()
    }
  }
}
</script>

<style scoped>
.tb-edit .el-input {
  display: none
}
.tb-edit .current-row .el-input {
  display: block
}
.tb-edit .current-row .el-input+span {
  display: none
}
</style>

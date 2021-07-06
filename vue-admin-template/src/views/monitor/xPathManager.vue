<template>
  <el-main>
    <el-card shadow="never" style="margin-bottom: 20px">
      <el-table
        :data="managetableList"
        element-loading-text="Loading"
        border
        fit
        highlight-current-row
        @cell-dblclick="tableEdit"
      >
        <el-table-column label="类型" prop="type" sortable/>
        <el-table-column label="是否在详情页" prop="inSpec" sortable/>
        <el-table-column label="数据库存储名字" prop="saveName" sortable/>
        <el-table-column label="需要爬取" prop="needCrawl" sortable/>
        <el-table-column label="字段名称（英）" prop="EnglishName" sortable/>
        <el-table-column label="字段名称（中）" prop="ChineseName" sortable/>
        <el-table-column label="需要存储" prop="needSave" sortable/>
      </el-table>
    </el-card>

    <el-card shadow="never">
      <el-table
        :data="tableList"
        element-loading-text="Loading"
        border
        fit
        highlight-current-row
        @cell-dblclick="tableEdit1"
      >
        <el-table-column label="_id" prop="_id" sortable/>
        <el-table-column label="button_xpath" prop="button_xpath" sortable/>
        <el-table-column label="column" prop="column" sortable/>
        <el-table-column label="content_url" prop="content_url" sortable/>
        <el-table-column label="content_xpath" prop="content_xpath" sortable/>
        <el-table-column label="lang" prop="lang" sortable/>
        <el-table-column label="resource_type" prop="resource_type" sortable/>
        <el-table-column label="time_xpath" prop="time_xpath" sortable/>
        <el-table-column label="title_xpath" prop="title_xpath" sortable/>
        <el-table-column label="type" prop="type" sortable/>
        <el-table-column label="update_interval" prop="update_interval" sortable/>
        <el-table-column label="web_url" prop="web_url" sortable/>
        <el-table-column label="website_name" prop="website_name" sortable/>
        <el-table-column label="writer_xpath" prop="writer_xpath" sortable/>
        <el-table-column label="article_xpath" prop="article_xpath" sortable/>
        <el-table-column label="time1_xpath" prop="time1_xpath" sortable/>
        <el-table-column label="writer1_xpath" prop="writer1_xpath" sortable/>
        <el-table-column label="prize_name" prop="prize_name" sortable/>
        <el-table-column label="prize_type" prop="prize_type" sortable/>
        <el-table-column label="prize_people" prop="prize_people" sortable/>
        <el-table-column label="prize_org" prop="prize_org" sortable/>
        <el-table-column label="prize_level" prop="prize_level" sortable/>
        <el-table-column label="prize_rank" prop="prize_rank" sortable/>
        <el-table-column label="combine" prop="combine" sortable/>
        <el-table-column label="source_xpath" prop="source_xpath" sortable/>
        <el-table-column label="source1_xpath" prop="source1_xpath" sortable/>
        <el-table-column label="button1_xpath" prop="button1_xpath" sortable/>
      </el-table>
    </el-card>
  </el-main>
</template>

<script>
import {
  newsCrawlerMany,
  getXpathByColumn,
  getAllXpath,
  getXpathByName,
  getXpathValueNameList,
  modifyOneSpecXpath,
  getXpathManage,
  modifyXpathManage
} from '@/api/newsCrawlerAll'
import { addStrategy, getStrategyLs } from '@/api/crawlStrategy'
import { getAllCrawlerLog } from '@/api/crawlLog'

export default {
  data() {
    return {
      tableList: [
        { type: '12', frameNumber: '23' }
      ],
      managetableList: []
    }
  },
  mounted() {
    getAllXpath(this.token)
      .then(response => {
        let infos = []
        infos = response['data']
        this.tableList = infos
      })
      .catch()
    getXpathManage(this.token)
      .then(response => {
        this.managetableList = response['data']
      })
      .catch()
  },
  methods: {
    tableEdit(row, column, cell, event) {
      // console.log(row)
      if (column.label) {
        var beforeVal = event.target.textContent
        event.target.innerHTML = ''
        cell.innerHTML = `<div class="cell">
            <div class="el-input">
              <input type="text" placeholder="请输入内容" class="el-input__inner">
            </div>
        </div>`
        const cellInput = cell.children[0].children[0].children[0]
        cellInput.value = beforeVal
        // console.log(beforeVal)
        cellInput.focus() // input自动聚焦
        // 失去焦点后  将input移除
        cellInput.onblur = function() {
          const onblurCont = `<div class="cell">${cellInput.value}</div>`
          cell.innerHTML = onblurCont // 换成原有的显示内容
          // 调用axios接口
          console.log(column)
          row[column['property']] = cellInput.value
          console.log(cellInput.value)
          modifyXpathManage(this.token, row)
          console.log(row)
        }
      }
    },
    tableEdit1(row, column, cell, event) {
      if (column.label) {
        var beforeVal = event.target.textContent
        event.target.innerHTML = ''
        cell.innerHTML = `<div class="cell">
            <div class="el-input">
              <input type="text" placeholder="请输入内容" class="el-input__inner">
            </div>
        </div>`
        const cellInput = cell.children[0].children[0].children[0]
        cellInput.value = beforeVal
        cellInput.focus() // input自动聚焦
        // 失去焦点后  将input移除
        cellInput.onblur = function() {
          const onblurCont = `<div class="cell">${cellInput.value}</div>`
          cell.innerHTML = onblurCont // 换成原有的显示内容
          // 调用axios接口
          if (column['property'] !== '_id') {
            row[column['property']] = cellInput.value
          }
          modifyOneSpecXpath(this.token, row)
        }
      }
    }
  }
}
</script>

<style scoped>
.el-row {
  margin-bottom: 20px;
}

.tb-edit .el-input {
  display: none;
}

.tb-edit .current-row .el-input {
  display: block;
}

.tb-edit .current-row .el-input + span {
  display: none;
}
</style>

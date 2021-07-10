<template>
  <el-main>
    <el-card style="margin-bottom: 20px" shadow="never">
      <div slot="header" class="clearfix">
        <span>X-Path 管理</span>
      </div>
      <el-table
        :data="managetableList.slice((managetableListCurrentPage - 1) * pageSize,
            managetableListCurrentPage * pageSize)"
        element-loading-text="Loading"
        fit
        highlight-current-row
        @cell-dblclick="tableEdit"
      >
        <el-table-column label="ID" prop="id" sortable/>
        <el-table-column label="类型" prop="type" sortable/>
        <el-table-column label="是否在详情页" prop="inSpec" sortable/>
        <el-table-column label="数据库存储名字" prop="saveName" sortable/>
        <el-table-column label="需要爬取" prop="needCrawl" sortable/>
        <el-table-column label="字段名称（英）" prop="EnglishName" sortable/>
        <el-table-column label="字段名称（中）" prop="ChineseName" sortable/>
        <el-table-column label="需要存储" prop="needSave" sortable/>
      </el-table>
      <el-row type="flex" justify="center" style="margin-top: 10px; margin-bottom: 30px">
        <el-col :span="3">
          <el-button
            type="primary"
            icon="el-icon-circle-plus-outline"
            size="small"
            round
            @click="xPathManagerDialogVisible = true"
          >
            新增
          </el-button>
        </el-col>
      </el-row>

      <el-row type="flex" justify="center">
        <el-pagination
          class="pagination"
          :current-page="managetableListCurrentPage"
          :page-sizes="10"
          :page-size="pageSize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="managetableList.length"
          @current-change="handlemanagetableCurrentChange"
        />
      </el-row>
    </el-card>

    <el-dialog title="X-Path 管理" :visible.sync="xPathManagerDialogVisible">
      <el-form
        ref="xPathManagerAddForm"
        :model="xPathManagerAddForm"
        label-width="150px"
        :rules="xPathManagerAddFormRules"
      >
        <el-form-item label="id" prop="id">
          <el-input
            v-model="xPathManagerAddForm.id"
            placeholder=""
            style="width: 300px"
          />
        </el-form-item>

        <el-form-item label="类型" prop="type">
          <el-input
            v-model="xPathManagerAddForm.type"
            placeholder=""
            style="width: 300px"
          />
        </el-form-item>

        <el-form-item label="是否在详情页" prop="inSpec">
          <el-input
            v-model="xPathManagerAddForm.inSpec"
            placeholder=""
            style="width: 300px"
          />
        </el-form-item>

        <el-form-item label="数据库存储名字" prop="saveName">
          <el-input
            v-model="xPathManagerAddForm.saveName"
            placeholder=""
            style="width: 300px"
          />
        </el-form-item>

        <el-form-item label="需要爬取" prop="needCrawl">
          <el-input
            v-model="xPathManagerAddForm.needCrawl"
            placeholder=""
            style="width: 300px"
          />
        </el-form-item>

        <el-form-item label="字段名称（英）" prop="EnglishName">
          <el-input
            v-model="xPathManagerAddForm.EnglishName"
            placeholder=""
            style="width: 300px"
          />
        </el-form-item>

        <el-form-item label="字段名称（中）" prop="ChineseName">
          <el-input
            v-model="xPathManagerAddForm.ChineseName"
            placeholder=""
            style="width: 300px"
          />
        </el-form-item>

        <el-form-item label="需要存储" prop="needSave">
          <el-input
            v-model="xPathManagerAddForm.needSave"
            placeholder=""
            style="width: 300px"
          />
        </el-form-item>

        <el-form-item>
          <el-button
            type="primary"
            @click="submitForm('xPathManagerAddForm')"
          >
            保存
          </el-button>
        </el-form-item>
      </el-form>
    </el-dialog>

    <el-card style="margin-bottom: 20px" shadow="never">
      <div slot="header" class="clearfix">
        <span>X-Path 信息</span>
      </div>
      <el-form :inline="true" style="padding-bottom: 20px">
        <el-form-item>
          <el-upload
            :headers="headers"
            action="http://127.0.0.1:8000/api/mongo/addXpathByFile/"
            :limit="3"
            name="file"
            :on-success="(response, file, fileList) => this.$message({message: '上传成功', type: 'success'})"
            :on-error="(err, file, fileList) => this.$message({message: '上传成功', type: 'success'})"
            :http-request="uploadSectionFile"
          >
            <el-button size="small" type="primary">上传文档</el-button>
          </el-upload>
        </el-form-item>
        <!--        <el-form-item>-->
        <!--          <input type="file" id="img"><br>-->
        <!--          <button type="submit" @click.prevent="on_sumit">添加</button>-->
        <!--        </el-form-item>-->
        <el-form-item>
          <el-checkbox v-model="presentType0">显示类型 0</el-checkbox>
          <el-checkbox v-model="presentType1">显示类型 1</el-checkbox>
        </el-form-item>
      </el-form>
      <div>
        <el-table
          :data="tableList.filter(item => item.type === '1' ? presentType1 : presentType0).slice((tableListCurrentPage - 1) * pageSize,
            tableListCurrentPage * pageSize)"
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
          <el-table-column label="website_type" prop="website_type"/>
          <el-table-column label="resource_corre" prop="resource_corre"/>
          <el-table-column label="update_interval" prop="update_interval"/>
          <el-table-column label="resource_quality" prop="resource_quality"/>
          <el-table-column label="website_intro" prop="website_intro"/>
        </el-table>
        <el-row type="flex" justify="center" style="margin-top: 10px; margin-bottom: 30px">
          <el-col :span="3">
            <el-button
              type="primary"
              icon="el-icon-circle-plus-outline"
              size="small"
              round
              @click="xPathManagerDialogVisible = true"
            >
              新增
            </el-button>
          </el-col>
        </el-row>

        <el-row type="flex" justify="center">
          <el-pagination
            class="pagination"
            :current-page="tableListCurrentPage"
            :page-sizes="10"
            :page-size="pageSize"
            layout="total, sizes, prev, pager, next, jumper"
            :total="tableList.length"
            @current-change="handletableListCurrentChange"
          />
        </el-row>

      </div>
    </el-card>

    <el-dialog title="新增 X-Path 信息" :visible.sync="xPathInfoDialogVisible">
      <el-form
        ref="form"
        :model="xPathManagerAddForm"
        label-width="150px"
        :rules="xPathManagerAddFormRules"
      >

      </el-form>
    </el-dialog>

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
  modifyXpathManage,
  addXpathByFile
} from '@/api/newsCrawlerAll'
import { addStrategy, getStrategyLs } from '@/api/crawlStrategy'
import { getAllCrawlerLog } from '@/api/crawlLog'
import { validUsername } from '@/utils/validate'
import axios from 'axios'
import request from '@/utils/request'

export default {
  data() {
    return {
      pageSize: 10,
      managetableListCurrentPage: 1,
      tableListCurrentPage: 1,
      headers: {
        'content-type': 'multipart/form-data',
        'authenticate': this.token
      },
      presentType0: true,
      presentType1: true,

      xPathManagerDialogVisible: false,
      xPathManagerAddForm: {},
      managetableList: [
        { type: '12', inSpec: '12' }
      ],
      tableList: [
        { type: '1', frameNumber: '23' },
        { type: '0', frameNumber: '23' },
        { type: '1', frameNumber: '23' }
      ],

      xPathManagerAddFormRules: {
        id: [{ required: true, message: '请输入 ID', trigger: 'blur' }],
        type: [{ required: true, message: '请输入类型', trigger: 'blur' }],
        inSpec: [{ required: true, message: '请输入是否在详情页', trigger: 'blur' }],
        saveName: [{ required: true, message: '请输入数据库存储名称', trigger: 'blur' }],
        needCrawl: [{ required: true, message: '请输入是否需要爬取', trigger: 'blur' }],
        EnglishName: [{ required: true, message: '请输入字段名称（英）', trigger: 'blur' }],
        ChineseName: [{ required: true, message: '请输入字段名称（中）', trigger: 'blur' }],
        needSave: [{ required: true, message: '请输入是否需要存储', trigger: 'blur' }]
      },

      xPathInfoDialogVisible: false
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
          this.$message({
            message: '修改字段管理成功',
            type: 'success'
          })
          // 调用axios接口
          console.log(column)
          row[column['property']] = cellInput.value
          console.log(cellInput.value)
          modifyXpathManage(this.token, row).then(response => {
          })
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
          modifyOneSpecXpath(this.token, row).then(response => {
            this.$message({
              message: '修改具体字段成功',
              type: 'success'
            })
          })
        }
      }
    },
    on_sumit() {
      var form_data = new FormData()
      var file = document.getElementById('img').files[0]
      console.log(file)
      form_data.append('file', file)
      // form_data.append('fileName', file.name)
      request({
        url: '/mongo/addXpathByFile/',
        method: 'post',
        data: form_data,
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then(res => {
        console.log(res)
      })
    },
    uploadSectionFile(param) {
      var form_data = new FormData()
      var file = param.file
      console.log(file)
      form_data.append('file', file)
      // form_data.append('fileName', file.name)
      request({
        url: '/mongo/addXpathByFile/',
        method: 'post',
        data: form_data,
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then(res => {
        console.log(res)
      })
      this.$message({
        message: '上传数据成功',
        type: 'success'
      })
    },
    handletableListCurrentChange(val) {
      // console.log(`当前页: ${val}`)
      this.tableListCurrentPage = val
    },
    handlemanagetableCurrentChange(val) {
      this.managetableListCurrentPage = val
    },
    validateXPathManagerAddForm(props, callback) {
      if (!props.every(text => !text.isEmpty())) {
        callback('Wrong')
      }
    },

    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.managetableList.push(this.xPathManagerAddForm)
          this.xPathManagerAddForm = {}
        } else {
          return false
        }
      })
    }
  }
}
</script>

<style scoped>
.tb-edit .el-input {
  display: none;
}

.tb-edit .current-row .el-input {
  display: block;
}

.tb-edit .current-row .el-input + span {
  display: none;
}

.clearfix {
  color: cornflowerblue;
}
</style>

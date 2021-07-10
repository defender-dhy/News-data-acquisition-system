<template>
  <el-main>
    <el-row>
      <el-col>
        <el-tag>共计：{{ totalCount }}</el-tag>
        <el-tag type="success" style="margin: 5px">新增：{{ incrementCount }}</el-tag>
        <el-tag type="danger" style="margin: 5px">删除：{{ decrementCount }}</el-tag>
      </el-col>
    </el-row>

    <el-row>
      <el-card class="box-card" shadow="never">
        <el-form ref="form" :model="addEntryForm" :inline="true">
          <el-form-item>
            <el-checkbox v-model="addEntryForm.websiteNameChecked">
              <el-select
                v-model="selectForm.website_name"
                filterable
                reserve-keyword
                placeholder="网站名称"
                style="border-radius: 25%;"
              >
                <el-option
                  v-for="item in websiteList"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </el-select>
            </el-checkbox>
          </el-form-item>

          <el-form-item>
            <el-checkbox v-model="addEntryForm.websiteTypeChecked">
              <el-select
                v-model="selectForm.website_type"
                filterable
                reserve-keyword
                placeholder="网站类型"
                style="border-radius: 25%;"
              >
                <el-option
                  v-for="item in websiteTypeLs"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </el-select>
            </el-checkbox>
          </el-form-item>

          <el-form-item>
            <el-checkbox v-model="addEntryForm.countryChecked">
              <el-select
                v-model="selectForm.website_country"
                filterable
                reserve-keyword
                placeholder="国别"
                style="border-radius: 25%;"
              >
                <el-option
                  v-for="item in websiteCountryLs"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </el-select>
            </el-checkbox>
          </el-form-item>

          <el-form-item>
            <el-checkbox v-model="addEntryForm.languageChecked">
              <el-select
                v-model="selectForm.lang"
                filterable
                reserve-keyword
                placeholder="语言"
                style="border-radius: 25%;"
              >
                <el-option
                  v-for="item in langLs"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </el-select>
            </el-checkbox>
          </el-form-item>

          <el-form-item>
            <el-checkbox v-model="addEntryForm.fieldChecked">
              <el-select
                v-model="selectForm.field"
                filterable
                reserve-keyword
                placeholder="所属领域"
                style="border-radius: 25%;"
              >
                <el-option
                  v-for="item in fieldLs"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </el-select>
            </el-checkbox>
          </el-form-item>

          <el-form-item>
            <el-checkbox v-model="addEntryForm.columnNameChecked">
              <el-select
                v-model="selectForm.column"
                filterable
                reserve-keyword
                placeholder="栏目名称"
                style="border-radius: 25%;"
              >
                <el-option
                  v-for="item in columnList"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </el-select>
            </el-checkbox>
          </el-form-item>

          <el-form-item>
            <el-checkbox v-model="addEntryForm.resourceTypeChecked">
              <el-select
                v-model="selectForm.resource_type"
                filterable
                reserve-keyword
                placeholder="资源类型"
                style="border-radius: 25%;"
              >
                <el-option
                  v-for="item in resourceTypeList"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </el-select>
            </el-checkbox>
          </el-form-item>

          <el-form-item>
            <el-checkbox v-model="addEntryForm.resourceRelevanceChecked">
              <el-select
                v-model="selectForm.resource_corre"
                filterable
                reserve-keyword
                placeholder="资源相关性"
                style="border-radius: 25%;"
              >
                <el-option
                  v-for="item in resourceCorreLs"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </el-select>
            </el-checkbox>
          </el-form-item>

          <el-form-item>
            <el-checkbox v-model="addEntryForm.updateFrequencyChecked">
              <el-select
                v-model="selectForm.update_interval"
                filterable
                reserve-keyword
                placeholder="更新频率"
                style="border-radius: 25%;"
              >
                <el-option
                  v-for="item in updateIntervalLs"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </el-select>
            </el-checkbox>
          </el-form-item>

          <el-form-item>
            <el-checkbox v-model="addEntryForm.dataQualityChecked">
              <el-select
                v-model="selectForm.resource_quality"
                filterable
                reserve-keyword
                placeholder="数据质量"
                style="border-radius: 25%;"
              >
                <el-option
                  v-for="item in resourceQualityLs"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </el-select>
            </el-checkbox>
          </el-form-item>

          <el-form-item>
            <el-checkbox v-model="addEntryForm.storageTimeChecked">
              <el-select
                v-model="selectForm.storageTime"
                filterable
                reserve-keyword
                placeholder="入库时间"
                style="border-radius: 25%;"
              >
                <el-option
                  v-for="item in websiteList"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </el-select>
            </el-checkbox>
          </el-form-item>

          <el-form-item>
            <el-input
              v-model="selectForm.comment"
              placeholder="注释"
              style="width: 300px"
            />
          </el-form-item>

          <el-form-item>
            <el-button type="primary" icon="el-icon-search" @click="onClickSearch">查询</el-button>
            <el-button type="primary" icon="el-icon-delete" @click="onClickDelete">清除选择</el-button>
          </el-form-item>
        </el-form>
      </el-card>
    </el-row>

    <el-row>
      <el-col :span="4">
        <el-button type="primary" icon="el-icon-circle-plus-outline">导入数据</el-button>
      </el-col>

      <el-col :span="14">
        <el-form ref="form" :model="crawlingForm" :inline="true">
          <el-form-item>
            <el-link
              icon="el-icon-edit"
              type="primary"
              @click="strategySettingDialogVisible = true"
            >
              新增策略
            </el-link>
          </el-form-item>

          <el-form-item>
            <el-select v-model="strategySettingForm.name" placeholder="请选择策略名字" size="mini">
              <el-option
                v-for="item in strategyNameLs"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
            <el-select v-model="strategySettingForm.beginDate" placeholder="请选择" size="mini">
              <el-option
                v-for="item in strategyBeginDateLs"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </el-form-item>

          <el-form-item>
            <el-radio-group v-model="crawlingForm.crawlingRadio" size="mini">
              <el-radio-button label="自动模式"/>
              <el-radio-button label="手动模式"/>
            </el-radio-group>
          </el-form-item>

          <el-form-item>
            <el-button type="primary" size="mini" @click="onCrawler">爬取</el-button>
          </el-form-item>
        </el-form>
      </el-col>

      <el-col :span="6">
        <el-input
          v-model="crawlingForm.searchText"
          placeholder="查询"
          prefix-icon="el-icon-search"
        />
      </el-col>
    </el-row>

    <el-card shadow="never">
      <div slot="header" class="clearfix">
        <span>监测源信息 </span>
        <!--            <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>-->
        <br></br>
        <el-checkbox v-model="selectAllData"></el-checkbox>
        <span> 全选</span>
      </div>
      <el-table
        class="dataTable tb-edit"
        :data="
          newsTableData.slice(
            (newsTableDataCurrentPage - 1) * pageSize,
            newsTableDataCurrentPage * pageSize
          )
        "
        highlight-current-row
        stripe="true"
        fit="true"
      >
        <el-table-column type="selection" width="35"/>

        <el-table-column label="序号" prop="_id" sortable/>

        <el-table-column v-if="addEntryForm.websiteNameChecked" label="网站名称" prop="website_name" sortable/>

        <el-table-column v-if="addEntryForm.websiteTypeChecked" label="网站类型" prop="type"/>

        <el-table-column v-if="addEntryForm.countryChecked" label="国别" prop="lang"/>

        <el-table-column v-if="addEntryForm.languageChecked" label="语言" prop="lang"/>

        <el-table-column v-if="addEntryForm.fieldChecked" label="所属领域" prop="resource_type"/>

        <el-table-column v-if="addEntryForm.columnNameChecked" label="栏目名称" prop="column"/>

        <el-table-column v-if="addEntryForm.websiteTypeChecked" label="网站类型" prop="website_type"/>

        <el-table-column v-if="addEntryForm.resourceTypeChecked" label="资源类型" prop="resource_type"/>

        <el-table-column v-if="addEntryForm.resourceRelevanceChecked" label="资源相关性" prop="resource_corre"/>

        <el-table-column v-if="addEntryForm.updateFrequencyChecked" label="更新频率" prop="update_interval"/>

        <el-table-column v-if="addEntryForm.dataQualityChecked" label="数据源质量" prop="resource_quality"/>

        <el-table-column label="网站简介" prop="website_intro"/>

        <el-table-column v-if="addEntryForm.commentChecked" label="备注" prop="others"/>

        <el-table-column label="详情"/>
      </el-table>

      <el-row type="flex" justify="center">
        <el-pagination
          class="pagination"
          :current-page="newsTableDataCurrentPage"
          :page-sizes="10"
          :page-size="pageSize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="newsTableData.length"
          @current-change="handlenewsTableCurrentChange"
        />
      </el-row>
    </el-card>

    <el-row style="margin-top: 20px">
      <el-col :span="12" style="padding-right: 5px">
        <el-card shadow="never">
          <div slot="header" class="clearfix">
            <span>爬取策略</span>
            <!--            <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>-->
          </div>
          <el-table
            class="dataTable tb-edit"
            :data="
              strategyTableData.slice(
                (strategyTableDataCurrentPage - 1) * pageSize,
                strategyTableDataCurrentPage * pageSize
              )
            "
            highlight-current-row
            stripe="true"
            fit="true"
            @row-dblclick="showStrategySettingDetail"
          >
            <el-table-column label="策略名称" prop="name" sortable/>

            <el-table-column label="爬取范围" prop="column"/>

            <el-table-column label="启动频率" prop="freq"/>

            <el-table-column label="启动日期" prop="beginDate"/>

            <el-table-column label="启动时间" prop="beginTime"/>

            <el-table-column label="停止时间" prop="endTime"/>
          </el-table>

          <el-row type="flex" justify="center">
            <el-pagination
              class="pagination"
              :current-page="strategyTableDataCurrentPage"
              :page-sizes="10"
              :page-size="pageSize"
              layout="total, sizes, prev, pager, next, jumper"
              :total="strategyTableData.length"
              @current-change="handlestrategyTableCurrentChange"
            />
          </el-row>
        </el-card>
      </el-col>

      <el-col :span="12" style="padding-left: 5px">
        <el-card shadow="never">
          <div slot="header" class="clearfix">
            <span>爬取日志</span>
            <!--            <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>-->
          </div>
          <el-table
            class="dataTable tb-edit"
            :data="
              crawlerLogTableData.slice(
                (crawlerLogTableDataCurrentPage - 1) * pageSize,
                crawlerLogTableDataCurrentPage * pageSize
              )
            "
            highlight-current-row
            stripe="true"
            fit="true"
            @row-dblclick="showCrawlerLogTableData"
          >
            <el-table-column label="日期" prop="beginDate" sortable/>

            <el-table-column label="开始时间" prop="beginTime"/>

            <el-table-column label="结束时间" prop="endTime"/>

            <el-table-column label="模式" prop="mode"/>

            <el-table-column label="爬取数量" prop="num"/>

            <el-table-column label="策略名称" prop="strategyName"/>

            <!--            <el-table-column label="数据量"/>-->

            <!--            <el-table-column label="数据量"/>-->

            <el-table-column label="详情" prop="detail"/>
          </el-table>

          <el-row type="flex" justify="center">
            <el-pagination
              class="pagination"
              :current-page="crawlerLogTableDataCurrentPage"
              :page-sizes="10"
              :page-size="pageSize"
              layout="total, sizes, prev, pager, next, jumper"
              :total="crawlerLogTableData.length"
              @current-change="handlecrawlerLogTableCurrentChange"
            />
          </el-row>
        </el-card>
      </el-col>
    </el-row>

    <el-dialog title="设置策略" :visible.sync="strategySettingDialogVisible">
      <el-form ref="form" :model="strategySettingForm" label-width="80px">
        <el-form-item label="策略名称">
          <el-input v-model="strategySettingForm.name" placeholder="请输入名称"/>
        </el-form-item>

        <el-form-item label="爬取范围">
          <el-select
            v-model="strategySettingForm.column"
            placeholder="请选择爬取栏目"
          >
            <el-option
              v-for="item in columnList"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </el-form-item>

        <el-form-item label="启动频率">
          <el-radio-group v-model="strategySettingForm.freqType">
            <el-radio label="一次"/>
            <el-radio label="每天"/>
            <el-radio label="每周"/>
            <el-radio label="自定义"/>
          </el-radio-group>
          <el-input
            v-if="strategySettingForm.freqType === '自定义'"
            v-model="strategySettingForm.freq"
          >
            <template slot="append">/ 小时</template>
          </el-input>
        </el-form-item>

        <el-form-item label="启动日期">
          <el-radio-group v-model="strategySettingForm.beginDateType">
            <el-radio label="今天"/>
            <el-radio label="自定义"/>
            <el-date-picker
              v-if="strategySettingForm.beginDateType === '自定义'"
              v-model="strategySettingForm.beginDate"
              type="date"
              placeholder="选择日期"
            />
          </el-radio-group>
        </el-form-item>

        <el-form-item label="启动时间">
          <el-radio-group v-model="strategySettingForm.beginTimeType">
            <el-radio label="现在"/>
            <el-radio label="自定义"/>
            <el-time-picker
              v-if="strategySettingForm.beginTimeType === '自定义'"
              v-model="strategySettingForm.beginTime"
              placeholder="自定义启动时间"
              format="HH:mm"
              value-format="HH:mm"
            />
          </el-radio-group>
        </el-form-item>

        <el-form-item label="停止时间">
          <el-radio-group v-model="strategySettingForm.endTimeType">
            <el-radio label="采集完成"/>
            <el-radio label="自定义"/>
            <el-time-picker
              v-if="strategySettingForm.endTimeType === '自定义'"
              v-model="strategySettingForm.endTime"
              placeholder="自定义停止时间"
              format="HH:mm"
              value-format="HH:mm"
            />
          </el-radio-group>
        </el-form-item>

        <el-form-item>
          <el-button type="primary" @click="onSaveStrategy">保存当前策略</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>

    <el-dialog
      title="监测源详情"
      :visible.sync="monitorSourceDetailDialogVisible"
    >
      <el-form ref="form" :model="monitorSourceDetailForm" label-width="80px">
        <el-form-item label="网站名称">
          <span v-if="!monitorSourceDetailForm.modifyMode">{{ monitorSourceDetailForm.websiteName }}</span>
          <el-input
            v-else
            v-model="monitorSourceDetailForm.websiteName"
            placeholder="网站名称"
            style="width: 300px"
          />
        </el-form-item>
        <el-form-item label="网址">
          <span v-if="!monitorSourceDetailForm.modifyMode">{{ monitorSourceDetailForm.websiteUrl }}</span>
          <el-input
            v-else
            v-model="monitorSourceDetailForm.websiteUrl"
            placeholder="网址"
            style="width: 300px"
          />
        </el-form-item>
        <el-form-item label="简介">
          <span v-if="!monitorSourceDetailForm.modifyMode">{{ monitorSourceDetailForm.description }}</span>
          <el-input
            v-else
            v-model="monitorSourceDetailForm.description"
            placeholder="简介"
            style="width: 300px"
          />
        </el-form-item>
        <el-form-item label="国别">
          <span v-if="!monitorSourceDetailForm.modifyMode">{{ monitorSourceDetailForm.country }}</span>
          <el-input
            v-else
            v-model="monitorSourceDetailForm.country"
            placeholder="国别"
            style="width: 300px"
          />
        </el-form-item>
        <el-form-item label="语言">
          <span v-if="!monitorSourceDetailForm.modifyMode">{{ monitorSourceDetailForm.language }}</span>
          <el-input
            v-else
            v-model="monitorSourceDetailForm.language"
            placeholder="语言"
            style="width: 300px"
          />
        </el-form-item>
        <el-form-item label="所属领域">
          <span v-if="!monitorSourceDetailForm.modifyMode">{{ monitorSourceDetailForm.scope }}</span>
          <el-input
            v-else
            v-model="monitorSourceDetailForm.scope"
            placeholder="所属领域"
            style="width: 300px"
          />
        </el-form-item>
        <el-form-item label="入库时间">
          <span v-if="!monitorSourceDetailForm.modifyMode">{{ monitorSourceDetailForm.addTime }}</span>
          <el-input
            v-else
            v-model="monitorSourceDetailForm.addTime"
            placeholder="入库时间"
            style="width: 300px"
          />
        </el-form-item>
        <el-form-item>
          <el-button
            type="primary"
            @click="monitorSourceDetailForm.modifyMode = !monitorSourceDetailForm.modifyMode"
          >
            {{ monitorSourceDetailForm.modifyMode ? '保存' : '修改信息' }}
          </el-button>
        </el-form-item>
      </el-form>

      <el-table
        class="dataTable tb-edit"
        :data="
          monitorSourceDetailData.slice(
            (monitorSourceDetailDataCurrentPage - 1) * pageSize,
            monitorSourceDetailDataCurrentPage * pageSize
          )
        "
        highlight-current-row
        stripe="true"
        fit="true"
      >
        <el-table-column type="selection" width="35"/>
        <el-table-column label="栏目序号" sortable/>
        <el-table-column label="栏目名称" sortable/>
        <el-table-column label="资源类型"/>
        <el-table-column label="资源相关性"/>
        <el-table-column label="更新频率"/>
        <el-table-column label="质量"/>
        <el-table-column label="备注"/>
      </el-table>

      <el-row type="flex" justify="center">
        <el-pagination
          class="pagination"
          :current-page="monitorSourceDetailDataCurrentPage"
          :page-sizes="10"
          :page-size="pageSize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="monitorSourceDetailData.length"
          @current-change="handlemonitorSourceDetailCurrentChange"
        />
      </el-row>
    </el-dialog>

    <el-dialog title="爬取日志详情" :visible.sync="crawlLogDetailDialogVisible">
      <el-form ref="form" :model="crawlLogDetailForm" label-width="80px">
        <el-form-item label="日期">
          <span>
            {{ crawlLogDetailForm.beginDate }}
          </span>
        </el-form-item>
        <el-form-item label="开始时间">
          <span>
            {{ crawlLogDetailForm.beginTime }}
          </span>
        </el-form-item>
        <el-form-item label="结束时间">
          <span>
            {{ crawlLogDetailForm.endDate }}
          </span>
        </el-form-item>
        <el-form-item label="模式">
          <span>
            {{ crawlLogDetailForm.mode }}
          </span>
        </el-form-item>
        <el-form-item label="数据">
          <el-button type="primary">一键下载</el-button>
          <el-button type="primary">数据预览</el-button>
        </el-form-item>
      </el-form>

      <el-table
        class="dataTable tb-edit"
        :data="
          crawlLogDetailTableData.slice(
            (crawlLogDetailTableDataCurrentPage - 1) * pageSize,
            crawlLogDetailTableDataCurrentPage * pageSize
          )
        "
        highlight-current-row
        stripe="true"
        fit="true"
      >
        <el-table-column label="序号" prop="index" sortable/>
        <el-table-column label="网站名称" prop="websiteName" sortable/>
        <el-table-column label="栏目名称" prop="columnName"/>
        <el-table-column label="数据量" prop="num"/>
        <el-table-column label="状态" prop="status"/>
        <el-table-column label="备注" prop="detail"/>
      </el-table>

      <el-row type="flex" justify="center">
        <el-pagination
          class="pagination"
          :current-page="crawlLogDetailTableDataCurrentPage"
          :page-sizes="10"
          :page-size="pageSize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="crawlLogDetailTableData.length"
          @current-change="handlecrawlLogDetailTableCurrentChange"
        />
      </el-row>
    </el-dialog>
  </el-main>
</template>

<script>
import {
  newsCrawlerMany,
  getXpathByColumn,
  getAllXpath,
  getManyXpath,
  getXpathByName,
  getXpathValueNameList,
  getAllXpathValueNameList
} from '@/api/newsCrawlerAll'
import { addStrategy, getStrategyLs } from '@/api/crawlStrategy'
import { getAllCrawlerLog, getAllSpecCrawlerLog } from '@/api/crawlLog'

export default {
  data() {
    return {
      selectAllData: false,
      name: '',
      newsTableData: [],
      strategyTableData: [{ name: '12' }, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}],
      crawlerLogTableData: [{ mode: 1 }, {}],
      pageSize: 10, // 每页的数据条数
      websiteValue: '', // 选中
      websiteList: [], // select框数据
      columnValue: '', // 选中
      columnList: [],
      websites: [],
      columns: [],
      resourceTypeValue: '',
      resourceTypes: [],
      resourceTypeList: [],
      websiteTypeLs: [],
      websiteCountryLs: [],
      fieldLs: [],
      langLs: [],
      resourceCorreLs: [],
      updateIntervalLs: [],
      resourceQualityLs: [],
      strategyNameLs: [],
      strategyBeginDateLs: [],

      totalCount: 0,
      incrementCount: 0,
      decrementCount: 0,

      newsTableDataCurrentPage: 1,
      strategyTableDataCurrentPage: 1,
      crawlerLogTableDataCurrentPage: 1,
      crawlLogDetailTableDataCurrentPage: 1,
      monitorSourceDetailDataCurrentPage: 1,

      selectForm: {
        website_name: '',
        website_type: '',
        website_country: '',
        lang: '',
        field: '',
        column: '',
        resource_type: '',
        resource_corre: '',
        update_interval: '',
        resource_quality: '',
        storageTime: '',
        comment: ''
      },

      addEntryForm: {
        websiteNameChecked: true,
        websiteTypeChecked: true,
        countryChecked: true,
        languageChecked: true,
        fieldChecked: true,
        columnNameChecked: true,
        resourceTypeChecked: true,
        resourceRelevanceChecked: true,
        updateFrequencyChecked: true,
        dataQualityChecked: true,
        storageTimeChecked: true,
        commentChecked: true
      },

      crawlingForm: {
        crawlingRadio: '自动模式',
        searchText: ''
      },
      crawlLogDetailTableData: [],

      strategySettingDialogVisible: false,
      strategySettingForm: {
        name: '',
        freqType: '一次',
        beginDateType: '今天',
        beginTimeType: '现在',
        endTimeType: '采集完成',
        freq: '12',
        beginDate: '',
        beginTime: '20:27',
        endTime: '20:30',
        column: '',
        urlList: [],
        selectForm: {}
      },

      monitorSourceDetailDialogVisible: false,
      monitorSourceDetailForm: {
        modifyMode: false,
        websiteName: '名字',
        websiteUrl: '网址',
        description: '简介',
        country: '国别',
        language: '语言',
        scope: '所属领域',
        addTime: '入库时间'
      },

      crawlLogDetailDialogVisible: false,
      monitorSourceDetailData: [],

      crawlLogDetailForm: {}
    }
  },
  watch: {
    // columnValue(newValue, oldValue) {
    //   getXpathByColumn(this.token, newValue)
    //     .then(response => {
    //       this.newsTableData = response['data']
    //     })
    //     .catch()
    // },
    // selectForm(newValue, oidValue) {
    //   getManyXpath(this.token, newValue).then(response => {
    //     this.newsTableData = response['data']
    //   })
    // }
  },
  mounted() {
    // getXpathValueNameList(this.token, 'column')
    //   .then(response => {
    //     this.columns = response['data']
    //     this.columnList = this.columns.map(item => {
    //       return { value: `${item}`, label: `${item}` }
    //     })
    //   })
    //   .catch()
    // getXpathValueNameList(this.token, 'resource_type')
    //   .then(response => {
    //     this.resourceTypes = response['data']
    //     this.resourceTypeList = this.resourceTypes.map(item => {
    //       return { value: `${item}`, label: `${item}` }
    //     })
    //   })
    //   .catch()
    getAllXpathValueNameList(this.token).then(response => {
      this.columnList = response['data']['column'].map(item => {
        return { value: `${item}`, label: `${item}` }
      })
      this.resourceTypeList = response['data']['resource_type'].map(item => {
        return { value: `${item}`, label: `${item}` }
      })
      this.websiteTypeLs = response['data']['website_type'].map(item => {
        return { value: `${item}`, label: `${item}` }
      })
      this.websiteCountryLs = response['data']['website_country'].map(item => {
        return { value: `${item}`, label: `${item}` }
      })
      this.langLs = response['data']['lang'].map(item => {
        return { value: `${item}`, label: `${item}` }
      })
      this.fieldLs = response['data']['field'].map(item => {
        return { value: `${item}`, label: `${item}` }
      })
      this.resourceCorreLs = response['data']['resource_corre'].map(item => {
        return { value: `${item}`, label: `${item}` }
      })
      this.updateIntervalLs = response['data']['update_interval'].map(item => {
        return { value: `${item}`, label: `${item}` }
      })
      this.resourceQualityLs = response['data']['resource_quality'].map(item => {
        return { value: `${item}`, label: `${item}` }
      })
    }).catch()
    getStrategyLs(this.token, 'name')
      .then(response => {
        let names = []
        names = response['data']
        this.strategyNameLs = names.map(item => {
          return { value: `${item}`, label: `${item}` }
        })
      })
      .catch()
    getStrategyLs(this.token, 'beginDate')
      .then(response => {
        let dates = []
        dates = response['data']
        this.strategyBeginDateLs = dates.map(item => {
          return { value: `${item}`, label: `${item}` }
        })
      })
      .catch()
    getAllCrawlerLog(this.token, '')
      .then(response => {
        let infos = []
        infos = response['data']
        this.crawlerLogTableData = infos
      })
      .catch()
    getStrategyLs(this.token, 'all')
      .then(response => {
        let infos = []
        infos = response['data']
        this.strategyTableData = infos
      })
      .catch()
    getAllXpath(this.token)
      .then(response => {
        let infos = []
        infos = response['data']
        this.newsTableData = infos
      })
      .catch()
  },
  methods: {
    onSaveStrategy() {
      this.strategySettingForm.selectForm = this.selectForm
      addStrategy(this.token, this.strategySettingForm)
      this.$message({
        message: '保存策略成功',
        type: 'success',
        duration: 2000
      })
    },

    onClickSearch() {
      getManyXpath(this.token, this.selectForm).then(response => {
        this.newsTableData = response['data']
      })
      this.$message({
        message: '查询成功',
        type: 'success'
      })
    },

    onClickDelete() {
      this.selectForm = {
        website_name: '',
        website_type: '',
        website_country: '',
        lang: '',
        field: '',
        column: '',
        resource_type: '',
        resource_corre: '',
        update_interval: '',
        resource_quality: '',
        storageTime: '',
        comment: ''
      }
      this.$message({
        message: '清除选择成功',
        type: 'success'
      })
    },

    onChooseStrategy() {
      return null
    },

    onCrawler() {
      newsCrawlerMany(
        this.token,
        this.strategySettingForm.name,
        this.strategySettingForm.beginDate
      )
      this.$message({
        message: '爬取结束',
        type: 'success'
      })
    },

    showStrategySettingDetail(row, column, event) {
      this.strategySettingDialogVisible = true
      this.strategySettingForm = row
    },

    showCrawlerLogTableData(row, column, event) {
      this.crawlLogDetailDialogVisible = true
      this.crawlLogDetailForm = row
      getAllSpecCrawlerLog(this.token, row).then(response => {
        this.crawlLogDetailTableData = response['data'].map(item => {
          return { value: `${item}`, label: `${item}` }
        })
      }).catch()
      console.log(row)
    },
    // handleSizeChange(val) {
    //   // console.log(`每页 ${val} 条`)
    //   this.currentPage = 1
    //   this.pageSize = val
    // },
    // 当前页改变时触发 跳转其他页
    handlenewsTableCurrentChange(val) {
      // console.log(`当前页: ${val}`)
      this.newsTableDataCurrentPage = val
    },
    handlestrategyTableCurrentChange(val) {
      // console.log(`当前页: ${val}`)
      this.strategyTableDataCurrentPage = val
    },
    handlecrawlerLogTableCurrentChange(val) {
      // console.log(`当前页: ${val}`)
      this.crawlerLogTableDataCurrentPage = val
    },
    handlecrawlLogDetailTableCurrentChange(val) {
      // console.log(`当前页: ${val}`)
      this.crawlLogDetailTableDataCurrentPage = val
    },
    handlemonitorSourceDetailCurrentChange(val) {
      // console.log(`当前页: ${val}`)
      this.monitorSourceDetailDataCurrentPage = val
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

.clearfix {
  color: cornflowerblue;
}
</style>

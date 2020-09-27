    <template>
    <div>
      <el-table
        :data="tableData"       
        :cell-style="cellStyle"
        :header-cell-style="headCellStyle"
        width="100%"
        row-key="name"
        border      
        :tree-props="{children: 'city', hasChildren: 'hasChildren'}">
        <el-table-column
          prop="name"
          label="States"
          sortable
         >
        </el-table-column>
        <el-table-column
          prop="confirm"
          label="Total Cases"
          sortable
         >
        </el-table-column>
        <el-table-column
          prop="death"
          label="Total Deaths"
          sortable
           
          >
        </el-table-column>
      </el-table>
    </div>
    </template>
    <script>
    import todaydata from '../assets/today.json'
    export default {
        data() {
          return {
            tableData: []
          }
        },
        methods:{
             cellStyle({ row, column, rowIndex, columnIndex }) {
                if (columnIndex === 0 || 1 || 2) {
                return 'font-family: "Times New Roman", Times, serif;';
                } else {
                 return ''
                }
              },
              headCellStyle({ row, column, rowIndex, columnIndex }) {
                if (rowIndex === 0) {
                   return 'font-family: "Times New Roman", Times, serif;';
                }
                else {
                   return ''
                }
            },
        },
        mounted(){
        this.tableData = todaydata.children
        }
    }
    </script>
    <style scoped>
    h2{
      background-color:darkturquoise;
    }
    </style>>
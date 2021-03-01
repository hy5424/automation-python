import pandas as pd

from util.OsUtil import OsUtil
from util.excelUtil import ExcelUtil


class ZhongHuaUtil(object):
    """
    中华工单记录合并方法
    """

    @staticmethod
    def zhonghua_excel(inputDirUrl, outDirUrl):
        inputDirUrl = inputDirUrl.replace('\\', '//')
        outDirUrl = outDirUrl.replace('\\', '//')
        files = OsUtil.walkFile(inputDirUrl)
        list = []
        for f in files:
            excelData = ExcelUtil.open_excel(f, 'Sheet1')
            excelData.drop(excelData[pd.isna(excelData['处理类型'])].index, inplace=True)
            list.append(excelData)
        df = pd.concat(list)
        df.to_excel(outDirUrl + '\\output.xlsx', index=False, header=True)


    """
    中华修改类型为其它的，将自己记录的操作类型替换工单里面的所属原因
    """
    @staticmethod
    def zhonghua_change_type(inputDirUrl, inputDirUrl2, outDirUrl):
        # 自己的excel
        inputDirUrl = inputDirUrl.replace('\\', '//')
        # itsm提供的excel
        inputDirUrl2 = inputDirUrl2.replace('\\', '//')
        # 导出地址
        outDirUrl = outDirUrl.replace('\\', '//')
        df1 = ExcelUtil.open_excel(inputDirUrl, 'Sheet1')
        df2 = ExcelUtil.open_excel(inputDirUrl2, 'Sheet1')
        df2 = df2[df2['系统'] == '新车险理赔系统']
        for idx, row in df1.iterrows():
            itsmId = row['工单号']
            for idx2, row2 in df2.iterrows():
                itsmId2 = row2['ID']
                if itsmId == itsmId2:
                    row2['所属原因'] = row['处理类型']
                    break
        df2.to_excel(outDirUrl + '\\output.xlsx', index=False, header=True)

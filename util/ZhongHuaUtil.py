import pandas as pd

from util.OsUtil import OsUtil
from util.excelUtil import ExcelUtil


class ZhongHuaUtil(object):
    """
    中华工单记录合并方法
    """

    @staticmethod
    def zhonghua_excel(inputDirUrl, outDirUrl):
        files = OsUtil.walkFile(inputDirUrl)
        list = []
        for f in files:
            f = f.replace('\\', '//')
            excelData = ExcelUtil.open_excel(f, 'Sheet1')
            excelData.drop(excelData[pd.isna(excelData['处理类型'])].index, inplace=True)
            list.append(excelData)
        df = pd.concat(list)
        df.to_excel(outDirUrl + 'output.xlsx', index=False, header=True)

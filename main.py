import numpy as np
import pandas as pd

from util.excelUtil import ExcelUtil
from util.OsUtil import OsUtil
from util.ZhongHuaUtil import ZhongHuaUtil

if __name__ == '__main__':
    # ZhongHuaUtil.zhonghua_excel('C:\\Users\\llllll\\Desktop\\itsm2', 'C:\\Users\\llllll\\Desktop\\itsm2')
    df1 = ExcelUtil.open_excel('C:\\Users\\llllll\\Desktop\\itsm3\\itsm2output.xlsx', 'Sheet1')
    df2 = ExcelUtil.open_excel('C:\\Users\\llllll\\Desktop\\itsm3\\1-2月运维工单.xlsx', 'Sheet1')
    df2 = df2[df2['系统'] == '新车险理赔系统']
    for idx, row in df1.iterrows():
        case_id = row['工单号']
        for idx2, row2 in df2.iterrows():
            case_id2 = row2['ID']
            if case_id == case_id2:
                row2['所属原因'] = row['处理类型']
                break
    df2.to_excel('C:\\Users\\llllll\\Desktop\\itsm3\\output.xlsx', index=False, header=True)

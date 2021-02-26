import numpy as np
import pandas as pd

from util.excelUtil import ExcelUtil
from util.OsUtil import OsUtil

if __name__ == '__main__':
    files = OsUtil.walkFile('C://Users//llllll//Desktop//itsm2')
    list = []
    for f in files:
        f = f.replace('\\', '//')
        excelData = ExcelUtil.open_excel(f, 'Sheet1')
        excelData.drop(excelData[pd.isna(excelData['处理类型'])].index, inplace=True)
        list.append(excelData)
    df = pd.concat(list)
    df.to_excel('C://Users//llllll//Desktop//itsm2//6.xlsx', index=False, header=True)

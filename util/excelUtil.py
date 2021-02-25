#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd


class ExcelUtil(object):

    @staticmethod
    def open_excel(excelUrl, sheetName):
        df = pd.read_excel(excelUrl, sheet_name=sheetName)
        return df

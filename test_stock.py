#coding: utf-8
import numpy as np 
import pandas as pd  
import talib
import os
import csv
import test
class haigui(object):


    def return_name(self,code):
        namelistfile = r'C:\Users\Administrator\Downloads\namelist.txt'
        code_list, name_list = [], []
        with open(namelistfile,'r',encoding='utf-8') as myfile:
            for line in myfile.readlines():
                if line != '\n':
                    code_list.append(line.split(',')[0])
                    name_list.append(line.split(',')[1][:-1])

        # code_list = pd.read_csv(namelistfile,index_col=0)
        # name_list = pd.read_csv(namelistfile,index_col=1)
        # print(code_list, name_list)
        dict1 = {}
        dict1 = dict(zip(code_list,name_list))
        # print(dict1)
        return dict1[code]
    def __init__(self,csvfile):
        self.code = os.path.basename(csvfile)[:6]
        # self.code = '300554'
        self.df = pd.read_csv(csvfile)
        self.close = np.array(self.df['收盘'][::-1])
        self.transit_date = np.array(self.df['日期'][::-1])
        self.high = np.array(self.df['高'][::-1])
        self.low = np.array(self.df['低'][::-1])
        self.atr_20 = talib.ATR(self.high,self.low,self.close,timeperiod=20)
        self.HIGH_30 = talib.MAX(self.high,timeperiod=30)
        self.LOW_10 = talib.MIN(self.low, timeperiod=10)
        self.base = 10000


    def add(self):
        print('这是股票代码为:',self.code, '名字为：', self.return_name(self.code))
        i=21
        start_price=0
        for i in range(21, len(self.close)):
            if start_price ==0 and self.close[i] > self.HIGH_30[i-1] + 0.5* self.atr_20[i-1]:
                print('这是开仓信号',self.transit_date[i], 'buy', self.close[i])
                start_price = self.close[i]
            if start_price != 0 and self.close[i] < self.LOW_10[i-1]:
                result = round((self.close[i]-start_price)/start_price,2)*self.base
                print('这是清仓信号',self.transit_date[i],'sell',self.close[i],'盈利为：', result)
                start_price = 0
        print('这是股票代码为:', self.code, '名字为：', self.return_name(self.code))

class bs_haigui(haigui):
    def get_bs_files(self,code):
        test.get_csv_files(code)
    def check_file(self):
        return os.path.exists(os.path.join(r'C:\Users\Administrator\Downloads','bs_'+code+'.csv'))
    def __init__(self,code):
        self.get_bs_files(code)
        if self.check_file():
            csvfile = os.path.join(r'C:\Users\Administrator\Downloads','bs_'+code+'.csv')
            self.code = os.path.basename(csvfile).split('_')[1][:6]
            self.df = pd.read_csv(csvfile)
            self.close = np.array(self.df['close'])
            self.transit_date = np.array(self.df['date'])
            self.high = np.array(self.df['high'])
            self.low = np.array(self.df['low'])
            self.atr_20 = talib.ATR(self.high, self.low, self.close, timeperiod=20)
            self.HIGH_30 = talib.MAX(self.high, timeperiod=30)
            self.LOW_10 = talib.MIN(self.low, timeperiod=10)
        self.base = 10000
    def __del__(self):
        print('测试完成，析构')


if __name__ == '__main__':
    # csvfile = '159901历史数据.csv'
    code = '300554'
    # code = '002367'
    # code = '159901'
    # code = '601369'
    # code = '603866'
    # data_dir = r'C:\Users\Administrator\Downloads'
    # for item in os.listdir(data_dir):
    #     if code in item and 'bs_' in item:
    #         csvfile = os.path.join(data_dir, item)
    for code in ['002367','601369','603866','300554']:
        # print(code)
        tt = bs_haigui(code)
        tt.add()

#不能用for来调用一系列的code，
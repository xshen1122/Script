import baostock as bs
import pandas as pd
import os
def return_header(code):
    if code[0] == '6':
        header = 'sh.'
    elif code[0] in ['0','3']:
        header = 'sz.'
    else:
        return 'Wrong'
    return header

def get_csv_files(code):

    lg = bs.login()
    print('login respond error_code:'+lg.error_code)

    print('login respond error_msg:'+lg.error_msg)
    if return_header(code) != 'Wrong':
        rs = bs.query_history_k_data_plus(return_header(code)+code,
        "date,code,high,low,close",
        start_date='2019-01-01',
        frequency="d", adjustflag="3")
    print('query_history_k_data_plus respond error_code:'+rs.error_code)
    print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

    #### 打印结果集 ####
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)

    #### 结果集输出到csv文件 ####
    data_dir = r"C:\Users\Administrator\Downloads"
    filename = 'bs_' + code +'.csv'
    result.to_csv(os.path.join(data_dir, filename), index=False)
    # print(result)

    #### 登出系统 ####
    bs.logout()

if __name__ == '__main__':
    print(return_header('300554'))
    get_csv_files('300554')
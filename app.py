from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


#建立首页路径
@app.route('/index')        #建立路径
def home():  # put application's code here
    #return render_template('index.html')        #返回网页
    return index()


@app.route('/work')
def work():  # put application's code here
    return render_template('work.html')


@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')


@app.route('/blog-single')
def blog_single():  # put application's code here
    '''    # 数据库引用
    datalist_21a = []       #21年的总资产    形成列表
    datalist_21l = []       #21年的总负债    形成列表
    datalist_22a = []       #22年的总资产    形成列表
    datalist_22l = []       #22年的总负债    形成列表

    #通用的步骤
    con = sqlite3.connect('alldatabase.db')     #连接数据库
    cur = con.cursor()                          #获取游标

    #引入表     21年的总资产
    sql_21a = "select Amount / 100000000 from stock_info where Date = '2021-12-31 00:00:00' and ITEM_CODE = '004009999'"
    #执行
    data_21a = cur.execute(sql_21a)
    #读取data_21a里一条总资产数据     就加一条数据到datalist_21a
    for item in data_21a:
        datalist_21a.append(item[0])            #[6]是总资产的数据
    # print(test1)

    sql_21l = "select Amount / 100000000 from stock_info where Date = '2021-12-31 00:00:00' and ITEM_CODE = '004025999'"
    data_21l = cur.execute(sql_21l)
    for item in data_21l:
        datalist_21l.append(item[0])
    # print(test2)

    #合并表    使用 list    map     zip     使多列表生成新的列表      [[a,b],[1,2]]       也就是21年[总资产,总负债]形式的列表
    multi_list21 = list(map(list, zip(datalist_21a, datalist_21l)))
    # print(multi_list21)

    # 引入表     22年的总资产
    sql_22a = "select Amount / 100000000 from stock_info where Date = '2022-12-31 00:00:00' and ITEM_CODE = '004009999'"
    # 执行
    data_22a = cur.execute(sql_22a)
    # 读取data_22a里一条总资产数据     就加一条数据到datalist_22a
    for item in data_22a:
        datalist_22a.append(item[0])  # [6]是总资产的数据
    # print(datalist_22a)

    sql_22l = "select Amount / 100000000 from stock_info where Date = '2022-12-31 00:00:00' and ITEM_CODE = '004025999'"
    data_22l = cur.execute(sql_22l)
    for item in data_22l:
        datalist_22l.append(item[0])
    # print(datalist_22l)

    # 合并表    使用 list    map     zip     使多列表生成新的列表      [[a,b],[1,2]]       也就是22年[总资产,总负债]形式的列表
    multi_list22 = list(map(list, zip(datalist_22a, datalist_22l)))
    # print(multi_list22)

    cur.close()
    con.close()

    return render_template('blog-single.html', multi_list21=multi_list21, multi_list22=multi_list22)'''
    return render_template('blog-single.html')


if __name__ == '__main__':
    app.run()

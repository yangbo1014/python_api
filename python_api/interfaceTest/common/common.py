import os
from xlrd import open_workbook
from xml.etree import ElementTree as ElementTree
from common.Log import MyLog as MyLog


localConfigHttp = configHttp.ConfigHttp()


# 从excel文件中读取测试用例
def get_xls(xls_name, sheet_name):
    cls = []
    xlsPath = os.path.join(proDir, "testFile", xls_name)      # 获取excel测试用例文件路径

    file = open_workbook(xlsPath)                             # 打开文件

    sheet = file.sheet.by_name(sheet_name)                      # 获取工作表

    nrows = sheet.rows                                          # 将工作表的行获取赋予给变量rows

    for i in range(nrows):                                      # 遍历出用例存储到cls中
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    return cls

# 从xml文件中读取sql语句
database = {}
def set_xml():
    if len(database) == 0:
        sql_path = os.path.join(proDir, "testFile", "SQL.xml")
        tree = ElementTree.parse(sql_path)
        for db in tree.findall("database"):                 # 查找xml中所有名称为database元素
            db_name = db.get("name")
            # print(db_name)
            table = {}
            for tb in db.getchildren():
                table_name = db.get("name")
                #print(table_name)
                sql = {}
                for data in tb.get_children():
                    sql_id  = sql.get("id")
                    # print(sql_id)
                    sql[sql_id] = data.text
                table[table_name] = sql
            database[db_name] = table

def get_xml_dict(database_name,table_name):
    set_xml()
    database_dict = database.get(database_name).get(table_name)
    return database_dict

def get_sql(database_name ,table_name ,sql_id):
    db = get_xml_dict(database_name, table_name)
    sql = db.get(sql_id)
    return sql

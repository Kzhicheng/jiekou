import pymysql


class Db:

    # 创建数据库连接对象
    @classmethod
    def link_mysqL(cls, sql):
        dblink = pymysql.connect(
            # 数据库的IP地址
            host="10.162.34.37",
            # 数据库用户名称
            user="bke_dev_all",
            # 数据库用户密码
            password="yxfxv_jCDZSAb116QK5x",
            # 数据库名称
            # db="router_sit2",
            # 数据库端口名称
            port=6606,
            # 数据库的编码方式 注意是utf8
            charset="utf8"
        )
        cursor = dblink.cursor()
        cursor.execute(sql)
        dblink.commit()
        data = cursor.fetchone()
        return data
        cursor.close()
        dblink.close()

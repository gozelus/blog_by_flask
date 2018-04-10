
class Config:
    SECRET_KEY = 'wjioqdjiwoqj'
    @staticmethod
    def init_app(app):
        pass
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql://root:Zhengli123@rm-2ze0sw4tx2r68q87qto.mysql.rds.aliyuncs.com/doubandushu?charset=utf8"

config = {
    "development":DevelopmentConfig
}
class Config():
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_ECHO = True #在终端打印SQL语句
    SQLALCHEMY_TRACK_MODIFICATIONS = False #禁用跟踪
    SQLALCHEMY_COMMIT_TEARDOWN = True #启用自动提交
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:sxy960806@netconfig.cn:3306/api'
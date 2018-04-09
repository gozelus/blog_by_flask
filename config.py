class Config:
    SECRET_KEY = "hwuidhiqw"

class DevelopConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:3306/blog_by_flask'    

config = {
    "develop": DevelopConfig
}
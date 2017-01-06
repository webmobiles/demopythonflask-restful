class Config:
    MONGO_URI = 'mongodb://localhost:27017/crm1'
    @staticmethod
    def init_app(app):
        pass

mongoConfig = Config

class Credentials(object):
    """description of class"""
    def __init__(self, clientId, userName, password, clientSecret):
        self.clientId = clientId
        self.userName = userName
        self.password = password
        self.clientSecret = clientSecret
        return super().__init__()



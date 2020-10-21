""" 
save.py file has:
class Save: store information of a save_job such as username,title
"""
class Save:
    def __init__(self, username, title):
        self.__username = username
        self.__title = title
    
    def get_username(self):
        return self.__username

    def get_title(self):
        return self.__title


        
        
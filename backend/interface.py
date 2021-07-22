from abc import ABCMeta, abstractclassmethod


class DbInterface():

    @abstractclassmethod
    def create_tables():
        pass

    @abstractclassmethod
    def insert_data_anime_search():
        pass

    @abstractclassmethod
    def insert_data_anime_by_id():
        pass

    @abstractclassmethod
    def insert_data_genre_anime():
        pass

    @abstractclassmethod
    def insert_data_manga_search():
        pass

    @abstractclassmethod
    def show_data():
        pass

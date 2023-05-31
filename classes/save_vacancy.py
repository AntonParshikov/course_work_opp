import json
import os
from classes.head_hunter import HeadHunterAPI
from classes.super_job import SuperJobAPI


class JSONSaver:

    def __init__(self):
        pass

    def add_vacancy(self, obj):
        file_name = '../vacancy_files/{}.json'.format(len(os.listdir('../vacancy_files/')))
        file = open(file_name, mode='w', encoding='utf8')
        _list = [v.to_dict() for v in obj]
        file.write(json.dumps(_list, ensure_ascii=False, indent=2))
        file.close()

    def rem_vacancy(self):
        pass

    def get_info(self):
        pass


if __name__ == '__main__':
    client = HeadHunterAPI()
    hh_vacancy = client.get_vacancies('Python')
    JSONSaver().add_vacancy(hh_vacancy)

    client_1 = SuperJobAPI()
    sj_vacancy = client_1.get_vacancies('Python')
    JSONSaver().add_vacancy(sj_vacancy)

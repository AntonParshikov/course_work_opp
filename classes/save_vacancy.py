import json
import os
from classes.head_hunter import HeadHunterAPI
from classes.super_job import SuperJobAPI


class JSONSaver:

    def __init__(self):
        pass

    def add_vacancy(self, obj):
        # file_name = '../vacancy_files/{}.json'.format(len(os.listdir('../vacancy_files/')))
        file = open('../vacancy_files/vacancy.json', mode='w', encoding='utf8')
        _list = [v.to_dict() for v in obj]
        file.write(json.dumps(_list, ensure_ascii=False, indent=2))
        file.close()

    def rem_vacancy(self, vacancy_del = str(input('Введите вакансию, которую нужно удалить? \n'))):

        with open('../vacancy_files/vacancy.json', mode='r', encoding='utf8') as file:
            obj = json.load(file)
            for v in obj:
                if v['Профессия'] == vacancy_del:
                    obj.remove(v)
            with open('../vacancy_files/vacancy.json', mode='w', encoding='utf8') as out_file:
                json.dump(obj, out_file, ensure_ascii=False, indent=2)
            out_file.close()

    def get_info(self):
        pass


if __name__ == '__main__':
    # client = HeadHunterAPI()
    # hh_vacancy = client.get_vacancies('Python')
    # JSONSaver().add_vacancy(hh_vacancy)

    # client_1 = SuperJobAPI()
    # sj_vacancy = client_1.get_vacancies('Python')
    # JSONSaver().add_vacancy(sj_vacancy)

    JSONSaver().rem_vacancy()



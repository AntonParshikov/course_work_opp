from classes.vacancy import Vacancy
from classes.working_with_api import WorkingWithAPI
import json
import requests


class HeadHunterAPI(WorkingWithAPI):

    def __init__(self):
        pass

    def get_vacancies(self, job_title):
        params = {
            'text': job_title,
            'area': 1,
            'page': 0,
            'per_page': 100
        }
        req = requests.get('https://api.hh.ru/vacancies', params)
        data = req.content.decode()
        req.close()
        js_obj = json.loads(data)
        return self.vacancies_pars(js_obj)

    def vacancies_pars(self, js_obj):
        all_vacancy = []
        for obj in js_obj['items']:
            salary = obj.get('salary') or {}
            all_vacancy.append(Vacancy(**{
                'title': obj['name'],
                'salary_from': salary.get('from', 0),
                'salary_to': salary.get('to', 0),
                'employer': obj['employer']['name'],
                'url': obj['url'],
                'req': obj['snippet']['requirement']
            }))

        return all_vacancy


if __name__ == "__main__":
    client = HeadHunterAPI()

    search_query = input('Вы выбрали HH \nВведите поисковый запрос: \n')
    hh_vacancy = client.get_vacancies(search_query)
    print(hh_vacancy)

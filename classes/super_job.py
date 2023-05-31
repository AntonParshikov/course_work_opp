import requests
from classes.vacancy import Vacancy
import os
from classes.working_with_api import WorkingWithAPI


class SuperJobAPI(WorkingWithAPI):

    def __init__(self):
        pass

    def get_vacancies(self, job_title):
        params = {'count': 20,
                  'town': 0,
                  'keyword': job_title
                  }
        super_job_api = 'v3.r.137575001.25e7b42b93e4624890e7bdde41d586b710997eb3.' \
                        '4e28b814a6d6f7ea4e9415050236c7948508cf49'
        headers = {'X-Api-App-Id': super_job_api}
        req = requests.get('https://api.superjob.ru/2.0/%s' % 'vacancies/', params, headers=headers)
        return self.vacancies_pars(req.json())

    def vacancies_pars(self, js_obj):
        all_vacancy = []
        for obj in js_obj['objects']:
            all_vacancy.append(Vacancy(**{
                'title': obj['profession'],
                'salary_from': obj['payment_from'],
                'salary_to': obj['payment_to'],
                'employer': obj['firm_name'],
                'url': obj['link'],
                'req': obj['candidat']
            }))
            # all_vacancy.append({
            #     'title': obj['profession'],
            #     'salary_from': obj['payment_from'],
            #     'salary_to': obj['payment_to'],
            #     'employer': obj['firm_name'],
            #     'url': obj['link'],
            #     'req': obj['candidat']
            # })
        return all_vacancy


if __name__ == "__main__":
    pass



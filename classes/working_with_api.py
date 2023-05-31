from abc import ABC, abstractmethod


class WorkingWithAPI(ABC):

    @abstractmethod
    def get_vacancies(self, job_title):
        pass


if __name__ == "__main__":
    pass

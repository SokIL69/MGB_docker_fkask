# MGB_docker_fkask
Итоговый проект курса "Машинное обучение в бизнесе"

Стек:

ML: sklearn, pandas, numpy API: flask Данные: с kaggle - https://www.kaggle.com/c/654pds2courseproject/data

Задача: Требуется, на основании имеющихся данных о клиентах банка, построить модель, используяобучающий датасет,
	для прогнозирования невыполнения долговых обязательств по текущему кредиту. Бинарная классификация

Используемые признаки:

1. Home Ownership - домовладение
2. Annual Income - годовой доход
3. Years in current job - количество лет на текущем месте работы
4. Tax Liens - налоговые обременения
5. Number of Open Accounts - количество открытых счетов
6. Years of Credit History - количество лет кредитной истории
7. Maximum Open Credit - наибольший открытый кредит
8. Number of Credit Problems - количество проблем с кредитом
9. Months since last delinquent - количество месяцев с последней просрочки платежа
10. Bankruptcies - банкротства
11. Purpose - цель кредита
12. Term - срок кредита
13. Current Loan Amount - текущая сумма кредита
14. Current Credit Balance - текущий кредитный баланс
15. Monthly Debt - ежемесячный долг
16. Credit Score - Кредитный рейтинг
17. Credit Default - факт невыполнения кредитных обязательств (0 - погашен вовремя, 1 -просрочка)

Преобразования признаков:
1. Обработка пропусков
2. Обработка выбрасов
3. Обработка категорий
4. Генерация новых фич


Модель: catboost

Клонируем репозиторий и создаем образ
$ git clone https://github.com/fimochka-sudo/GB_docker_flask_example.git
$ cd GB_docker_flask_example
$ docker build -t fimochka/gb_docker_flask_example .
Запускаем контейнер
Здесь Вам нужно создать каталог локально и сохранить туда предобученную модель (<your_local_path_to_pretrained_models> нужно заменить на полный путь к этому каталогу)

$ docker run -d -p 8180:8180 -p 8181:8181 -v <your_local_path_to_pretrained_models>:/app/app/models fimochka/gb_docker_flask_example

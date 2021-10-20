# python-flask-docker
Итоговый проект курса "Машинное обучение в бизнесе"
Задание выполнил Соковнин И.Л.

Стек:

ML: sklearn, pandas, numpy API: flask Данные: с kaggle - https://www.kaggle.com/c/654pds2courseproject/data

Задача: Требуется, на основании имеющихся данных о клиентах банка, построить модель, используяобучающий датасет, для прогнозирования невыполнения долговых обязательств по текущему кредиту. Бинарная классификация

Используемые признаки:

Home Ownership - домовладение
Annual Income - годовой доход
Years in current job - количество лет на текущем месте работы
Tax Liens - налоговые обременения
Number of Open Accounts - количество открытых счетов
Years of Credit History - количество лет кредитной истории
Maximum Open Credit - наибольший открытый кредит
Number of Credit Problems - количество проблем с кредитом
Months since last delinquent - количество месяцев с последней просрочки платежа
Bankruptcies - банкротства
Purpose - цель кредита
Term - срок кредита
Current Loan Amount - текущая сумма кредита
Current Credit Balance - текущий кредитный баланс
Monthly Debt - ежемесячный долг
Credit Score - Кредитный рейтинг
Credit Default - факт невыполнения кредитных обязательств (0 - погашен вовремя, 1 -просрочка)


Преобразования признаков:
- Обработка пропусков
- Обработка выбрасов
- Обработка категорий
- Генерация новых фич
- Нормализация данных

Модель: logreg

Каталог app/models/:
1. Модель-пайплайн предобученная:
  - logreg_pipeline_v15.dll
2. Подготовленные файлы с преобразованными данными для тестирования:
  - X_test.csv
  - Y_test.csv
3. Файл с кодом для тестирования модели из jupyter notebook:
  - step_3_15.ipynb
4. Текст задания:
  - HW.ipynb



Клонируем репозиторий и создаем образ 
'''
$ git clone https://github.com/SokIL69/MLB_docker_flask.git 
$ cd MLB_docker_flask 
$ docker build -t sil/gb_mlb_docker_flask . 
'''
Запускаем контейнер

Необходимо локально создать каталог и сохранить в нём предобученную модель (<your_local_path_to_pretrained_models> нужно  заменить на полный путь к этому каталогу)

$ docker run -d -p 8182:8182 -p 8181:8181 -v <your_local_path_to_pretrained_models>:/app/app/models sil/gb_mlb_docker_flask

Файл с кодом для тестирования модели из jupyter notebook:
  - step_3_15.ipynb

### Открыть в jupyter notebook файл step_3_15.ipynb
### web-api - localhost:8182
### Перейти на web-страницу - localhost:8181

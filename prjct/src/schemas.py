from marshmallow import Schema, fields
import os


class SearchPageSchema(Schema):
    webpage = fields.String(description="Простая веб-страница с возможностью поиска с использованием API", required=True, example=' '.join(
        [str(elem) for elem in open(os.path.join(os.getcwd(), 'search.html')).readlines()]), encoding='utf-8')


class SearchParametersSchema(Schema):
    q = fields.String(description="Строка, которую необходимо найти",
                      required=True, example='Привет', encoding='utf-8')


class SearchResponseSchema(Schema):
    response = fields.String(description="Список из минимум 0 и максмум 20 найденных результатов, отсортированных по дате создания в порядке возрастания", required=True, example='[{"created_date":"Wed, 09 Jan 2019 20:55:44 GMT","id":16796,"rubrics":["VK-1603736028819866","VK-88413115730","VK-69103370657"],"text":"\u041c\u0443\u0436\u0438\u043a\u0438 \u0432\u0441\u0435\u043c \u043f\u0440\u0438\u0432\u0435\u0442, \u043f\u043e\u0434\u0441\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430 \u0433\u0434\u0435 \u043f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043a\u043e\u0434\u044b \u043e\u0448\u0438\u0431\u043e\u043a \u043d\u0430 \u043c\u0435\u0440\u0441\u0435\u0434\u0435\u0441 \u0432\u0438\u0430\u043d\u043e \u0433\u043e\u0434 2008, \u043c\u043e\u0442\u043e\u0440 2.2 150 \u043a\u043e\u0431\u044b\u043b"},{"created_date":"Tue, 15 Jan 2019 19:47:26 GMT","id":17874,"rubrics":["VK-1603736028819866","VK-10847316026","VK-27470760776"],"text":"\u041f\u0440\u0438\u0432\u0435\u0442 \u0432\u0430\u043c \u0438\u0437 \u0434\u0435\u0442\u0441\u0442\u0432\u0430, \u043e\u0442 \u0421\u0430\u0448\u0435\u043d\u044c\u043a\u0438 \u0438 \u0412\u043e\u0432\u043a\u0438\u2764 \u043e\u043d\u0438 \u0441\u0435\u0439\u0447\u0430\u0441 \u043d\u0430\u0432\u0430\u043b\u044f\u044e\u0442\u0441\u044f \u0432\u0434\u043e\u0432\u043e\u043b\u044c, \u043f\u0440\u043e\u043c\u043e\u043a\u043d\u0443\u0442 \u0434\u043e \u043d\u0438\u0442\u043a\u0438 \u0438 \u0433\u0440\u0435\u0442\u044c\u0441\u044f \u0431\u0435\u0433\u043e\u043c \u0434\u043e\u043c\u043e\u0439, \u043a \u0431\u0430\u0442\u0430\u0440\u0435\u0435. \n\u0410 \u043a\u0430\u043a\u043e\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u0443 \u0432\u0430\u0441? \u2744"}]', encoding='utf-8')


class DeleteParametersSchema(Schema):
    id = fields.Int(description="Индекс документа в поисковом индексе",
                    required=True, example=16796, encoding='utf-8')


class DeleteSuccessSchema(Schema):
    response = fields.String(description="Документ с заднным `id` найден, удаление успешно",
                             required=True, example="{'message':'success'}", encoding='utf-8')


class DeleteErrorSchema(Schema):
    response = fields.String(description="Документ с заднным `id` не найден, ошибка удаления",
                             required=True, example="{'message':'error'}", encoding='utf-8')

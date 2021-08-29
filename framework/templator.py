from jinja2 import Template
import os


def render(template_name, folder='project/templates', **kwargs):
    """
    Минимальный пример работы с шаблонизатором
    :param folder:
    :param template_name: имя шаблона
    :param kwargs: параметры для передачи в шаблон
    :return:
    """

    file_path = os.path.join(folder, template_name)
    with open(file_path, encoding='utf-8') as f:
        template = Template(f.read())
    return template.render(**kwargs)


# if __name__ == '__main__':
#     output_test = render('index.html', object_list=[{'name': 'Leo'}, {'name': 'Kate'}])
#     print(output_test)

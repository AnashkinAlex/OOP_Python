class RenderList:
    def __init__(self, type_list):
        self. type_list =  type_list if type_list in ('ol','ul') else 'ul'

    def __call__(self,lst, *args, **kwargs):
        html = f'<{self. type_list}> \n'
        for item in lst:
            html += f'<li>{item}</li>\n'

        html += f'</{self. type_list}>'
        return html

lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("olv")
html = render(lst)
print(html)


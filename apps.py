from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
    menu = (
        ParentItem('Controle de Acesso', children=[
            ChildItem('Usuários', model='account.user'),
            ChildItem('Grupos', model='auth.group'),
        ]),
    )


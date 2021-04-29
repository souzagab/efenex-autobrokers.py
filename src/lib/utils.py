"""
Funcoes multiuso
"""


def clear():
    """
    Limpa a tela comparando sistema operacional
    """
    from platform import system as system_name
    from subprocess import call   as system_call

    command = 'cls' if system_name().lower()=='windows' else 'clear'
    system_call([command])

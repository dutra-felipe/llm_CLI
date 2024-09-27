from observer.observer import ResponseNotifier, UserObserver
from unittest.mock import MagicMock

def test_add_observer():
    notifier = ResponseNotifier()
    observer = MagicMock()

    notifier.add_observer(observer)
    assert observer in notifier.observers

def test_notify_observers():
    notifier = ResponseNotifier()
    observer1 = MagicMock()
    observer2 = MagicMock()

    notifier.add_observer(observer1)
    notifier.add_observer(observer2)

    message = "Nova mensagem"

    notifier.notify(message)

    observer1.update.assert_called_once_with(message)
    observer2.update.assert_called_once_with(message)

def test_user_observer_update(capsys):
    observer = UserObserver()
    
    observer.update("Mensagem de teste")
    
    captured = capsys.readouterr()
    assert captured.out == "Atualização: Mensagem de teste\n"

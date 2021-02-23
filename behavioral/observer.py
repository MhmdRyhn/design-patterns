import abc
from random import randint


class SubjectInterface(abc.ABC):
    @abc.abstractmethod
    def attach(self, observer):
        pass

    @abc.abstractmethod
    def detach(self, observer):
        pass

    @abc.abstractmethod
    def notify(self):
        pass


class Subject(SubjectInterface):
    def __init__(self):
        self._observers = []
        self.number = -1

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, **kwargs):
        for observer in self._observers:
            observer.update(self)

    def some_execution(self):
        self.number = randint(1, 8)
        self.notify()


class ObserverInterface(abc.ABC):
    @abc.abstractmethod
    def update(self, subject):
        pass


class ObserverA(ObserverInterface):
    def update(self, subject):
        print("Notification sent to ObserverA >>", subject.number)


class ObserverB(ObserverInterface):
    def update(self, subject):
        print("Notification sent to ObserverB >>", subject.number)


class ObserverC(ObserverInterface):
    def update(self, subject):
        print("Notification sent to ObserverC >>", subject.number)


if __name__ == '__main__':
    subject = Subject()

    print("Before attaching any observer -->>")
    subject.some_execution()

    observer_a = ObserverA()
    observer_b = ObserverB()
    # Attaching observer_a, observer_b
    subject.attach(observer_a)
    subject.attach(observer_b)
    print("\nAfter attaching ObserverA, ObserverB -->>")
    subject.some_execution()

    observer_c = ObserverC()
    # Attaching observer_c
    subject.attach(observer_c)
    print("\nAfter attaching ObserverC (ObserverA, ObserverB were previously attached) -->>")
    subject.some_execution()

    # Detaching observer_b
    subject.detach(observer_b)
    print("\nAfter detaching ObserverB from ObserverA, ObserverB, ObserverC -->>")
    subject.some_execution()

from abc import ABC, abstractmethod
from random import randint


class SubjectInterface(ABC):
	@abstractmethod
	def attach(self, observer):
		pass

	@abstractmethod
	def detach(self, observer):
		pass

	@abstractmethod
	def notify(self):
		pass


class Subject(SubjectInterface):
	def __init__(self):
		self._observers = list()
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

	def some_logic(self):
		self.number = randint(0, 7)
		self.notify()
		print()



class ObserverInterface(ABC):
	@abstractmethod
	def update(self, subject):
		pass


class Observer_A(ObserverInterface):
	def update(self, subject):
		if 0 <= subject.number <= 2 or 5 <= subject.number <= 7:
			print('Updating Observer_A:', subject.number)


class Observer_B(ObserverInterface):
	def update(self, subject):
		if 2 <= subject.number <= 5:
			print('Updating Observer_B:', subject.number)



if __name__ == '__main__':
	subject = Subject()

	observer_a = Observer_A()
	observer_b = Observer_B()

	subject.attach(observer_a)
	subject.attach(observer_b)

	for _ in range(5):
		subject.some_logic()

	print('....... After Detaching .........\n')
	subject.detach(observer_a)
	for _ in range(5):
		subject.some_logic()

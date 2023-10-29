from abc import ABC, abstractmethod

from src.user_actions_handler import get_handler
from src.utils.constants import INVITE_MESSAGE, TYPE_OR_ATTRIBUTE_ERROR_MESSAGE
from src.utils.parser import parser
import globals


class AbstractBot(ABC):
    @abstractmethod
    def run(self):
        ...


class CLIBot(AbstractBot):
    def __init__(self):
        self.user_interface = CLIUserInterface()

    def run(self):
        while globals.IS_LISTENING:
            user_line = self.user_interface.get_input()

            if user_line:
                try:
                    command, data = parser(user_line)
                    handler = get_handler(command)
                    result = handler(data)
                    self.user_interface.yield_output(result)
                    continue
                except AttributeError:
                    print(f'{TYPE_OR_ATTRIBUTE_ERROR_MESSAGE} \n{get_handler("help")()}')


class AbstractUserInterface(ABC):
    @abstractmethod
    def get_input(self):
        ...

    @abstractmethod
    def yield_output(self, output):
        ...


class CLIUserInterface(AbstractUserInterface):

    def get_input(self):
        return input(INVITE_MESSAGE)

    def yield_output(self, output):
        print(output)

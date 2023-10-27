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

    def run(self):
        while globals.IS_LISTENING:
            user_line = input(INVITE_MESSAGE)

            if user_line:
                try:
                    command, data = parser(user_line)
                    handler = get_handler(command)
                    result = handler(data)
                    print(result)
                    continue
                except AttributeError:
                    print(f'{TYPE_OR_ATTRIBUTE_ERROR_MESSAGE} \n{get_handler("help")()}')
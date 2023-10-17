class EmptyPhoneNumberError(Exception):
    pass


def input_error(handler):
    def error_handler(data):
        try:
            return handler(data)
        except EmptyPhoneNumberError:
            return f'Phone is required'
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command format"
        except Exception as error:
            return f'Something happens: {error}'
        

    return error_handler

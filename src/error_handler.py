class EmptyPhoneNumberError(Exception):
    pass


def input_error(handler):
    def error_handler(data):
        try:
            return handler(data)
        except EmptyPhoneNumberError:
            return f'Phone is required'
        except Exception as error:
            return f'Something happens: {error}'

    return error_handler

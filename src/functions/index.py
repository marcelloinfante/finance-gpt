from src.functions.enums import FunctionsEnum


class Functions:
    @classmethod
    def execute(self, function_name, **args):
        function = FunctionsEnum[function_name].value
        function_response = function.run(**args)

        return function_response

    @classmethod
    def list_functions(self):
        serialized_functions = []

        for function in list(FunctionsEnum):
            function_class = function.value

            serialized_functions.append(function_class.get_infos())

        return serialized_functions

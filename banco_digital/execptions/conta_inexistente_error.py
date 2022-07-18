from rest_framework.exceptions import APIException

class ContaInexistenteError(APIException):
    
    status_code = 404
    default_detail = "Conta inexistente!"
    default_code = "conta_inexistente"
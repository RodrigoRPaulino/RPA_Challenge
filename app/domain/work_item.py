# Importa o decorator dataclass para criar uma classe de dados automaticamente
from dataclasses import dataclass


# O decorator @dataclass gera automaticamente:
# - __init__
# - __repr__
# - __eq__
# - e outros métodos úteis
# Isso evita escrever código repetitivo
@dataclass
class WorkItem:
    # Cada atributo representa uma coluna do Excel
    # A tipagem ajuda o type checker (Pylance) e melhora legibilidade
    first_name: str
    last_name: str
    company_name: str
    role_in_company: str
    address: str
    email: str
    phone_number: str

    # Método de validação simples
    # Ele verifica se todos os campos possuem algum valor (não vazio)
    def is_valid(self) -> bool:
        # A função all() retorna True se TODOS os valores forem truthy
        # Strings vazias ("") são consideradas False
        return all((
            self.first_name,
            self.last_name,
            self.company_name,
            self.role_in_company,
            self.address,
            self.email,
            self.phone_number,
        ))
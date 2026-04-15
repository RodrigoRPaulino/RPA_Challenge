# Tipagem forte
from typing import List

# Entidade de domínio
from app.domain.work_item import WorkItem

# Serviço de infraestrutura
from app.services.excel_service import ExcelService


class Dispatcher:

    # Recebe ExcelService por injeção
    # Isso permite trocar implementação futuramente
    def __init__(self, excel_service: ExcelService) -> None:
        self._excel_service = excel_service

    # Método principal do Dispatcher
    # Responsável por "preparar" os itens
    def dispatch(self, file_path: str) -> List[WorkItem]:

        # Lê todos os itens do Excel
        work_items = self._excel_service.read_work_items(file_path)

        # Filtra apenas itens válidos
        # Regra de negócio começa aqui
        valid_items = [item for item in work_items if item.is_valid()]

        # Retorna somente os válidos
        return valid_items
from typing import List
from app.services.excel_service import ExcelService
from app.domain.work_item import WorkItem


class Dispatcher:

    def __init__(self):
        self._excel_service = ExcelService()

    def run(self, file_path: str) -> List[WorkItem]:
        # Lê todos os itens do Excel
        items = self._excel_service.read_work_items(file_path)

        # Filtra apenas itens válidos
        valid_items = [item for item in items if item.is_valid()]

        print(f"Total lidos: {len(items)}")
        print(f"Total válidos: {len(valid_items)}")

        return valid_items
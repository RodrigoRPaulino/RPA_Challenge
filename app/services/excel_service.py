# Tipagem para listas fortemente tipadas
from typing import List

# Biblioteca para leitura de Excel
import pandas as pd

# Importa a entidade de domínio
from app.domain.work_item import WorkItem


class ExcelService:
    # Método responsável por ler um arquivo Excel
    # Recebe caminho e retorna lista de WorkItem
    def read_work_items(self, file_path: str) -> List[WorkItem]:

        # Lê o Excel inteiro para um DataFrame
        # Cada linha vira uma "row"
        #vamos explicitar o tipo para evitar erros visuais no código
        df = pd.read_excel(file_path) # type: ignore
       
       #Tratar colunas
        df.columns = df.columns.str.strip()

        # Inicializa lista tipada vazia
        work_items: List[WorkItem] = []

        # Percorre cada linha do DataFrame
        # _ é o índice (que não usamos)
        # row é a linha atual
        for _, row in df.iterrows():

            # Cria uma instância de WorkItem
            # Mapeando cada coluna do Excel para atributo do domínio
            item = WorkItem(
                first_name=row["First Name"],
                last_name=row["Last Name"],
                company_name=row["Company Name"],
                role_in_company=row["Role in Company"],
                address=row["Address"],
                email=row["Email"],
                phone_number=row["Phone Number"],
            )

            # Adiciona à lista
            work_items.append(item)

        # Retorna lista final
        return work_items
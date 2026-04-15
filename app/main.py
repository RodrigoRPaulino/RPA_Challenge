# Importa dependências necessárias
from app.services.excel_service import ExcelService
from app.dispatcher.dispatcher import Dispatcher


# Função principal do programa
def main() -> None:

    # Instancia serviço de infraestrutura
    excel_service = ExcelService()

    # Injeta dependência no Dispatcher
    dispatcher = Dispatcher(excel_service)

    # Executa fluxo principal
    items = dispatcher.dispatch(
        r"C:\Users\rodri\Downloads\challenge.xlsx"
    )

    # Exibe quantidade de itens válidos
    print(f"Itens válidos: {len(items)}")

    # Mostra primeiro item para debug
    print(items[0])


# Garante execução apenas se rodar como módulo principal
if __name__ == "__main__":
    main()
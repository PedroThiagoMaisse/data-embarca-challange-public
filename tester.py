import tests.services_test as services
import tests.utils_test as utils

def main():
    print('Começando os testes\n')

    results = [
        services.main(),
        utils.main(),
    ]

    for item in results:
        if not item["success"]:
            print('FALHA:')
            print(item)
            return False
        else:
            print(item["response"])

    print('\nTodos testes bem sucedidos!')
    return True

main()

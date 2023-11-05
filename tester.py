import services.test as services
import utils.test as utils

def main():
    print('Começando testes\n')

    results = [
        services.main(),
        utils.main(),
    ]

    for item in results:
        if not item["success"]:
            print('FALHA: \n' + item)
            return False
        else:
            print(item["response"])

    print('\nTodos testes bem sucedidos!')
    return True

main()
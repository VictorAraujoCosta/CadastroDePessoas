# 1- Pessoa Fisica / 2 - Pessoa Juridica / 3 - Sair
# 1 - Cadastrar Pessoa Física / 2 - Listar Pessoal Física / 3 - Sair
# 1 - Cadastrar Pessoa Juridica / 2 - Listar Pessoa Juridica / 3 - Sair

from datetime import date, datetime

from Pessoa import Endereco, PessoaFisica


def main():
    lista_pf = []
    while True:
        opcao = int(input("Selecione uma opção: 1- Pessoa Física / 2 - Pessoa Jurídica / 0 - Sair"))

        if opcao == 1:
            while True:
                opcao_pf = int(input("Escolha uma opção: 1- Pessoa Física / 2 - Listar Pessoa Física / 0 - Voltar ao menu anterior"))
                # 1 - Cadastrar uma Pessoa Física
                if opcao_pf == 1:
                    novapf = PessoaFisica()
                    novo_end_pf = Endereco()

                    novapf.nome = input("Digite o nome da pessoa física")
                    novapf.cpf = input("Digíte o CPF")
                    novapf.rendimento = input("Digite o rendimento mensal (Digíte somente números):")

                    data_nascimento = input("Digite a data de nascimento (dd/MM/aaaa)") # Solicita a data de nascimento
                    novapf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade = (date.today() - novapf.dataNascimento).days // 365 #Calcula a idade da pessoa

                    if idade >= 18:
                        print("A pessoa tem mais de 18 anos")
                    else:
                        print("A pessoa tem menos de 18 anos. Retorne ao menu...")
                        continue # Retonar ao ínicio do loop

                    # CADASTRO DE ENDEREÇO
                    novo_end_pf.logradouro = input("Digíte o logradouro: ")
                    novo_end_pf.numero = input("Digite o número: ")
                    end_comercial = input("Este endereço é comercial: S/N:")
                    novo_end_pf.endereco_Comercial = end_comercial.strip().upper() == 'S' # Define se o string é maísculo
                    
                    novapf.endereco = novo_end_pf

                    lista_pf.append(novapf)

                    print('Cadastro realizado com sucesso!')

                    #LISTAR PESSOA FÍSICA

                elif opcao_pf == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f'Nome: {cada_pf.nome}')
                            print(f'CPF: {cada_pf.cpf}')
                            print(f'Endereço: {cada_pf.endereco.logradouro}, {cada_pf.endereco.numero}')
                            print(f'Data nascimento: {cada_pf.data_Nascimento.strftime('%d/%m/%Y')}')
                            print(f'Imposto a ser pago: {cada_pf.calcular_imposto(cada_pf.rendimento)}')
                            print('Dígite 0 para sair')
                            input()
                    else:
                        print("Lista vazia")

                    #SAIR DO MENU ATUAL
                elif opcao_pf == 0:
                        print("Voltando ao menu anterior")
                        break

                else:            
                    print("Opção inválida, por favor digíte uma das opções índicadas:")
                        
        elif opcao == 2:
                    print("Funcionalidade para pessoa jurídica não implementadas")
                    pass
            
        elif opcao == 0:
                    print("Obrigado por utilizar o nosso sistema!")
                    break

        else:
                    print("Opção inválida, por favor, digíte uma das opções inválidas!")

if __name__ == "__main__":
    main() # chama a função principal
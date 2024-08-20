from datetime import date

# CLASSE ENDEREÇO
class Endereco:
    def __init__(self, logradouro="", numero="", endereco_Comercial=False):
        # Inicializar os nossos atributos com valores padrão
        self.logradouro = logradouro
        self.numero = numero
        self.endereco_Comercial = endereco_Comercial

# CLASSE PESSOA
class Pessoa:
    def __init__(self, nome="", rendimento=0.0, endereco=None):
        self.nome = nome
        self.rendimento = rendimento
        self.endereco = endereco

    def calcular_imposto(self, rendimento):
        return rendimento


# CLASSE PESSOA FÍSICA
class PessoaFisica(Pessoa):
    # iniciar os atributos que foram herdados e próprios atributos da classe
    def __init__(self, nome="", rendimento=0.0, endereco=None, cpf="", dataNascimento=None):
        if endereco is None:
            # se nenhum endereço for fornecido, cria um bojeto Endereco padrão
            endereco = Endereco()

        if dataNascimento is None:
            dataNascimento = date.today()
            
        super().__init__(nome, rendimento, endereco)
        # chama o construtor da superclasse Pessoa para inicializar os atributos herdados

        # atributos da própria classe
        self.cpf = cpf
        self.dataNascimento = dataNascimento
    
    def calcular_imposto(self, rendimento: float) -> float:
        if rendimento <= 1500:
            return 0
        elif 1500 < rendimento <= 3500:
            return (rendimento / 100) * 2
        elif 3500 < rendimento <= 6000:
            return (rendimento / 100) * 3.5
        else:
            return rendimento * 0.5

# CLASSE PESSOA JURÍDICA
class PessoaJuridica(Pessoa):
    pass


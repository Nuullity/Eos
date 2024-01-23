import os
import random
import pyodbc
from datetime import datetime, timedelta

#--------------------------------------------------------------------------------------------------------------------------------
#variaveis



cargo = ['estagiario', 'aprendiz', 'operador', 'gerente']

salario=[1024,1320,1900,5200]


#--------------------------------------------------------------------------------------------------------------------------------


def Nomes(total):

    # Lista de nomes femininos
    nomes_femininos = [
    'Ana', 'Beatriz', 'Camila', 'Daniela', 'Eduarda', 'Fernanda', 'Gabriela', 'Helena', 'Isabela', 'Juliana',
    'Larissa', 'Mariana', 'Natália', 'Olivia', 'Patrícia', 'Renata', 'Sabrina', 'Tatiane', 'Ursula', 'Valentina',
    'Wanessa', 'Ximena', 'Yasmin', 'Zara', 'Bianca', 'Carolina', 'Diana', 'Elisa', 'Flávia', 'Gabrielle', 'Heloísa',
    'Isis', 'Júlia', 'Karina', 'Leticia', 'Mirella', 'Natalie', 'Oriana', 'Paula', 'Raquel', 'Simone', 'Tamara',
    'Ursulina', 'Vivian', 'Wendy', 'Xenia', 'Yara', 'Zuleica', 'Alessandra', 'Bárbara', 'Cristina', 'Dora', 'Elena',
    'Fabiana', 'Gisele', 'Hilda', 'Ivone', 'Joana', 'Kátia', 'Luciana', 'Márcia', 'Nina', 'Ornela', 'Priscila',
    'Quiteria', 'Rebeca', 'Samara', 'Talita', 'Umbelina', 'Vera', 'Waleska', 'Xuxa', 'Yolanda', 'Zélia', 'Amélia',
    'Belinda', 'Clarissa', 'Dulce', 'Eva', 'Fátima', 'Gloria', 'Hortência', 'Isidora', 'Jasmine', 'Karla', 'Luana',
    'Margarida', 'Neide', 'Ofélia', 'Penélope', 'Quitéria', 'Rafaela', 'Sofia', 'Teresa', 'Ursulina', 'Viviane',
    'Wanda', 'Xuxa', 'Yasmin', 'Zilda'
    ]

        # Lista de sobrenomes
    sobrenomes = [
        'Silva', 'Santos', 'Pereira', 'Oliveira', 'Rodrigues', 'Almeida', 'Costa', 'Lima', 'Gomes', 'Martins',
        'Venancio', 'Lacerda', 'Mendes', 'Ferreira', 'Barbosa', 'Rocha', 'Miranda', 'Castro', 'Fernandes', 'Souza',
        'Alves', 'Carvalho', 'Sampaio', 'Cardoso', 'Ribeiro', 'Marques', 'Moreira', 'Teixeira', 'Amaral', 'Dias', 'Monteiro',
        'Nunes', 'Pinto', 'Lima', 'Miranda', 'Mendes', 'Fernandes', 'Teixeira', 'Pereira', 'Ribeiro', 'Costa', 'Almeida',
        'Sampaio', 'Rodrigues', 'Barbosa', 'Venancio', 'Rocha', 'Gomes', 'Souza', 'Martins', 'Carvalho', 'Lacerda', 'Silva',
        'Alves', 'Oliveira', 'Dias', 'Moreira', 'Amaral', 'Cardoso', 'Ferreira', 'Monteiro', 'Lacerda', 'Teixeira',
        'Rocha', 'Santos', 'Castro', 'Marques', 'Alves', 'Barbosa', 'Fernandes', 'Rocha', 'Santos', 'Souza', 'Silva',
        'Venancio', 'Teixeira', 'Costa', 'Gomes', 'Lima', 'Nunes', 'Mendes', 'Carvalho', 'Almeida', 'Pereira', 'Ribeiro',
        'Miranda', 'Sampaio', 'Martins', 'Oliveira', 'Moreira', 'Ferreira', 'Pinto', 'Cardoso', 'Rodrigues', 'Amaral'
    ]
    # Lista de nomes masculinos
    nomes_masculinos = [
    'Arthur', 'Bernardo', 'Carlos', 'Daniel', 'Eduardo', 'Fábio', 'Gustavo', 'Henrique', 'Igor', 'João',
    'Lucas', 'Miguel', 'Nuno', 'Otávio', 'Pedro', 'Quintino', 'Rafael', 'Sérgio', 'Thiago', 'Ulisses',
    'Vicente', 'Wilian', 'Xavier', 'Yuri', 'Zélio', 'André', 'Benjamin', 'Cesar', 'David', 'Estevão',
    'Felipe', 'Gabriel', 'Heitor', 'Ivan', 'Joaquim', 'Kevin', 'Leandro', 'Matheus', 'Nathan', 'Oliver',
    'Paulo', 'Ricardo', 'Samuel', 'Tomás', 'Vinícius', 'William', 'Xande', 'Yago', 'Zacarias', 'Alexandre',
    'Breno', 'Carlos', 'Diego', 'Emanuel', 'Fernando', 'Giovanni', 'Hugo', 'Isaac', 'Júlio', 'Luciano',
    'Marco', 'Nícolas', 'Orlando', 'Pablo', 'Quirino', 'Raul', 'Simão', 'Teodoro', 'Marcos', 'Vitor',
    'Wesley', 'Xisto', 'Yago', 'Zacarias', 'Alfredo', 'Bruno', 'Cleber', 'Dante', 'Enzo', 'Fernando', 'Geraldo',
    'Higor', 'Ícaro', 'Jorge', 'Kaique', 'Levi', 'Mateus', 'Noah', 'Otto', 'Pietro', 'Quirino', 'Rodrigo',
    'Sérgio', 'Tomás', 'Umberto', 'Vanderlei', 'Walter', 'Xavier', 'Yan', 'Zélio'
    ]

    # Criação da lista final com 1600 nomes
    nomes = []


        
    qtdn_fem =  total // 2 # divide por 2 e separa o valor inteiro
    qtdn_masc = total - qtdn_fem # confere quantos nomes faltam ate o total definido e entao define o numero de nomes masculinos




    for _ in range(qtdn_fem):
        nome_completo = random.choice(nomes_femininos) + ' ' + random.choice(sobrenomes)
        nomes.append(nome_completo)

    for _ in range(qtdn_masc):
        nome_completo = random.choice(nomes_masculinos) + ' ' + random.choice(sobrenomes)
        nomes.append(nome_completo)

    # Embaralha a lista para misturar os nomes
    random.shuffle(nomes)
    return (nomes)

def Data_contratacao():
    # Data inicial
    data_inicial = datetime(2000, 1, 1)

    # Número de dias aleatórios a serem adicionados
    dias_aleatorios = random.randint(0, (datetime.now() - data_inicial).days)

    # Criação da data final
    data_final = data_inicial + timedelta(days=dias_aleatorios)

    data = (data_final.strftime('%d/%m/%Y'))
    return data

def cargo_salario():
    


    

    numero_aleatorio = random.randint(0,9)


 #estagiario
    if numero_aleatorio >= 0 and numero_aleatorio <= 1:  #estagiario
         C_S = 0
    elif  numero_aleatorio >= 2 and numero_aleatorio <=4:  #aprendiz
         C_S = 1
    elif  numero_aleatorio >= 5 and numero_aleatorio <=8:  #operador
         C_S = 2
    elif numero_aleatorio >=9:  #gerente
         C_S = 3
    
    return C_S

def gerar_cpf():
    # Gera os nove primeiros dígitos aleatórios
    cpf_base = [random.randint(0, 9) for _ in range(9)]

    # Calcula o primeiro dígito verificador
    primeiro_digito = calcular_digito_verificador(cpf_base)

    # Adiciona o primeiro dígito verificador aos nove primeiros dígitos
    cpf_base.append(primeiro_digito)

    # Calcula o segundo dígito verificador
    segundo_digito = calcular_digito_verificador(cpf_base)

    # Adiciona o segundo dígito verificador ao CPF completo
    cpf_base.append(segundo_digito)

    # Formata o CPF como string
    cpf_formatado = ''.join(map(str, cpf_base))

    return cpf_formatado

def calcular_digito_verificador(cpf_base):
    soma = 0
    peso = len(cpf_base) + 1

    for digito in cpf_base:
        soma += digito * peso
        peso -= 1

    resto = soma % 11
    digito_verificador = 11 - resto if resto > 1 else 0

    return digito_verificador

def Commit_Def():
   


   #altere com o nome ds tables que esta utilizando
    Comando = f"""
    INSERT INTO DADOS_FUNCIONARIOS (Nome, Data_Contratacao , Cargo , Salario, CPF ) 
    VALUES (
        
        '{nome[i]}', 
        '{data}',
        '{cargo[C_S]}',
         {salario[C_S]},
        '{cpf}'
    );
    """
    Cursor.execute(Comando)
    Conexao.commit()







Server = input("digite o nome de seu servidor (Caso seja Local, utilize o nome de sua maquina): ")
if Server == '1':
   Server = 'DESKTOP-HETLCUJ'
   #colocando o valor de minha maquina para que eu não precise digitar todas as vezes 
DB = input("digite o nome de seu Banco de dados: ")
if DB == '1':
   DB = 'DESTRUICAO'
   #colocando o valor de minha BD para que eu não precise digitar todas as vezes 
dados_conexao = (

    
        "Driver={SQL Server};"
        #Nome do server ( se for local será o nome da maquina)
        f"Server={Server};"
        #Nome da DB
        f"database={DB};"
)



total = int(input('quantos nomes deseja gerar ? '))
nome= Nomes(total)
data = Data_contratacao()




with pyodbc.connect(dados_conexao) as Conexao:             
    with Conexao.cursor() as Cursor:


        for i in range (0,total):
            os.system('cls')
            data = Data_contratacao()
            C_S = cargo_salario()
            cpf = gerar_cpf()
            Commit_Def()
            # i+1 ( indice inicia em 0, coloco +1 para que o valor fique correto na hora de printar)
            
            print(f'adicionado {i+1} de {total}, Feito {(i+1)*100/(total)}% ')


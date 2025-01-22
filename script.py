import os

# Pegando variáveis de ambiente
my_var = os.getenv('MY_VAR')

# Função para imprimir variáveis de ambiente
def print_env_vars():
    print('Environment Variables:')
    print(f'MY_VAR: {my_var}')

# Chamando a função
print_env_vars()

import os

# Pegando variáveis de ambiente
my_var = os.getenv('MY_VAR')
my_var2 = os.environ.get("MY_VAR")
my_var3 = os.environ.get("my_var")

# Função para imprimir variáveis de ambiente
def print_env_vars():
    print('Environment Variables:')
    print(f'MY_VAR:  {my_var}')
    print(f'MY_VAR2: {my_var2}')
    print(f'MY_VAR3: {my_var3}')

# Chamando a função
print_env_vars()

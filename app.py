from automacao_github.AutomacaoGithub import AutomacaoGithub

TOKEN = 'seu_tokem'

try:
    # Instanciando a classe.
    github = AutomacaoGithub('seu_token')

    # Lista repositórios.
    github.listar_repositorios()

    # Cria um novo repositório.
    # github.criar_repositorio('repositorio', 'Repositório de teste.')

    # Cria README.md no repositório recém criado
    # github.criar_readme('repositorio', '# README de Teste.')

    # Cria .gitignore padrão Python
    # github.criar_gitignore_python('repositorio')

    # Exclui o repositório (opcional)
    # github.excluir_repositorio('repositorio')

except RuntimeError as e:
    print(f"Ocorreu um erro: {e}")    




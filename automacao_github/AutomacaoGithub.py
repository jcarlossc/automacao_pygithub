from github import Github, GithubException

class AutomacaoGithub:
    """
    Classe responsável por automatizar operações no GitHub utilizando a API oficial através do módulo PyGithub.

    Métodos disponíveis:
        - listar_repositorios(): Lista os repositórios do usuário autenticado.
        - criar_repositorio(nome_repositorio, descricao): Cria um novo repositório público.
        - criar_readme(nome_repositorio, conteudo): Adiciona um arquivo README.md ao repositório.
        - criar_gitignore_python(nome_repositorio): Adiciona um arquivo .gitignore padrão para projetos Python.
        - excluir_repositorio(nome_repositorio): Exclui um repositório existente.

    Attributes:
        token (str): Token de autenticação pessoal (PAT) do GitHub.
        github_objeto (Github): Instância autenticada da API do GitHub.
        usuario (AuthenticatedUser): Usuário autenticado obtido pela API.

    Raises:
        RuntimeError: Caso ocorra falha na autenticação com o GitHub.
    """
    def __init__(self, TOKEN) -> None:
        self.token = TOKEN
        self.github_objeto = Github(TOKEN)
        try:
            self.usuario = self.github_objeto.get_user()
        except GithubException as e:    
            raise RuntimeError(f"Erro de autenticação: {e}")

    def listar_repositorios(self) -> None:    
        """ Lista todos os repositórios do usuário autenticado na plataforma GitHub.

        Raises:
            RuntimeError: Caso ocorra uma falha na comunicação com a API do GitHub
                      ou problema na autenticação ao tentar listar os repositórios.
        """
        try:
            for i, repositorio in enumerate(self.usuario.get_repos(), start = 1):
                print(f"{i}. {repositorio.name} | {'Privado' if repositorio.private else 'Público'} | {repositorio.html_url}")
        
        except GithubException as e:
            raise RuntimeError(f"Erro ao listar repositórios: {e}")

    def criar_repositorio(self, nome_repositorio: str, descricao: str) -> None:
        """ Este método cria um novo repositório público.

        Args:
            nome_repositorio (str): Nome do repositório a ser criado.
            descricao (str): Descrição do repositório.

        Raises:
            RuntimeError: Caso ocorra uma falha na comunicação com a API do GitHub
                      ou problema na autenticação ao tentar listar os repositórios.
        """
        try:
            novo_repositorio = self.usuario.create_repo(
                name = nome_repositorio,
                description = descricao,
                private = False
            )
            print(f"Repositório criado: {novo_repositorio.html_url}")

        except GithubException as e:
            raise RuntimeError(f"Erro ao criar repositório '{nome_repositorio}': {e}")    

    def criar_readme(self, nome_repositorio: str, conteudo: str) -> None:
        """ Este método cria um arquivo README no repositório.

        Args:
            nome_repositorio (str): Nome do repositório onde será criado o README.
            conteudo (str): Conteúdo o README.

        Raises:
            RuntimeError: Caso ocorra uma falha na comunicação com a API do GitHub
                      ou problema na autenticação ao tentar listar os repositórios.
        """
        try:
            repositorio = self.usuario.get_repo(nome_repositorio)
            content = conteudo
            repositorio.create_file("README.md", 'Adicionando README', content)
            print(f"Arquivo README criado com sucesso!")

        except GithubException as e:
            raise RuntimeError(f"Erro ao criar README.md em '{repositorio.name}': {e}")

    def criar_gitignore_python(self, nome_repositorio: str) -> None:  
        """ Este método cria um arquivo .gitignore no repositório.

        Args:
            nome_repositorio (str): Nome do repositório onde será criado o .gitignore.

        Raises:
            RuntimeError: Caso ocorra uma falha na comunicação com a API do GitHub
                      ou problema na autenticação ao tentar listar os repositórios.
        """
        try:
            repositorio = self.usuario.get_repo(nome_repositorio)   
            conteudo_gitignore = """
            # Byte-compiled / optimized / DLL files
            __pycache__/
            *.py[cod]
            *.so

            # Virtual environment
            venv/
            env/

            # VS Code
            .vscode/
            """
            repositorio.create_file(
                path=".gitignore",
                message="Adiciona arquivo .gitignore padrão para Python",
                content=conteudo_gitignore,
                branch="main"
            )

            print("Aquivo .gitignore criado com sucesso")

        except GithubException as e:
            raise RuntimeError(f"Erro ao criar .gitignore em '{repositorio.name}': {e}")

    def excluir_repositorio(self, nome_repositorio: str) -> None:   
        """ Este método exclui um repositório espedífico.

        Args:
            nome_repositorio (str): Nome do repositório a ser excluído.

        Raises:
            RuntimeError: Caso ocorra uma falha na comunicação com a API do GitHub
                      ou problema na autenticação ao tentar listar os repositórios.
        """
        try:
            repositorio = self.usuario.get_repo(nome_repositorio)
            repositorio.delete()
            print("Repositório excluído com sucesso!")    

        except GithubException as e:
            raise RuntimeError(f"Erro ao excluir repositório '{nome_repositorio}': {e}")
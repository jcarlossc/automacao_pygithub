from github import Github, GithubException

class AutomacaoGithub:
    
    def __init__(self, TOKEN) -> None:
        self.token = TOKEN
        self.github_objeto = Github(TOKEN)
        try:
            self.usuario = self.github_objeto.get_user()
        except GithubException as e:    
            raise RuntimeError(f"Erro de autenticação: {e}")

    def listar_repositorios(self) -> None:    
        try:
            for i, repositorio in enumerate(self.usuario.get_repos(), start = 1):
                print(f"{i}. {repositorio.name} | {'Privado' if repositorio.private else 'Público'} | {repositorio.html_url}")
        
        except GithubException as e:
            raise RuntimeError(f"Erro ao listar repositórios: {e}")

    def criar_repositorio(self, nome_repositorio: str, descricao: str) -> None:
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
        try:
            repositorio = self.usuario.get_repo(nome_repositorio)
            content = conteudo
            repositorio.create_file("README.md", 'Adicionando README', content)
            print(f"Arquivo README criado com sucesso!")

        except GithubException as e:
            raise RuntimeError(f"Erro ao criar README.md em '{repositorio.name}': {e}")

    def criar_gitignore_python(self, nome_repositorio: str) -> None:  
        usuario = self.github_objeto.get_user()
        repositorio = usuario.get_repo(nome_repositorio)   
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

    def excluir_repositorio(self, nome_repositorio: str) -> None:   
        usuario = self.github_objeto.get_user()
        repositorio = usuario.get_repo(nome_repositorio)
        repositorio.delete()
        print("Repositório excluído com sucesso!")      
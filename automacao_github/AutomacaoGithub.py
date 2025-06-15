from github import Github

class AutomacaoGithub:
    
    def __init__(self, TOKEN) -> None:
        self.token = TOKEN
        self.github_objeto = Github(TOKEN)

    def listar_repositorios(self) -> None:    
        usuario = self.github_objeto.get_user()
        for i, repositorio in enumerate(usuario.get_repos(), start = 1):
            print(f"{i}. {repositorio.name} | {'Privado' if repositorio.private else 'Público'} | {repositorio.html_url}")

    def criar_repositorio(self, nome: str, descricao: str) -> None:
        usuario = self.github_objeto.get_user()
        novo_repositorio = usuario.create_repo(
            name = nome,
            description = descricao,
            private = False
        )
        print(f"Repositório criado: {novo_repositorio.html_url}")

    def criar_readme(self, nome_repositorio: str, conteudo: str) -> None:
        usuario = self.github_objeto.get_user()
        repositorio = usuario.get_repo(nome_repositorio)
        content = conteudo
        repositorio.create_file("README.md", 'Adicionando README', content)
        print(f"Arquivo README criado com sucesso!")

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

        print("Repositório criado com .gitignore!")
from automacao_github.AutomacaoGithub import AutomacaoGithub

github = AutomacaoGithub()
#github.excluir_repositorio('repositorio')
# github.criar_gitignore_python('repositorio')
github.criar_readme('repositorio', '# README de Teste.')
# github.criar_repositorio('repositorio', 'Repositório de teste.')
# github.listar_repositorios()
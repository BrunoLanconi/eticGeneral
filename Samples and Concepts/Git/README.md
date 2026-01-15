# Git - Comandos Principais

## Configuração Inicial

### Configurar identidade do usuário
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@example.com"
```

### Verificar configurações
```bash
git config --list
git config user.name
git config user.email
```

### Inicializar repositório
```bash
git init
```

### Clonar repositório existente
```bash
git clone <url-do-repositorio>
git clone <url-do-repositorio> <nome-do-diretorio>
```

---

## Comandos Básicos

### Verificar status dos arquivos
```bash
git status
git status -s  # Formato curto
```

### Adicionar arquivos ao staging area
```bash
git add <arquivo>
git add .                    # Adiciona todos os arquivos
git add *.js                 # Adiciona todos os arquivos .js
git add -A                   # Adiciona todos (incluindo deletados)
```

### Fazer commit
```bash
git commit -m "Mensagem do commit"
git commit -am "Mensagem"    # Add e commit juntos (apenas arquivos tracked)
git commit --amend           # Corrigir último commit
```

### Remover arquivos
```bash
git rm <arquivo>             # Remove do working directory e staging
git rm --cached <arquivo>    # Remove apenas do staging
```

### Mover/Renomear arquivos
```bash
git mv <arquivo-antigo> <arquivo-novo>
```

### Ver diferenças
```bash
git diff                     # Diferenças não staged
git diff --staged            # Diferenças staged
git diff HEAD                # Todas as diferenças
git diff <branch1> <branch2> # Diferenças entre branches
```

---

## Branches

### Listar branches
```bash
git branch                   # Branches locais
git branch -r                # Branches remotas
git branch -a                # Todas as branches
```

### Criar branch
```bash
git branch <nome-da-branch>
```

### Mudar de branch
```bash
git checkout <nome-da-branch>
git switch <nome-da-branch>  # Comando mais novo
```

### Criar e mudar para nova branch
```bash
git checkout -b <nome-da-branch>
git switch -c <nome-da-branch>
```

### Deletar branch
```bash
git branch -d <nome-da-branch>   # Deleta apenas se merged
git branch -D <nome-da-branch>   # Força deleção
```

### Renomear branch
```bash
git branch -m <novo-nome>        # Renomeia branch atual
git branch -m <antigo> <novo>    # Renomeia outra branch
```

---

## Merge e Rebase

### Fazer merge
```bash
git merge <nome-da-branch>
git merge --no-ff <branch>   # Força commit de merge
git merge --squash <branch>  # Combina commits em um
```

### Rebase
```bash
git rebase <branch>
git rebase -i HEAD~3         # Rebase interativo dos últimos 3 commits
git rebase --continue        # Continuar após resolver conflitos
git rebase --abort           # Cancelar rebase
```

### Resolver conflitos
```bash
# 1. Editar arquivos em conflito
# 2. Adicionar arquivos resolvidos
git add <arquivo>
# 3. Continuar merge/rebase
git merge --continue
git rebase --continue
```

---

## Stash

### Guardar alterações temporariamente
```bash
git stash
git stash save "Mensagem"
git stash -u                 # Inclui arquivos untracked
```

### Listar stashes
```bash
git stash list
```

### Aplicar stash
```bash
git stash apply              # Aplica último stash
git stash apply stash@{2}    # Aplica stash específico
git stash pop                # Aplica e remove da lista
```

### Remover stash
```bash
git stash drop stash@{0}     # Remove stash específico
git stash clear              # Remove todos os stashes
```

### Ver conteúdo do stash
```bash
git stash show
git stash show -p            # Mostra diff completo
```

---

## Histórico e Logs

### Ver histórico de commits
```bash
git log
git log --oneline            # Formato resumido
git log --graph              # Mostra árvore de branches
git log --all --graph        # Todas as branches
git log -n 5                 # Últimos 5 commits
git log --author="Nome"      # Commits de um autor
git log --since="2 weeks ago"
git log --until="2023-12-31"
```

### Ver histórico de um arquivo
```bash
git log <arquivo>
git log -p <arquivo>         # Com diferenças
git blame <arquivo>          # Quem alterou cada linha
```

### Ver detalhes de um commit
```bash
git show <commit-hash>
git show HEAD                # Último commit
git show HEAD~2              # Commit 2 atrás do HEAD
```

---

## Desfazer Alterações

### Desfazer alterações em arquivo (não staged)
```bash
git checkout -- <arquivo>
git restore <arquivo>        # Comando mais novo
```

### Remover arquivo do staging
```bash
git reset HEAD <arquivo>
git restore --staged <arquivo>
```

### Desfazer commits
```bash
git reset --soft HEAD~1      # Mantém alterações staged
git reset --mixed HEAD~1     # Mantém alterações não staged (padrão)
git reset --hard HEAD~1      # Descarta todas as alterações
```

### Reverter commit (cria novo commit)
```bash
git revert <commit-hash>
git revert HEAD              # Reverte último commit
```

---

## Remoto

### Adicionar remoto
```bash
git remote add origin <url>
```

### Listar remotos
```bash
git remote
git remote -v                # Mostra URLs
git remote show origin       # Detalhes do remoto
```

### Renomear/Remover remoto
```bash
git remote rename origin novo-nome
git remote remove origin
```

### Buscar alterações
```bash
git fetch                    # Busca de todos os remotos
git fetch origin             # Busca de remoto específico
```

### Baixar e integrar alterações
```bash
git pull                     # fetch + merge
git pull --rebase            # fetch + rebase
git pull origin main
```

### Enviar alterações
```bash
git push
git push origin main
git push -u origin main      # Define upstream
git push --all               # Todas as branches
git push --tags              # Todas as tags
git push --force             # Força push (cuidado!)
```

---

## Tags

### Criar tag
```bash
git tag v1.0.0
git tag -a v1.0.0 -m "Versão 1.0.0"  # Tag anotada
git tag v1.0.0 <commit-hash>         # Tag em commit específico
```

### Listar tags
```bash
git tag
git tag -l "v1.*"            # Tags que começam com v1.
```

### Ver informações da tag
```bash
git show v1.0.0
```

### Deletar tag
```bash
git tag -d v1.0.0            # Local
git push origin --delete v1.0.0  # Remota
```

### Enviar tags
```bash
git push origin v1.0.0       # Tag específica
git push origin --tags       # Todas as tags
```

---

## Boas Práticas

### Mensagens de Commit
- Use mensagens claras e descritivas
- Primeira linha: resumo (máximo 50 caracteres)
- Linha em branco
- Descrição detalhada (se necessário)

```
feat: adiciona funcionalidade de login

- Implementa autenticação JWT
- Adiciona validação de credenciais
- Cria middleware de autorização
```

### Convenções de Commit
```
feat:     Nova funcionalidade
fix:      Correção de bug
docs:     Documentação
style:    Formatação
refactor: Refatoração de código
test:     Testes
chore:    Manutenção
```

### Workflow Básico
```bash
# 1. Atualizar branch principal
git checkout main
git pull origin main

# 2. Criar branch de feature
git checkout -b feature/nova-funcionalidade

# 3. Fazer alterações e commits
git add .
git commit -m "feat: implementa nova funcionalidade"

# 4. Atualizar com main
git checkout main
git pull origin main
git checkout feature/nova-funcionalidade
git rebase main

# 5. Enviar para remoto
git push origin feature/nova-funcionalidade

# 6. Criar Pull Request no GitHub/GitLab
```

### .gitignore
Exemplo de arquivo `.gitignore`:
```
# Node
node_modules/
npm-debug.log
.env

# Python
__pycache__/
*.pyc
.venv/
venv/

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Build
dist/
build/
*.log
```

---

## Comandos Úteis

### Limpar arquivos não tracked
```bash
git clean -n                 # Preview
git clean -f                 # Remove arquivos
git clean -fd                # Remove arquivos e diretórios
```

### Encontrar bugs com bisect
```bash
git bisect start
git bisect bad               # Marca commit atual como ruim
git bisect good <commit>     # Marca commit bom
# Testar e marcar como good/bad até encontrar o problema
git bisect reset             # Finalizar
```

### Cherry-pick (aplicar commit específico)
```bash
git cherry-pick <commit-hash>
```

### Ver quem fez cada alteração
```bash
git blame <arquivo>
git blame -L 10,20 <arquivo> # Linhas específicas
```

### Reflog (histórico de referências)
```bash
git reflog                   # Ver histórico de HEAD
git reflog show <branch>     # Histórico de uma branch
```

---

## Atalhos e Aliases

### Criar aliases
```bash
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.lg "log --oneline --graph --all"
```

### Usar aliases
```bash
git co main
git st
git lg
```

# Guia Git para Windows: Instalacao e Uso Completo

## Objetivo
Este guia ensina como baixar, instalar e usar Git no Windows do zero ate o uso avancado.

---

## Passo 1: Download e Instalacao

### 1.1 Baixar o Git
1. Acesse: **https://git-scm.com/download/win**
2. O download comecara automaticamente
3. Escolha a versao:
   - **64-bit Git for Windows Setup** (recomendado para PCs modernos)
   - **32-bit Git for Windows Setup** (para PCs antigos)

### 1.2 Instalar o Git
1. **Execute o arquivo baixado** (Git-2.x.x-64-bit.exe)
2. **Aceite a licenca** → Clique "Next"
3. **Escolha o diretorio** → Deixe padrao ou mude → "Next"
4. **Selecione componentes:**
   - [x] Windows Explorer integration
   - [x] Git Bash Here
   - [x] Git GUI Here
   - [x] Git LFS (Large File Support)
   - [x] Associate .git* configuration files
   - [x] Associate .sh files to be run with Bash
5. **Menu Iniciar** → Deixe padrao → "Next"
6. **Editor padrao** → Escolha "Visual Studio Code" ou "Notepad++"
7. **Nome da branch inicial** → Escolha "Let Git decide"
8. **PATH environment** → Escolha "Git from the command line and also from 3rd-party software"
9. **SSH executable** → Deixe "Use bundled OpenSSH"
10. **HTTPS transport backend** → Deixe "Use the OpenSSL library"
11. **Line ending conversions** → "Checkout Windows-style, commit Unix-style line endings"
12. **Terminal emulator** → "Use MinTTY (the default terminal of MSYS2)"
13. **Comportamento git pull** → "Default (fast-forward or merge)"
14. **Credential helper** → "Git Credential Manager"
15. **Configuracoes extras:**
    - [x] Enable file system caching
    - [x] Enable symbolic links
16. **Clique "Install"** e aguarde
17. **Clique "Finish"**

---

## Passo 2: Configuracao Inicial

### 2.1 Abrir Git Bash
- **Clique com botao direito** em qualquer pasta
- Selecione **"Git Bash Here"**
- Ou abra pelo Menu Iniciar: **"Git Bash"**

### 2.2 Configurar Usuario
```bash
# Configure seu nome (obrigatorio)
git config --global user.name "Seu Nome Completo"

# Configure seu email (obrigatorio)
git config --global user.email "seu.email@exemplo.com"

# Configure editor padrao (opcional)
git config --global core.editor "code --wait"
```

### 2.3 Verificar Configuracao
```bash
# Ver todas as configuracoes
git config --list

# Ver configuracoes especificas
git config user.name
git config user.email
```

---

## Passo 3: Criando Primeiro Repositorio

### 3.1 Criar Pasta do Projeto
```bash
# Navegar para onde quer criar o projeto
cd C:/Users/SeuUsuario/Documents

# Criar pasta do projeto
mkdir meu-primeiro-projeto

# Entrar na pasta
cd meu-primeiro-projeto
```

### 3.2 Inicializar Git
```bash
# Inicializar repositorio Git
git init

# Verificar status
git status
```

### 3.3 Criar Primeiro Arquivo
```bash
# Criar arquivo README
echo "# Meu Primeiro Projeto" > README.md

# Ver o que foi criado
git status
```

### 3.4 Fazer Primeiro Commit
```bash
# Adicionar arquivo ao controle de versao
git add README.md

# Ou adicionar todos os arquivos
git add .

# Fazer commit
git commit -m "Primeiro commit: adiciona README"

# Ver historico
git log --oneline
```

---

## Passo 4: Conectando com GitHub

### 4.1 Criar Conta no GitHub
1. Acesse: **https://github.com**
2. Clique **"Sign up"**
3. Preencha: **username**, **email**, **senha**
4. Verifique email e complete cadastro

### 4.2 Criar Repositorio no GitHub
1. Faca login no GitHub
2. Clique **"+"** no canto superior direito
3. Selecione **"New repository"**
4. Preencha:
   - **Repository name:** meu-primeiro-projeto
   - **Description:** Meu primeiro projeto Git
   - **Public** (ou Private se preferir)
   - Nao marque **Add a README file** (ja temos um)
5. Clique **"Create repository"**

### 4.3 Conectar Repositorio Local ao GitHub
```bash
# Adicionar origem remota
git remote add origin https://github.com/SEU_USUARIO/meu-primeiro-projeto.git

# Verificar conexao
git remote -v

# Enviar codigo para GitHub
git push -u origin main
```

### 4.4 Configurar Autenticacao (Token)
1. **GitHub** → **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. **Generate new token (classic)**
3. **Expiration:** 90 days
4. **Scopes:**
   - [x] repo (Full control of private repositories)
   - [x] workflow
5. **Generate token** → **COPIE E GUARDE O TOKEN**
6. **No Git Bash:** Use o token como senha quando pedir

---

## Passo 5: Comandos Essenciais do Dia a Dia

### 5.1 Verificacao de Status
```bash
# Ver status dos arquivos
git status

# Ver diferencas nao commitadas
git diff

# Ver historico de commits
git log --oneline -10
```

### 5.2 Adicionando e Commitando
```bash
# Adicionar arquivo especifico
git add arquivo.txt

# Adicionar todos os arquivos modificados
git add .

# Adicionar apenas arquivos ja rastreados
git add -u

# Fazer commit
git commit -m "Descricao clara das mudancas"

# Adicionar e commitar em um comando
git commit -am "Mensagem do commit"
```

### 5.3 Sincronizacao com Repositorio Remoto
```bash
# Baixar mudancas do repositorio remoto
git pull origin main

# Enviar mudancas para repositorio remoto
git push origin main

# Ver repositorios remotos
git remote -v
```

### 5.4 Trabalhando com Branches
```bash
# Ver branches existentes
git branch

# Criar nova branch
git branch nova-funcionalidade

# Mudar para outra branch
git checkout nova-funcionalidade

# Criar e mudar para nova branch
git checkout -b outra-funcionalidade

# Voltar para branch main
git checkout main

# Fazer merge de branch
git merge nova-funcionalidade

# Deletar branch local
git branch -d nova-funcionalidade
```

---

## Passo 6: Resolvendo Problemas Comuns

### 6.1 Esqueceu de Fazer Pull
```bash
# Se tiver mudancas locais nao commitadas
git stash
git pull origin main
git stash pop
```

### 6.2 Conflitos de Merge
1. **Git mostrara os arquivos em conflito**
2. **Abra os arquivos no editor**
3. **Procure por marcadores:**
   ```
   <<<<<<< HEAD
   Seu codigo local
   =======
   Codigo do repositorio remoto
   >>>>>>> origin/main
   ```
4. **Escolha qual codigo manter**
5. **Remova os marcadores**
6. **Salve o arquivo**
7. **Execute:**
   ```bash
   git add arquivo-resolvido.txt
   git commit -m "Resolve conflito de merge"
   ```

### 6.3 Desfazer Mudancas
```bash
# Desfazer mudancas nao commitadas em arquivo especifico
git checkout -- arquivo.txt

# Desfazer todas as mudancas nao commitadas
git checkout -- .

# Desfazer ultimo commit (mantem mudancas)
git reset --soft HEAD~1

# Desfazer ultimo commit (remove mudancas)
git reset --hard HEAD~1
```

### 6.4 Erro de Autenticacao
```bash
# Configurar credenciais novamente
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@exemplo.com"

# Limpar credenciais salvas
git config --global --unset credential.helper
```

---

## Passo 7: Ferramentas Adicionais

### 7.1 Git GUI (Interface Grafica)
- **Abrir:** Clique direito na pasta → "Git GUI Here"
- **Ou:** Digite `git gui` no Git Bash
- **Funcionalidades:**
  - Visualizar mudancas
  - Fazer commits
  - Ver historico
  - Gerenciar branches

### 7.2 GitK (Visualizador de Historico)
```bash
# Abrir visualizador de historico
gitk

# Ver todas as branches
gitk --all
```

### 7.3 Extensoes para VS Code
Se usar VS Code, instale:
- **GitLens** - Historico e blame
- **Git Graph** - Visualizacao grafica
- **Git History** - Historico detalhado

---

## Passo 8: Workflow Recomendado

### 8.1 Inicio do Trabalho
```bash
# 1. Abra Git Bash na pasta do projeto
# 2. Atualize o repositorio
git pull origin main

# 3. Verifique status
git status
```

### 8.2 Durante o Trabalho
```bash
# 1. Faca suas modificacoes nos arquivos
# 2. Verifique o que mudou
git status
git diff

# 3. Adicione as mudancas
git add .

# 4. Faca commit frequente
git commit -m "Descricao clara das mudancas"
```

### 8.3 Final do Trabalho
```bash
# 1. Envie as mudancas para GitHub
git push origin main

# 2. Verifique se foi enviado corretamente
git status
```

---

## Comandos Uteis Avancados

### Configuracoes Uteis
```bash
# Configurar para nao pedir senha sempre (Windows)
git config --global credential.helper manager

# Configurar cores no terminal
git config --global color.ui auto

# Configurar aliases uteis
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.cm commit
```

### Informacoes do Repositorio
```bash
# Ver informacoes detalhadas do repositorio
git remote show origin

# Ver diferencas entre branches
git diff main..outra-branch

# Ver arquivos modificados entre commits
git diff --name-only HEAD~1 HEAD
```

---

## Solucoes para Erros Comuns

| Erro | Solucao |
|------|---------|
| "fatal: not a git repository" | Execute `git init` na pasta do projeto |
| "Permission denied (publickey)" | Configure token de acesso do GitHub |
| "Your local changes would be overwritten" | Execute `git stash` antes do `git pull` |
| "Merge conflict" | Resolva manualmente e faca novo commit |
| "fatal: remote origin already exists" | Use `git remote set-url origin URL` |

---

## Checklist de Instalacao

- [ ] Git baixado e instalado
- [ ] Git Bash funcionando
- [ ] Usuario configurado (`git config user.name` e `user.email`)
- [ ] Conta GitHub criada
- [ ] Token de acesso configurado
- [ ] Primeiro repositorio criado e sincronizado
- [ ] Comandos basicos testados

---

## Proximos Passos

1. **Pratique** os comandos basicos diariamente
2. **Crie** mais projetos e repositorios
3. **Explore** branches para funcionalidades diferentes
4. **Colabore** com outros desenvolvedores
5. **Aprenda** sobre Git Flow e workflows avancados

---

*Criado em: 30 de Setembro de 2025*  
*Guia para iniciantes em Git no Windows*  
*Autor: Carlos G. Santos*
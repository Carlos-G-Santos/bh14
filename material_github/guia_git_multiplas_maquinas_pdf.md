# Guia Git: Trabalho em Multiplas Maquinas

## Objetivo
Este guia ensina como trabalhar com Git em multiplas maquinas sem conflitos de versao.

---

## Fluxo Basico (REGRA DE OURO)

### SEMPRE Antes de Comecar a Trabalhar:
```bash
git pull origin main
```

### Durante o Trabalho:
```bash
# Faca commits pequenos e frequentes:
git add .
git commit -m "Descricao clara do que mudou"
```

### SEMPRE Antes de Sair da Maquina:
```bash
git push origin main
```

---

## Protocolo Detalhado

### Maquina A (Casa):
1. **`git pull origin main`** <- **SEMPRE primeiro**
2. Trabalhe nos arquivos
3. **`git add .`**
4. **`git commit -m "Mudancas feitas em casa"`**
5. **`git push origin main`** <- **SEMPRE antes de sair**

### Maquina B (Trabalho):
1. **`git pull origin main`** <- **SEMPRE primeiro**
2. Trabalhe nos arquivos  
3. **`git add .`**
4. **`git commit -m "Mudancas feitas no trabalho"`**
5. **`git push origin main`** <- **SEMPRE antes de sair**

---

## Resolucao de Conflitos

### Se Esqueceu de Fazer Pull:
```bash
git stash                    # Guarda suas mudancas
git pull origin main         # Atualiza o repositorio
git stash pop               # Recupera suas mudancas
# Resolve conflitos se houver
git add .
git commit -m "Resolvendo conflitos"
git push origin main
```

### Se Deu Conflito no Push:
```bash
git pull origin main        # Tenta fazer merge automatico
# Se der conflito, resolve manualmente nos arquivos
git add .
git commit -m "Merge resolvido"
git push origin main
```

### Como Identificar Conflitos:
Os conflitos aparecem nos arquivos com estas marcacoes:
```
<<<<<<< HEAD
Seu codigo local
=======
Codigo do repositorio remoto
>>>>>>> branch-name
```

**Resolucao:**
1. Escolha qual codigo manter
2. Remova as marcacoes `<<<<<<<`, `=======`, `>>>>>>>`
3. Salve o arquivo
4. Execute: `git add .` e `git commit -m "Conflito resolvido"`

---

## Configuracoes Recomendadas

### Configurar Pull com Rebase:
```bash
git config --global pull.rebase true
```

### Configurar Merge Strategy:
```bash
git config --global pull.ff only
```

### Ver Configuracoes Atuais:
```bash
git config --list
```

---

## Comandos Uteis de Verificacao

### Ver Status do Repositorio:
```bash
git status
```

### Ver Historico de Commits:
```bash
git log --oneline -10
```

### Ver Diferencas Nao Commitadas:
```bash
git diff
```

### Ver Branches Remotas:
```bash
git branch -a
```

### Verificar Origem Remota:
```bash
git remote -v
```

---

## Comandos de Emergencia

### Desfazer Ultimo Commit (Mantem Mudancas):
```bash
git reset --soft HEAD~1
```

### Desfazer Mudancas Nao Commitadas:
```bash
git checkout -- <arquivo>
# ou para todos os arquivos:
git checkout -- .
```

### Voltar para um Commit Especifico:
```bash
git checkout <hash-do-commit>
# Para voltar ao estado atual:
git checkout main
```

### Cancelar Merge em Progresso:
```bash
git merge --abort
```

---

## Dicas de Boas Praticas

### Mensagens de Commit:
- **Bom:** "Adiciona funcao de plotagem de dose"
- **Ruim:** "mudancas"

### Frequencia de Commits:
- Faca commits a cada mudanca significativa
- Nao acumule muitas alteracoes em um commit

### Organizacao:
- Mantenha arquivos grandes fora do repositorio
- Use `.gitignore` para arquivos temporarios

### Sincronizacao:
- **NUNCA** saia da maquina sem fazer `git push`
- **SEMPRE** comece o trabalho com `git pull`

---

## Solucao de Problemas Comuns

| Problema | Comando | Descricao |
|----------|---------|-----------|
| Esqueci de fazer pull | `git stash && git pull && git stash pop` | Salva mudancas, atualiza, restaura |
| Conflito de merge | Editar arquivo -> `git add .` -> `git commit` | Resolve manualmente |
| Push rejeitado | `git pull origin main` -> resolver conflitos | Atualiza e resolve |
| Mudancas indesejadas | `git checkout -- .` | Desfaz mudancas nao commitadas |

---

## Checklist Diario

### Ao Comecar o Trabalho:
- [ ] `git status` (verificar estado)
- [ ] `git pull origin main` (atualizar)
- [ ] Verificar se nao ha conflitos

### Ao Terminar o Trabalho:
- [ ] `git add .` (adicionar mudancas)
- [ ] `git commit -m "Descricao clara"` (salvar)
- [ ] `git push origin main` (enviar)
- [ ] Verificar se o push foi bem-sucedido

---

*Criado em: 30 de Setembro de 2025*  
*Projeto: bh14*  
*Autor: Carlos G. Santos*
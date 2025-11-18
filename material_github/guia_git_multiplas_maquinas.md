# 📋 Guia Git: Trabalho em Múltiplas Máquinas

## 🎯 Objetivo
Este guia ensina como trabalhar com Git em múltiplas máquinas sem conflitos de versão.

---

## 🔄 Fluxo Básico (REGRA DE OURO)

### ✅ SEMPRE Antes de Começar a Trabalhar:
```bash
git pull origin main
```

### 💾 Durante o Trabalho:
```bash
# Faça commits pequenos e frequentes:
git add .
git commit -m "Descrição clara do que mudou"
```

### 🚀 SEMPRE Antes de Sair da Máquina:
```bash
git push origin main
```

---

## 📍 Protocolo Detalhado

### 🏠 Máquina A (Casa):
1. **`git pull origin main`** ← **SEMPRE primeiro**
2. Trabalhe nos arquivos
3. **`git add .`**
4. **`git commit -m "Mudanças feitas em casa"`**
5. **`git push origin main`** ← **SEMPRE antes de sair**

### 🏢 Máquina B (Trabalho):
1. **`git pull origin main`** ← **SEMPRE primeiro**
2. Trabalhe nos arquivos  
3. **`git add .`**
4. **`git commit -m "Mudanças feitas no trabalho"`**
5. **`git push origin main`** ← **SEMPRE antes de sair**

---

## ⚠️ Resolução de Conflitos

### 🔧 Se Esqueceu de Fazer Pull:
```bash
git stash                    # Guarda suas mudanças
git pull origin main         # Atualiza o repositório
git stash pop               # Recupera suas mudanças
# Resolve conflitos se houver
git add .
git commit -m "Resolvendo conflitos"
git push origin main
```

### 💥 Se Deu Conflito no Push:
```bash
git pull origin main        # Tenta fazer merge automático
# Se der conflito, resolve manualmente nos arquivos
git add .
git commit -m "Merge resolvido"
git push origin main
```

### 🔍 Como Identificar Conflitos:
Os conflitos aparecem nos arquivos com estas marcações:
```
<<<<<<< HEAD
Seu código local
=======
Código do repositório remoto
>>>>>>> branch-name
```

**Resolução:**
1. Escolha qual código manter
2. Remova as marcações `<<<<<<<`, `=======`, `>>>>>>>`
3. Salve o arquivo
4. Execute: `git add .` e `git commit -m "Conflito resolvido"`

---

## 🛡️ Configurações Recomendadas

### Configurar Pull com Rebase:
```bash
git config --global pull.rebase true
```

### Configurar Merge Strategy:
```bash
git config --global pull.ff only
```

### Ver Configurações Atuais:
```bash
git config --list
```

---

## 📚 Comandos Úteis de Verificação

### Ver Status do Repositório:
```bash
git status
```

### Ver Histórico de Commits:
```bash
git log --oneline -10
```

### Ver Diferenças Não Commitadas:
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

## 🚨 Comandos de Emergência

### Desfazer Último Commit (Mantém Mudanças):
```bash
git reset --soft HEAD~1
```

### Desfazer Mudanças Não Commitadas:
```bash
git checkout -- <arquivo>
# ou para todos os arquivos:
git checkout -- .
```

### Voltar para um Commit Específico:
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

## ✨ Dicas de Boas Práticas

### 📝 Mensagens de Commit:
- **Bom:** "Adiciona função de plotagem de dose"
- **Ruim:** "mudanças"

### 🕒 Frequência de Commits:
- Faça commits a cada mudança significativa
- Não acumule muitas alterações em um commit

### 📂 Organização:
- Mantenha arquivos grandes fora do repositório
- Use `.gitignore` para arquivos temporários

### 🔄 Sincronização:
- **NUNCA** saia da máquina sem fazer `git push`
- **SEMPRE** comece o trabalho com `git pull`

---

## 📞 Solução de Problemas Comuns

| Problema | Comando | Descrição |
|----------|---------|-----------|
| Esqueci de fazer pull | `git stash && git pull && git stash pop` | Salva mudanças, atualiza, restaura |
| Conflito de merge | Editar arquivo → `git add .` → `git commit` | Resolve manualmente |
| Push rejeitado | `git pull origin main` → resolver conflitos | Atualiza e resolve |
| Mudanças indesejadas | `git checkout -- .` | Desfaz mudanças não commitadas |

---

## 📋 Checklist Diário

### 🌅 Ao Começar o Trabalho:
- [ ] `git status` (verificar estado)
- [ ] `git pull origin main` (atualizar)
- [ ] Verificar se não há conflitos

### 🌙 Ao Terminar o Trabalho:
- [ ] `git add .` (adicionar mudanças)
- [ ] `git commit -m "Descrição clara"` (salvar)
- [ ] `git push origin main` (enviar)
- [ ] Verificar se o push foi bem-sucedido

---

*Criado em: 30 de Setembro de 2025*  
*Projeto: bh14*  
*Autor: Carlos G. Santos*
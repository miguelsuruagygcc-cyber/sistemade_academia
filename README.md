# 🏋️ Sistema de Academia

Sistema de terminal em Python para gerenciar uma academia: cadastro de alunos, divisão por grupos de treino, fila de avaliação física e montagem de treinos.

O objetivo do projeto é praticar **estruturas de dados implementadas do zero**, sem usar as estruturas prontas do Python (como `list.append` ou `collections.deque`) na lógica principal.

## ✨ Funcionalidades

**Alunos**
- Cadastrar aluno no fim da lista ou numa posição específica
- Remover aluno por matrícula, o primeiro ou o último
- Buscar aluno por matrícula
- Listar todos os alunos
- Ver quantos alunos há em cada grupo de treino (A a E), com um gráfico de barras no terminal

**Fila de avaliação física**
- Colocar aluno na fila
- Chamar o próximo da fila
- Ver a fila de espera

**Montagem de treino**
- Adicionar exercício ao treino
- Desfazer o último exercício adicionado
- Ver o treino montado

## 🧠 Estruturas de dados usadas

| Estrutura | Classe | Onde é usada |
|---|---|---|
| **Vetor** (tamanho fixo) | `Vetor` | Contador de alunos por grupo de treino |
| **Lista encadeada** | `ListaEncadeadaAlunos` | Cadastro de alunos (inserir, remover, buscar) |
| **Fila** (FIFO) | `FilaAvaliacao` | Fila de espera da avaliação física: quem chega primeiro é atendido primeiro |
| **Pilha** (LIFO) | `PilhaTreino` | Montagem do treino: o "desfazer" remove o último exercício adicionado |

## ▶️ Como executar

Você só precisa ter o **Python 3** instalado. O projeto não usa nenhuma biblioteca externa.

```bash
git clone https://github.com/miguelsuruagygcc-cyber/sistemade_academia.git
cd sistemade_academia
python sistema_academia.py
```

## 🖥️ Exemplo de uso

```
============================================================
  ACADEMIA - DIVISAO DE ALUNOS E TREINOS PERSONALIZADOS
============================================================
   1 - Cadastrar aluno (no fim)
   2 - Cadastrar aluno em uma posicao
   ...
  14 - Ver treino montado
   0 - Sair

  Escolha uma opcao: 8

============================================================
  DIVISAO DE ALUNOS POR GRUPO
============================================================
  Grupo A:  3  ###
  Grupo B:  1  #
  Grupo C:  0
  Grupo D:  2  ##
  Grupo E:  0
```

## 🚀 Próximos passos

- [ ] Salvar os dados num arquivo para não perder ao fechar o programa
- [ ] Ligar cada treino montado a um aluno específico
- [ ] Criar uma interface gráfica

## 👤 Autor

Feito por **Miguel Costa**, estudante de programação.
[GitHub](https://github.com/miguelsuruagygcc-cyber)

class Vetor:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.dados = [None] * tamanho

    def set(self, indice, valor):
        if 0 <= indice < self.tamanho:
            self.dados[indice] = valor
            return True
        return False

    def get(self, indice):
        if 0 <= indice < self.tamanho:
            return self.dados[indice]
        return None


class NoAluno:
    def __init__(self, matricula, nome, objetivo, grupo):
        self.matricula = matricula
        self.nome = nome
        self.objetivo = objetivo
        self.grupo = grupo
        self.proximo = None


class ListaEncadeadaAlunos:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.total = 0

    def append(self, matricula, nome, objetivo, grupo):
        if self.buscar(matricula) is not None:
            return False
        novo = NoAluno(matricula, nome, objetivo, grupo)
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo
        self.total += 1
        return True

    def insert(self, posicao, matricula, nome, objetivo, grupo):
        if self.buscar(matricula) is not None:
            return False
        if posicao < 0:
            posicao = 0
        if posicao >= self.total:
            return self.append(matricula, nome, objetivo, grupo)
        novo = NoAluno(matricula, nome, objetivo, grupo)
        if posicao == 0:
            novo.proximo = self.inicio
            self.inicio = novo
            if self.fim is None:
                self.fim = novo
        else:
            anterior = self.inicio
            for _ in range(posicao - 1):
                anterior = anterior.proximo
            novo.proximo = anterior.proximo
            anterior.proximo = novo
        self.total += 1
        return True

    def popleft(self):
        if self.inicio is None:
            return None
        removido = self.inicio
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self.total -= 1
        return removido

    def pop(self):
        if self.inicio is None:
            return None
        if self.inicio is self.fim:
            removido = self.inicio
            self.inicio = None
            self.fim = None
            self.total -= 1
            return removido
        atual = self.inicio
        while atual.proximo is not self.fim:
            atual = atual.proximo
        removido = self.fim
        atual.proximo = None
        self.fim = atual
        self.total -= 1
        return removido

    def buscar(self, matricula):
        atual = self.inicio
        while atual is not None:
            if atual.matricula == matricula:
                return atual
            atual = atual.proximo
        return None

    def remover(self, matricula):
        atual = self.inicio
        anterior = None
        while atual is not None:
            if atual.matricula == matricula:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                if atual is self.fim:
                    self.fim = anterior
                self.total -= 1
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def listar(self):
        alunos = []
        atual = self.inicio
        while atual is not None:
            alunos.append(atual)
            atual = atual.proximo
        return alunos


class NoFila:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None


class FilaAvaliacao:
    def __init__(self):
        self.frente = None
        self.fim = None
        self.total = 0

    def enfileirar(self, nome):
        novo = NoFila(nome)
        if self.fim is None:
            self.frente = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo
        self.total += 1

    def desenfileirar(self):
        if self.frente is None:
            return None
        atendido = self.frente
        self.frente = self.frente.proximo
        if self.frente is None:
            self.fim = None
        self.total -= 1
        return atendido.nome

    def listar(self):
        nomes = []
        atual = self.frente
        while atual is not None:
            nomes.append(atual.nome)
            atual = atual.proximo
        return nomes


class NoPilha:
    def __init__(self, exercicio):
        self.exercicio = exercicio
        self.abaixo = None


class PilhaTreino:
    def __init__(self):
        self.topo = None
        self.total = 0

    def empilhar(self, exercicio):
        novo = NoPilha(exercicio)
        novo.abaixo = self.topo
        self.topo = novo
        self.total += 1

    def desempilhar(self):
        if self.topo is None:
            return None
        removido = self.topo
        self.topo = self.topo.abaixo
        self.total -= 1
        return removido.exercicio

    def listar(self):
        exercicios = []
        atual = self.topo
        while atual is not None:
            exercicios.append(atual.exercicio)
            atual = atual.abaixo
        return exercicios


GRUPOS = ['A', 'B', 'C', 'D', 'E']


def indice_do_grupo(letra):
    letra = letra.upper()
    if letra in GRUPOS:
        return GRUPOS.index(letra)
    return -1


def cabecalho(titulo):
    print("\n" + "=" * 60)
    print(f"  {titulo}")
    print("=" * 60)


def main():
    grupos_vetor = Vetor(len(GRUPOS))
    for i in range(len(GRUPOS)):
        grupos_vetor.set(i, 0)

    alunos = ListaEncadeadaAlunos()
    fila = FilaAvaliacao()
    treino = PilhaTreino()

    while True:
        cabecalho("ACADEMIA - DIVISAO DE ALUNOS E TREINOS PERSONALIZADOS")
        print("   1 - Cadastrar aluno (no fim)")
        print("   2 - Cadastrar aluno em uma posicao")
        print("   3 - Remover aluno por matricula")
        print("   4 - Remover primeiro aluno")
        print("   5 - Remover ultimo aluno")
        print("   6 - Buscar aluno por matricula")
        print("   7 - Listar todos os alunos")
        print("   8 - Ver divisao de alunos por grupo")
        print("   9 - Entrar na fila de avaliacao")
        print("  10 - Chamar proximo da fila")
        print("  11 - Ver fila de espera")
        print("  12 - Adicionar exercicio ao treino")
        print("  13 - Desfazer ultimo exercicio")
        print("  14 - Ver treino montado")
        print("   0 - Sair")
        opcao = input("\n  Escolha uma opcao: ").strip()

        if opcao == "1":
            cabecalho("CADASTRAR ALUNO")
            matricula = input("  Matricula: ").strip()
            nome = input("  Nome: ").strip()
            objetivo = input("  Objetivo (ex: hipertrofia, emagrecimento): ").strip()
            grupo = input(f"  Grupo de treino {GRUPOS}: ").strip().upper()
            idx = indice_do_grupo(grupo)
            if idx == -1:
                print("  >> Grupo invalido! Use A, B, C, D ou E.")
            elif alunos.append(matricula, nome, objetivo, grupo):
                grupos_vetor.set(idx, grupos_vetor.get(idx) + 1)
                print(f"  >> Aluno '{nome}' cadastrado no grupo {grupo}!")
            else:
                print("  >> Ja existe um aluno com essa matricula.")

        elif opcao == "2":
            cabecalho("CADASTRAR ALUNO EM UMA POSICAO")
            posicao_txt = input(f"  Posicao (0 a {alunos.total}): ").strip()
            if not posicao_txt.isdigit():
                print("  >> Posicao invalida.")
            else:
                matricula = input("  Matricula: ").strip()
                nome = input("  Nome: ").strip()
                objetivo = input("  Objetivo: ").strip()
                grupo = input(f"  Grupo de treino {GRUPOS}: ").strip().upper()
                idx = indice_do_grupo(grupo)
                if idx == -1:
                    print("  >> Grupo invalido! Use A, B, C, D ou E.")
                elif alunos.insert(int(posicao_txt), matricula, nome, objetivo, grupo):
                    grupos_vetor.set(idx, grupos_vetor.get(idx) + 1)
                    print(f"  >> Aluno '{nome}' inserido na posicao {posicao_txt}.")
                else:
                    print("  >> Ja existe um aluno com essa matricula.")

        elif opcao == "3":
            cabecalho("REMOVER ALUNO POR MATRICULA")
            matricula = input("  Matricula do aluno: ").strip()
            aluno = alunos.buscar(matricula)
            if aluno is None:
                print("  >> Aluno nao encontrado.")
            else:
                idx = indice_do_grupo(aluno.grupo)
                alunos.remover(matricula)
                grupos_vetor.set(idx, grupos_vetor.get(idx) - 1)
                print(f"  >> Aluno '{aluno.nome}' removido.")

        elif opcao == "4":
            cabecalho("REMOVER PRIMEIRO ALUNO")
            removido = alunos.popleft()
            if removido is None:
                print("  >> Nao ha alunos cadastrados.")
            else:
                idx = indice_do_grupo(removido.grupo)
                grupos_vetor.set(idx, grupos_vetor.get(idx) - 1)
                print(f"  >> Primeiro aluno '{removido.nome}' removido.")

        elif opcao == "5":
            cabecalho("REMOVER ULTIMO ALUNO")
            removido = alunos.pop()
            if removido is None:
                print("  >> Nao ha alunos cadastrados.")
            else:
                idx = indice_do_grupo(removido.grupo)
                grupos_vetor.set(idx, grupos_vetor.get(idx) - 1)
                print(f"  >> Ultimo aluno '{removido.nome}' removido.")

        elif opcao == "6":
            cabecalho("BUSCAR ALUNO")
            matricula = input("  Matricula: ").strip()
            aluno = alunos.buscar(matricula)
            if aluno is None:
                print("  >> Aluno nao encontrado.")
            else:
                print(f"  Matricula : {aluno.matricula}")
                print(f"  Nome      : {aluno.nome}")
                print(f"  Objetivo  : {aluno.objetivo}")
                print(f"  Grupo     : {aluno.grupo}")

        elif opcao == "7":
            cabecalho(f"ALUNOS CADASTRADOS (total: {alunos.total})")
            lista = alunos.listar()
            if not lista:
                print("  Nenhum aluno cadastrado.")
            for pos, a in enumerate(lista):
                print(f"  {pos} - [{a.matricula}] {a.nome} - grupo {a.grupo} - {a.objetivo}")

        elif opcao == "8":
            cabecalho("DIVISAO DE ALUNOS POR GRUPO")
            for i in range(len(GRUPOS)):
                qtd = grupos_vetor.get(i)
                barra = "#" * qtd
                print(f"  Grupo {GRUPOS[i]}: {qtd:2d}  {barra}")

        elif opcao == "9":
            cabecalho("ENTRAR NA FILA DE AVALIACAO")
            nome = input("  Nome do aluno: ").strip()
            fila.enfileirar(nome)
            print(f"  >> '{nome}' entrou na fila. Posicao: {fila.total}")

        elif opcao == "10":
            cabecalho("CHAMAR PROXIMO DA FILA")
            atendido = fila.desenfileirar()
            if atendido is None:
                print("  >> A fila esta vazia.")
            else:
                print(f"  >> Chamando '{atendido}' para a avaliacao fisica!")

        elif opcao == "11":
            cabecalho(f"FILA DE ESPERA (total: {fila.total})")
            nomes = fila.listar()
            if not nomes:
                print("  A fila esta vazia.")
            for pos, nome in enumerate(nomes, start=1):
                marca = "  <- proximo" if pos == 1 else ""
                print(f"  {pos}o - {nome}{marca}")

        elif opcao == "12":
            cabecalho("ADICIONAR EXERCICIO AO TREINO")
            exercicio = input("  Exercicio (ex: Supino reto 4x10): ").strip()
            treino.empilhar(exercicio)
            print(f"  >> '{exercicio}' adicionado ao treino.")

        elif opcao == "13":
            cabecalho("DESFAZER ULTIMO EXERCICIO")
            removido = treino.desempilhar()
            if removido is None:
                print("  >> O treino esta vazio, nada para desfazer.")
            else:
                print(f"  >> Exercicio '{removido}' removido.")

        elif opcao == "14":
            cabecalho(f"TREINO MONTADO (total: {treino.total})")
            exercicios = treino.listar()
            if not exercicios:
                print("  Nenhum exercicio no treino.")
            for i, ex in enumerate(exercicios):
                marca = "  <- ultimo adicionado" if i == 0 else ""
                print(f"  - {ex}{marca}")

        elif opcao == "0":
            print("\n  Encerrando o sistema. Bom treino!\n")
            break

        else:
            print("  >> Opcao invalida, tente novamente.")

        input("\n  (pressione ENTER para continuar)")


if __name__ == "__main__":
    main()

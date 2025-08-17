'''
Paula trabalha em uma plataforma de ensino online e precisa garantir que os alunos sejam inscritos corretamente nos cursos desejados.
 O sistema deve seguir as seguintes regras:

Cada aluno pode se inscrever em um curso, mas antes a plataforma precisa verificar se há vagas disponíveis;
Se houver vagas, o aluno deve ser confirmado na turma e a vaga deve ser reduzida;
Se não houver vagas, o aluno deve ser notificado de que a turma está lotada;
Se um aluno já estiver inscrito, ele não pode se inscrever novamente no mesmo curso.
A lista de alunos e os cursos disponíveis já está definida no sistema. Lembre-se de processar múltiplas inscrições em paralelo. Confira o código:

cursos = {
    "Python Avançado": {"vagas": 2, "inscritos": []},
    "Java para Iniciantes": {"vagas": 1, "inscritos": []},
    "Machine Learning": {"vagas": 0, "inscritos": []},
}
 
alunos = [
    {"nome": "Alice", "curso": "Python Avançado"},
    {"nome": "Bruno", "curso": "Python Avançado"},
    {"nome": "Carlos", "curso": "Java para Iniciantes"},
    {"nome": "Daniela", "curso": "Machine Learning"},
    {"nome": "Alice", "curso": "Python Avançado"},  # Tentativa de inscrição duplicada
]
Copiar código
Saída esperada:

Inscrevendo Alice no curso Python Avançado...
Inscrição confirmada para Alice no curso Python Avançado!  
 
Inscrevendo Bruno no curso Python Avançado...
Inscrição confirmada para Bruno no curso Python Avançado!  
 
Inscrevendo Carlos no curso Java para Iniciantes...
Inscrição confirmada para Carlos no curso Java para Iniciantes!  
 
Inscrevendo Daniela no curso Machine Learning...
Turma lotada! Daniela não pôde se inscrever no curso Machine Learning.  
 
Inscrevendo Alice no curso Python Avançado...
Alice já está inscrita no curso Python Avançado! Inscrição rejeitada.  
 
Todas as inscrições foram processadas! 
'''
import asyncio

cursos = {
    "Python Avançado": {"vagas": 2, "inscritos": []},
    "Java para Iniciantes": {"vagas": 1, "inscritos": []},
    "Machine Learning": {"vagas": 0, "inscritos": []},
}
 
alunos = [
    {"nome": "Alice", "curso": "Python Avançado"},
    {"nome": "Bruno", "curso": "Python Avançado"},
    {"nome": "Carlos", "curso": "Java para Iniciantes"},
    {"nome": "Daniela", "curso": "Machine Learning"},
    {"nome": "Alice", "curso": "Python Avançado"},  # Tentativa de inscrição duplicada
]

async def inscricao(aluno):
  curso = aluno['curso']
  nome= aluno['nome']

  print(f'Inscrevendo {nome} no curso {curso}...')
  vagas = cursos[curso]['vagas']
  if not aluno['nome'] in cursos[curso]['inscritos']:
    if vagas > 0:
      cursos[curso]["inscritos"].append(nome)
      cursos[curso]['vagas']-= 1
      print(f'Inscrição confirmada para {nome} no curso {curso}!\n')
    else:
      print(f'Turma lotada! {nome} não pôde se inscrever no curso {curso}.\n')
  else:
    print(f'{nome} já está inscrito no curso de {curso}. Inscrição rejeitada!\n')

async def main():
  inscricoes = [asyncio.create_task(inscricao(aluno)) for aluno in alunos]
  await asyncio.gather(*inscricoes)
  print('Todas as inscrições foram processadas!')

asyncio.run(main())
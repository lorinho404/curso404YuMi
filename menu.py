from​data.ferramentas​import​figlet, sleep
from​data.cores_persux​import​*


def​cor():
 ​  ​print(f'{br} >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    ​tools_cor​=​['Vermelho',​'Verde',​'Amarelo', 'Azul', 'Rosa',​'Ciano',​'Branco',​'Voltar']
 ​    ​sleep(0.01)
 ​  ​for​c, item​in​enumerate(tools_cor):
 ​      ​print(f' {am}[ {c+1} ] {br}-{cy}​{item}')
 ​      ​sleep(0.01)
 ​  ​print(f'{br}​>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


def​styles():
 ​  ​print(f'{br} >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
 ​  ​sleep(0.01)
 ​  ​tools_style​=​['comum',​'poison', 'lean', 'block',​'alligator',​'cosmic', 'rozzo', 'sblood',​'larry3d']
 ​   for​c​,​item​in​enumerate(tools_style):
 ​      ​print(f' {am}[ {c+1} ] {br}-{cy}​{item}')
 ​        ​sleep(0.01)
 ​  ​print(f'{br} >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


ban_sen​=​f'''{br}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  {ve}​[ 1 ]​{br}-{ve}​alterar
 ​{ve}​[ 2 ] {br}-{ve} remover
  {ve}​[ 3 ] {br}-{ve} voltar
{ve}​>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'''

menu_nome​=​f'''{ve} >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'''
 ​{ve}​[ 1 ]​{br}-{ve} alterar nome
  {ve}​[ 2 ]​{by}-{ve} voltar
{ve}​>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#figled
person404f​=​f"{rx}{figlet.renderText('person404')}"
coresf =​f"{az}{figlet.renderText('Cores')}"
bannerf​=​f"{ve}{figlet.renderText('Banner')}"
senhaf​=​f"{vd}{figlet.renderText('Senha')}"
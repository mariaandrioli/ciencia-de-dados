# Ciência de Dados

UFPR - CI1030 - CIÊNCIA DE DADOS PARA SEGURANÇA - 2021

## Descrição

Esse dataset contém análises manuais e automáticas de malwares num período de aproximadamente 2 anos (Outubro 2014 a Dezembro 2016).
É composto por 143332 registros de malwares.
As entradas numéricas captadas passaram por uma transformação PCA devido a problemas de confidencialidade.

## Links

[Dataset ](https://www.kaggle.com/firebits/vulcanoio-org-misp2-4-54-initial-20161127-07h35m)

## Informações
[MISP  - Malware Information Sharing Platform](https://www.misp-project.org/index.html)

### Campos do dataset  

| Nome  | Descrição  |  Tipo de Dado |
| ------------ | ------------ | ------------ |
| uuid  | Identificador único  | String  |
| event_id  | ID sequencial do evento do MISP  | Integer  |
|  category  |  Categoria segundo o MISP | String  |
| type  |  Tipo segundo o MISP | String  |
|  value | Valor segundo o MISP  | String  |
| to_ids  |  ID designado para o IDS (Sistema de detecção de intrusão) | Integer  |
| date  | Data e hora da análise  |  Integer |

###  Exploração de Dados
#### 1. Que tipos de dados você tem, majoritariamente (atributos numéricos, textuais)?  
Os dados são análises de malwares feitas a partir de sandboxes. Os dados contém identificadores que usam o MISP Project para classificar estes malwares, sendo a maioria dos atributos textuais.
 #### 2. Qual seu objetivo com esse dataset?  
O objetivo á usar esse dataset para analisar quais malwares são mais comuns de acordo com sua categoria, assim possibilitando, em uma solução hipotética para além dessa disciplina, estudar esses malwares e combater esses ataques. 
 #### 3. Seu dataset é rotulado de que maneira?  
Informação disponível no notebook exploraçao.ipynb.
####  4. Como é a distribuição dos dados do dataset?  
Informação disponível no notebook exploraçao.ipynb.

 #### 5. Quais colunas/atributos você julga ser interessante manter e remover? Por quê?  
- Mantém: category, type, value
- Remove: uuid, event_id, to_ids, date

### Autor

- Maria Teresa Andrioli 

[![Linkedin](https://i.stack.imgur.com/gVE0j.png) LinkedIn](https://www.linkedin.com/in/mariateresaandrioli/)
&nbsp;
[![GitHub](https://i.stack.imgur.com/tskMh.png) GitHub](https://github.com/mariaandrioli)

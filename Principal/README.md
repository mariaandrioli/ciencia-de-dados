# Ciência de Dados

UFPR - CI1030 - CIÊNCIA DE DADOS PARA SEGURANÇA - 2021

## Descrição

Esse dataset contém análises manuais e automáticas de malwares num período de de aproximadamente 2 anos (Outubro 2014 a Dezembro 2016)

## Links

[Dataset utilizado](https://www.kaggle.com/firebits/vulcanoio-org-misp2-4-54-initial-20161127-07h35m)

## Informações
MISP  - Malware Information Sharing Platform

### Campos do dataset  

**uuid**: Universally Unique IDentifier  
**event_id**: Sequential Event ID used from the MISP Project  
**category**: category that is classified the artifact internally in the MISP Project  
**type**: type of artifact specified in the MISP Project  
**value**: value assigned to the artifact within the MISP Project  
**to_ids**: Integer ID assigned to the Intrusion Detection System (IDS) to generate alerts  
**date**: Integer ID assigned to date and time of analysis  

###  Exploração de Dados
 1. Que tipos de dados você tem, majoritariamente (atributos numéricos,
    textuais)?  
Os dados são análises de malwares feitas a partir de sandboxes. Os dados contém identificadores que usam o MISP Project para classificar estes malwares, sendo a maioria dos atributos textuais.
 2. Qual seu objetivo com esse dataset?  
O objetivo á usar esse dataset para analisar quais malwares são mais comuns, assim possibilitando, em uma solução hipotética para além dessa disciplina, estudar esses malwares e combater esses ataques. 
 3. Seu dataset é rotulado de que maneira?  
A rotulação é feita a usando o [MISP Project](https://www.misp-project.org/index.html) e os parâmetros do dataset.
 4. Como é a distribuição dos dados do dataset?  
Esse dataset é um csv contendo, em cada linha, um identificador único e suas características, sendo elas: ID, categora, tipo e valor usando o MISP Project e data de análise. Os atributos estão mais explicados na seção "Campos do Dataset acima"
 5. Quais colunas/atributos você julga ser interessante manter e remover? Por quê?  
A única coluna que acredito que seja possível de remover é a de id único. Como a maior parte da análise será de frequências, não é essencial que cada campo tenho seu identificador exclusivo. É interessante manter todas as outras pois elas proporcionam uma melhor filtragem e análise, e como são apenas seis colunas, não acredito que o processamento fosse ser prejudicado drasticamente caso o dataset fosse maior. Uma coluna que talvez pudesse ser removida é a de data, mas eu ainda optaria por mantê-la para que haja a possibilidade de filtrar por períodos específicos e possivelmente encontrar similaridades. 

### Autor

- Maria Teresa Andrioli 

[![Linkedin](https://i.stack.imgur.com/gVE0j.png) LinkedIn](https://www.linkedin.com/in/mariateresaandrioli/)
&nbsp;
[![GitHub](https://i.stack.imgur.com/tskMh.png) GitHub](https://github.com/mariaandrioli)

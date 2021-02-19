# Ciência de Dados

UFPR - CI1030 - CIÊNCIA DE DADOS PARA SEGURANÇA - 2021

## Descrição

PARTE 1:

O arquivo AV1. txt e AV2.txt representam parte da base de dados de assinaturas de vírus do antivírus CLAMAV.

A. Usando informações de AV1.txt, gere um arquivo com as seguintes informações:

- Rótulos ordenados alfabeticamente únicos compostos apenas pelo TIPO e FAMÍLIA (removendo o sistema operacional e as variantes) e quantidade de variantes, separados por vírgulas.

- Um exemplo de rótulo é Win.Trojan.Agent-1135181, onde:

Win é o Sistema Operacional
Trojan é o tipo de código malicioso
Agent é a família
1135181 a variante
Exemplo de saída esperada no arquivo resultante (supondo que só haja amostras de Win.Trojan.Agent-<variante>):

Trojan.Agent,14512

B. Usando informações de AV2.txt, gere uma saída onde cada linha é uma amostra com os campos "Plataforma/Linguagem", "Tipo", "Subtipo", "Variante", excluindo-se o termo PUA (Potentially Unwanted Application). 

- O arquivo de saída deve gerar a seguinte linha para a entrada "PUA.Win.Tool.PsyBNC-1:6:*:707379424e430025732573257300533d002a00533d2573007372632f705f7365727665722e63007365":

Win,Tool,PsyBNC,1

- O arquivo final é o conjunto de amostras representadas como acima, uma por linha, do total de linhas de AV2.txt

==================================================================================

PARTE 2:

Gerar um dataset a partir dos arquivos "community.rules" e "sid-msg.map", composto dos seguintes campos separados por ",":

Protocolo, representado numericamente (0 para ip, 1 para tcp, 2 para udp, 3 para icmp)
Porta de destino
SID, representando o rótulo como uma string
Por exemplo, a entrada "alert tcp $EXTERNAL_NET any -> $HOME_NET 445 (msg:"MALWARE-CNC Win.Trojan.BasicPipeShell variant communication attempt"; flow:to_server,established; content:"|FE|SMB"; depth:4; offset:4; content:"|05 00|"; within:2; distance:8; content:"|70 00 69 00 70 00 65 00 73 00 68 00 65 00 6C 00 6C 00 2D 00 70 00 69 00 70 00 65 00 6E 00 61 00 6D 00 65 00|"; metadata:policy max-detect-ips drop, ruleset community, service netbios-ssn; reference:url,www.fireeye.com/blog/threat-research/2020/12/unauthorized-access-of-fireeye-red-team-tools.html; classtype:trojan-activity; sid:56892; rev:1;)" ficaria assim no arquivo de saída:

1,445,MALWARE-CNC Win.Trojan.BasicPipeShell variant communication attempt

## Execução

```python
python T1p1a.py <nome_do_arquivo>
```
```python
python T1p1b.py <nome_do_arquivo>
```
```python
python T1p2.py <nome_do_arquivo_1> <nome_do_arquivo_2>
```



### Autor

- Maria Teresa Andrioli 

[![Linkedin](https://i.stack.imgur.com/gVE0j.png) LinkedIn](https://www.linkedin.com/in/mariateresaandrioli/)
&nbsp;
[![GitHub](https://i.stack.imgur.com/tskMh.png) GitHub](https://github.com/mariaandrioli)

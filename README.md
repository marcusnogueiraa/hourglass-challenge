# hourglass-challenge

**Desafio da Ampulheta - Disciplina Matemática Discreta**

 *A matemática possui ferramentas que podem ser utilizadas para resolver problemas. Juntamente com a implementação de uma linguagem de programação, é possivel utilizar da matemática discreta de forma a apresentar ao usuário uma possível solução.*
 
 **Descrição do Desafio**<br/>
 Existem duas ampulhetas, que medem dois tempos diferentes:<br/>
  **- Ampulheta A:** 3 minutos<br/>
  **- Ampulheta B:** 5 minutos<br/>
  
  Apresente um modo de medir qualquer tempo existente (em minutos e inteiro), utilizando apenas essas duas ampulhetas.
  
  Certamente, é um problema mais matemático do que de lógica de programação, o código em si é apenas algumas condicionais com com blocos de impressão de texto (solução).
  A resolução do problema é totalmente matemático, primeiramente é preciso eliminar os casos nulos:
  
  **X = Minutos requeridos pelo usuário**
  
  >**X é menor ou igual á 0**<br/>
  >Nesse caso não é preciso o algoritmo para resolver o problema, pois não é preciso nenhum instrumento de medição para medir o valor "0" em minutos. E não é possivel medir tempo negativo, portanto, o valor inserido pelo usuário se trata de um unsigned int. (Inteiro sem sinal, número positivo).
  
  **Resolução do Problema**<br/>
  Para resolver o problema, foi preciso encontrar um padrão, para cada um dos tempos de 1 até o infinito (em minutos). O usuário iria inserir esse número e uma instrução em texto teria de informar exatamente como medir esse tempo. Perceba que, números multiplos de 3 e 5 possuem muita facilidade para medição. Se o minuto inserido (X) for multiplo de 3, é só medirmos o tempo utilizando a ampulheta A (3min) K vezes (sendo K = X / 3). Por exemplo o número 15 é multiplo de 3, sabemos que 15 / 3 = 5, logo se utilizarmos a ampulheta A (3min) 5 vezes, iremos conseguir medir esse valor. O mesmo se aplica aos múltiplos de 5, mas dessa vez utilizando a ampulheta B (3min) e dividindo os valores por 5. 
  
  Podemos aplicar isso também aos multiplos de 8, medir o número 8 também é muito simples, basta utilizar a ampulheta A (3min), e ao terminar, utilizar a ampulheta B (5min), assim teremos 3 min + 5min = 8min. No caso do número 56, sabemos que 56 / 8 = 7, logo precisamos apenas repetir esse processo 7 vezes.
  
 Os outros dois casos são os casos que atendem a seguinte condição: (k . 3 + 1 = x) e (k . 3 + 2 = x)<br/>
 Sendo K = Constante qualquer, X = Número requisitado pelo usuário.
 
 No caso (k . 3 + 1 = x), utilizamos as duas ampulhetas ao mesmo tempo, quando a ampulheta A (3min) terminar, restará 2 min na ampulheta B (5min). Viramos a ampulheta A novamente, e quando os 2 minutos de B terminar, Restará 1 minuto na ampulheta A, logo utilizamos o resto de A + K vezes a ampulheta A, sendo K o restante dos minutos dividido por 3. Podemos utilizar como exemplo o número 31, ao fazer todo o processo até termos restado 1 minuto na ampulheta A, iremos medir esse 1 minuto e logo após medir os 30 minutos restantes para completar os 31, que seria o valor de K, então, medimos utlizando a ampulheta A 10 vezes. Totalizando 30 + 1 = 31 minutos. Lembrando que esse caso pode ser utilizado para medir o número 1, sendo o valor de K = 0;
 
 No caso (k . 3 + 2 = x) utilizamos as duas ampulhetas ao mesmo tempo, quando a ampulheta A (3min terminar), restará 2min na ampulheta B (5mim). Utilizamos os 2 minutos restantes de B + K vezes a ampulheta A para medir o tempo. Por exemplo o número 11, ao restar 2 minutos em B, utilizamos B mais 3 vezes a ampulheta a para medir o valor, resultando em 2 + 9 = 11. Lembrando que esse caso pode ser utilizado para medir o número 2, sendo o valor de K = 0:
 
 | **Casos**  |
| ------------- |
| **1.** *K . 3 == X*  |
| **2.** *K . 5 == X*  |
| **3.** *K . (5 + 3) == X* |
| **4.** *K . 3 + 1 = X* |
| **5.** *K . 3 + 2 = X*  |

**OBSERVAÇÕES E CONCLUSÃO**<br/> Lembrando que seria possivel resolver esse problema utilizando apenas os casos 1, 4 e 5. Porém foi utilizado mais casos para apresentar ao usuário não só um método correto quanto o mais simples. O número 10 por exemplo poderia ser resolvido utilizando o Caso 4, pois 3 . 3 + 1 = 10, mas certamente é bem mais simples utilizar a ampulheta B (5min) duas vezes, não acha?

A resolução do problema foi bem simples, em breve irei adcionar um algorítimo 2.0, na qual o usuário além de inserir os minutos a serem medidos, também iria definir o tempo das duas ampulhetas.

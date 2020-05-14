# ADN-TyMA
Este programa de Python genera una secuencia de nucleótidos aleatoria, que representará nuestra primera hebra de ADN. 
Encontraremos la secuencia complementaria (3' - 5') y su reversa complementaria (5' - 3'). 
Después, encontraremos el ARN mensajero resultante en el proceso de transcripción. 
Hallaremos los codones de inicio y de parada, y partiremos la secuencia de tres en tres a partir de ellos. 
Realizaremos el proceso de traducción encontrando los aminoácidos correspondientes y acabaremos imprimiendo 
los 6 marcos de lectura. Este proyecto ha sido desarrollado para la asignatura "Técnicas y Modelos Algorítmicos", 
asignatura de Ingeniería de la Salud de la Universidad de Málaga. 

Realizado por Juan Herrera Conde.

## 1. OBJETIVOS

En esta primera entrega, he desarrollado un programa codificado en Python que genera una secuencia de nucleótidos aleatoria, que representará nuestra primera hebra de ADN. Encontraremos la secuencia complementaria (3' - 5') y su reversa complementaria (5' - 3'). Después, encontraremos el ARN mensajero resultante en el proceso de transcripción. Hallaremos los codones de inicio y de parada, y partiremos la secuencia de tres en tres a partir de ellos. Realizaremos el proceso de traducción encontrando los aminoácidos correspondientes y acabaremos imprimiendo los 6 marcos de lectura. 
Aunque el objetivo de este proyecto es diferenciar los distintos codones de la secuencia del ARN mensajero con sus correspondientes marcos de lectura, no he querido desaprovechar la oportunidad de repasar los conceptos biológicos estudiados en la introducción de la asignatura, como son las hebras complementarias o los procesos de traducción y transcripción.

## 2. SECCIONES DEL PROGRAMA

Aunque considero que lo importante de este proyecto era asimilar los contenidos biológicos tratados en las primeras semanas de curso, voy a explicar brevemente cómo he decidido organizar el código del programa, ya que es una parte fundamental del resultado que obtendremos. En código está dividida en dos clases o secciones, la primera es la principal, la que ejecuta los métodos, y la segunda es en la que implementaremos los conjuntos de datos y los métodos. No he querido implementar ningún tipo de interfaz por lo ya mencionado, no considero que sea el objetivo principal y prefiero optar por la funcionalidad y la simpleza.

### 2.1. VALIDACIÓN DE LA SECUENCIA OBTENIDA

Como he comentado anteriormente, la secuencia de nucleótidos que produciremos será completamente aleatoria. Cada vez que ejecutemos el programa, podremos elegir su longitud. Antes de tenerla en cuenta para calcular sus diferentes parámetros, tenemos que validarla, es decir, que contiene los cuatro tipos de nucleótidos. Para lograr este objetivo hemos implementado este sencillo método.

### 2.2. CÁLCULO DE FRECUENCIAS RELATIVAS

Estableceremos un método que calcule la frecuencia relativa porcentual, y la imprimiremos por pantalla, como veremos en el punto tres. 

### 2.3. TRANSCRIPCIÓN Y SECUENCIAS COMPLEMENTARIAS

Se realiza la transcripción de la secuencia de nucleótidos a ARN mensajero, traduciendo la timina a uracilo. Imprimiremos también la frecuencia de la hebra complementaria y la reversa complementaria.

### 2.4. TRADUCCIÓN

Con este método realizaremos la traducción del ARN mensajero a la secuencia de aminoácidos correspondiente.

### 2.5. CODONES DE INICIO Y DE PARADA

Encontraremos los codones de inicio y de parada de esa secuencia de ARN mensajero.

### 2.6. MARCOS DE LECTURA

Generaremos los seis marcos de lectura que corresponden a la traducción del ARN mensajero, teniendo en cuenta los codones de inicio y de parada previamente encontrados.
 
## 3. IMPRESIÓN 

En la clase principal (main), ejecutaremos todos los métodos ya descritos. El resultado será todas las impresiones por pantalla anteriormente revisadas.










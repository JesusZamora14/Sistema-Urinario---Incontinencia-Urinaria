[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=JesusZamora14/Sistema-Urinario---Incontinencia-Urinaria)

Sistema Urinario
Estudiantes
Marla Espinoza Bedoy, Abraham Gómez Aguilar, Jesus Zamora Cervantes 
Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México. Email:  l21212152@tectijuana.edu.mx; l21212158@tectijuana.edu.mx; l21212185@tectijuana.edu.mx
Asignaturas o departamento donde se puede usar la Actividad
Modelado de Sistemas Fisiológicos de Ingeniería Biomédica

Información general
El modelado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.
Objetivo general
Diseñar un gemelo digital de un sistema fisiológico que permita identificar las diferencias entre un paciente afectado por una enfermedad (caso) y un individuo saludable (control) para desarrollar un protocolo de tratamiento mediante un sistema de control en lazo cerrado.
Descripción detallada del sistema
El sistema urinario, en particular el proceso de filtración hasta la expulsión de orina como desecho a través de la uretra puede ser representado mediante un modelo que simula la dinámica de los órganos que componen el sistema y hacen posible la generación y transporte de la orina con un circuito eléctrico de segundo orden.

Se inicia con una rama principal que representa la llegada de la sangre y sus componentes al riñón a través de la arteria renal, con ésta llega una presión de entrada denominada presión hidrostática sanguínea, la cual es esencialmente la fuerza principal que empuja a la sangre contra la barrera de filtración glomerular. Este proceso es realizado en la unidad fundamental del riñón denominada nefrona y se representa en la rama principal del circuito por una resistencia de 10 kOhm. Se considera la filtración de sales, iones, metabolitos y otros componentes útiles de la sangre por medio de poros capilares que impiden el paso de estos componentes, lo cual representa el 99% del líquido recibido inicialmente por los riñones. En la primera rama secundaria, se representa la reabsorción de la sangre con una resistencia de 1000 kOhm y se asume la formación de la orina por el mismo componente, lo cual se puede observar por el flujo resultante en la segunda rama secundaria. En esta aparece en cadena los efectos de los uréteres, la vejiga y finalmente los esfínteres de la uretra, por donde se expulsa la orina. En los uréteres se presentan movimientos peristálticos, los cuales son contracciones que generan ondas que ayudan a transportar la orina desde los riñones hacia la vejiga, impidiendo que fluya en sentido contrario, por lo mismo se representa con un inductor. Luego llega a la vejiga, al cual está prevista de propiedades elásticas que le permiten expandirse a medida que se llena de orina, lo cual permite que sea representada con un capacitor. Su elasticidad es crucial porque le permite almacenar una cantidad variable de orina sin romperse. Finalmente, cuando es momento de excretar la orina producida (aproximadamente de 1.5-2 litros al día), se dirige a la uretra la cual está rodeada de esfínteres internos y externos, este último siendo voluntario, que permite liberar la orina de manera consciente, se representa con una resistencia. Cuando se presenta incontinencia urinaria, la vejiga presenta mayor dificultad para almacenar orina, a la par que los esfínteres uretrales presentan menos resistencia para resistirse al paso de la misma, haciendo que se libere de manera involuntaria. 

Se utiliza una función de impulso para representar la capacidad de la vejiga y la uretra, revelando diferencias claves entre una condición normal y patológica (incontinencia) mediante el estímulo abrupto como un aumento momentáneo de presión o flujo urinario, permitiendo evaluar cómo se almacena y distribuye en los órganos del sistema urinario que se encargan de la expulsión de la orina.

Referencias principales
[1] J. E. Robles. La incontinencia urinaria. Anales del sistema sanitario de Navarra. Gobierno de Navarra. Departamento de Salud. vol. 29, no. 2, pp. 219-231, 2006.

[2] National Institute of Diabetes and Digestive and Kidney Diseases. Síntomas y causas de los problemas de control de vejiga (incontinencia urinaria). Accedido: Dic. 06, 2024. {En línea] Disponible:https://www.niddk.nih.gov/health-information/informacion-de-la-salud/enfermedades-urologicas/problemas-control-vejiga-incontinencia-urinaria/sintomas-causascontinencia urinaria



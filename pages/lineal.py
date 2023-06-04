import streamlit as st
from PIL import Image

## ñ, á, é, í, ó, ú ¿

st.markdown("# Álgebra Lineal 🐝")
st.sidebar.markdown("# Álgebra Lineal 🐝")
activation_function = st.selectbox('Definiciones', ['None', 'Espacios Vectoriales', 'Subespacios Vectoriales', 'Matrices', 'Determinantes', 'Transformaciones Lineales','Bibliografia Recomendada'])

## Espacios Vectoriales
if activation_function == 'Espacios Vectoriales':
    st.title("Espacios Vectoriales")
    st.write('Definición de un Espacio Vectorial.')
    st.write('Un espacio vectorial es un conjunto no vacío V de objetos, llamados vectores, en el que se han definido dos operaciones: la suma y el producto por un escalar (número real) sujetas a los diez axiomas que se dan a continuación. Los axiomas deben ser válidos para todos los vectores u,v y w en V y los ecalares α y β reales. Llamamos u + v a la suma de vectores en V, y αv al producto del real α por un vector v ∈ V')
    st.markdown('- $u + v ∈ V$.')
    st.markdown('- $u+v = v+u$.')
    st.markdown('- $(u+v) + w = u + (v+w)$.')
    st.markdown('- Existe un vector nulo $0_{V} ∈ V$ tal que $v + 0_{V} = v $.')
    st.markdown('- Para cada $v en V$, existe $(–v)∈ V$ tal que $v+(–v)=0_{V}$.')
    st.markdown('- $α v ∈ V$ .')
    st.markdown('- $α(u+v)=αu+αv$')
    st.markdown('- $(α+β)v=αv+βv$.')
    st.markdown('- $α(βv)=(αβ)v$.')
    st.markdown('- $1v=v$')
    st.title("Ejemplo")
    st.markdown('Llamemos $P_{2}$ al conjunto de polinomios de grado menor o igual que 2, incluyendo el polinomio nulo. Recordemos la suma de polinomios y la multiplicación por un escalar:')
    st.markdown('Dados $p(x)=a_{o} + a_{1}x + a_{2}x^{2} ∈ P_{2}$ y $q(x)=b_{o}+b_{1}x+b_{2}x^{2} ∈ P_{2}$. Definimos las operaciones: $(p+q)(x)=p(x)+q(x)=(a_{o}+b_{o})+(a_{1}+b_{1})x+(a_{2}+b_{2})x^{2} ∈ P_{2}$')
    st.markdown('$(αp)(x)=αp(x)=(αa_{o})+(αa_{1})x+(αa_{2})x^{2} ∈ P_{2}$')
    st.markdown('Puede demostrarse que estas operaciones verifican todos los axiomas de espacio vectorial. En particular, el vector nulo en este espacio es el polinomio nulo, es decir el polinomio cuyos coeficientes son todos iguales a cero. Generalizando, para cualquier $n≥0$ el conjunto $P_{n}$ de todos los polinomios de grado menor o igual que $n$ (incluyendo el polinomio nulo) es un espacio vectorial.')
    
  
    
## Subespacios Vectoriales
if activation_function == 'Subespacios Vectoriales':
    st.title("Subespacios Vectoriales")
    st.write('Definición de un Subespacio Vectorial.')
    st.markdown('Sea $V$ un espacio vectorial y $W$ un subconjunto no vacío de $V$. $W$ es un subespacio de $V$ si $W$ es en sí mismo un espacio vectorial con las mismas operaciones (suma de vectores y producto por un escalar) definidas en $V$.')
    st.title("Ejemplo")
    st.markdown('$W={(x_{1},x_{2})∈ R^{2}:x_{2}=3x_{1}}$ ¿es un subespacio de $R^{2}$?')
    st.markdown('Primero analicemos el conjunto $W$. Son todos vectores de $R^{2}$ tales que la segunda componente es el triple de la primera:')
    st.markdown('$(x_{1},3x_{1})=x_{1}(1,3)$')
    st.markdown('$W$ es la recta que pasa por el origen y tiene vector director $(1,3)$, o sea la recta de ecuación $y = 3x$.')
    st.title("Condiciones necesarias y suficientes para caracterizar subespacios")
    st.markdown('Sea $W$ un subconjunto de un espacio vectorial $V (W⊆V)$. $W$ es subespacio de $V$ si y sólo si se cumplen las siguientes condiciones:')
    st.markdown('$V$ está en $W$.')
    st.markdown('Si $u$ y $v$ están en $W$, entonces $u+v$ está en $W$.')
    st.markdown('Si $u$ está en $W$ y $k$ es un escalar,  $ku$ está en $W$.')
    
    
## Matrices
if activation_function == 'Matrices':
    st.title("Matrices")
    st.write('Definición de una matriz.')
    st.markdown('Una matriz es un conjunto $p-dimensional$ de números (elementos de la matriz) ordenados en filas (o renglones) y columnas, donde una fila es cada una de las líneas horizontales de la matriz y una columna es cada una de las líneas verticales. A una matriz con $m$ filas y $n$ columnas se le denomina matriz $mxn$ donde $m,n ∈ \mathbb N - \{0\}$. El conjunto de las matrices de tamaño $mxn$ se representa como $\mathbb M_{mxn}(\mathbb K)$, en donde $\mathbb K$ es el cuerpo al cual pertenecen los elementos de la matriz.')
    st.write('Propiedades de la suma de matrices.')
    st.markdown('Sean A, B, C ∈ $\mathbb M_{mxn} (\mathbb K)$ entonces se cumplen las siguientes propiedades para la operación binaria $+$')
    st.write('Asociatividad')
    st.markdown('$(A+B)+C=A+(B+C)$')
    st.write('Conmutatividad')
    st.markdown('$(A+B)=(B+A)$')
    st.write('Existencia del Neutro Aditivo')
    st.markdown('Existe $0$ ∈ $\mathbb M_{mxn}(\mathbb K)$ tal que $(A+0)=(0+A)=A$')
    st.write('Existencia del Inverso Aditivo')
    st.markdown('Existe $D$ ∈ $\mathbb M_{mxn}(\mathbb K)$ tal que $A+D=0$')
    st.write('Propiedades del producto por un escalar.')
    st.markdown('Sean A, B, C ∈ $\mathbb M_{mxn} (\mathbb K)$ y $\lambda, \mu \in \mathbb K$ entonces se cumplen las siguientes propiedades para la operación producto por un escalar')
    st.write('Asociatividad')
    st.markdown('$(\lambda \mu)A=\lambda(\mu A)$')
    st.write('Distributividad respecto a la suma de matrices')
    st.markdown('$\lambda (A+B)= \lambda A + \lambda B$')
    st.write('Distributividad respecto a la suma en el cuerpo')
    st.markdown('$(\lambda + \mu)A= \lambda A + \mu A$')
    st.write('Producto por el neutro multiplicativo del cuerpo')
    st.markdown('$1_{\mathbb K}A = A$')
    st.write('Ejemplos')
    st.write('Ejemplo de la suma de dos matrices')
    st.markdown('Sean A, B ∈ $\mathbb M_{mxn} (\mathbb K)$, se define la suma de matrices como:')
    st.latex(r'''\begin{bmatrix}
2 & 2 & 1 \\
3 & 2 & 1 \\
2 & 3 & 2 \\
2 & 0 & 4
\end{bmatrix} + \begin{bmatrix}
0 & 1 & 4 \\
1 & 4 & 0 \\
2 & 1 & 1 \\
0 & 2 & 2
\end{bmatrix} = \begin{bmatrix}
2 & 3 & 5 \\
4 & 6 & 1 \\
4 & 4 & 3 \\
2 & 2 & 6
\end{bmatrix} ''')
    
    
## Transformaciones Lineales
if activation_function == 'Transformaciones Lineales':
    st.title("Transformaciones Lineales")
    st.write('Definición.')
    st.write('Se denomina aplicación lineal, función lineal, transformación lineal, u operador lineal a toda aplicación cuyo dominio y codominio sean espacios vectoriales, tal que satisfaga la siguiente definición:')
    st.markdown('Sean $V$ y $W$ espacios vectoriales sobre el mismo cuerpo $\mathbb K$. Una transformacion $T$ de $V$ en $W$, es decir, $T:V → W$  es una transformación lineal si para todo par de vectores $u,v∈V$  y para todo escalar $k$ ∈ $\mathbb K$  se satisface que:')
    st.markdown('1.$T(u+v$ = T(u) + T(v)$')
    st.markdown('2.$T(ku)=kT(u)$')
    st.write('Al cimplimiento de 1 y 2 se le conoce como "principio de superposicion".')
    st.write('Ejemplo')
    st.markdown('Sea $V$ el conjunto de funciones continuas en $\mathbb R$ y defínase $\phi : V \to V$ mediante ${\displaystyle \phi (f)(t)=\int _{0}^{t}f(x)\,dx}$ ocurre que:')
    st.markdown('${\displaystyle \int _{0}^{t}(f(x)+g(x))\,dx=\int _{0}^{t}f(x)\,dx+\int _{0}^{t}g(x)\,dx}$ ')
    st.write('y')
    st.markdown('${\displaystyle \int _{0}^{t}cf(x)\,dx=c\int _{0}^{t}f(x)\,dx}$ para ${\displaystyle c\in \mathbb {R}}$')
    st.write('Por lo tanto se cumple que')
    st.markdown('$\phi (f+g) = \phi(f) + \phi(g)$ y $\phi (cf) = c \phi (f)$ para todo $f,g \in V$ y todo $c \in \mathbb R$ Por lo que $\phi$ es una transformacion lineal de $V$ en $V$')
    
## Determinantes 
if activation_function == 'Determinantes':
    st.title("Determinantes")
    st.markdown('El determinante de una matriz nos indica si estamos ante un sistema singular o no singular de ecuaciones lineales. Por ello, si el resultado del determinante es cero (nulo), estaremos ante una matriz singular, y si el resultado es distinto de cero, estaremos ante una matriz no singular. ')
    st.subheader('Propiedades de un determinante:')
    st.write('El determinante de una matriz siempre es igual al de su matriz traspuesta.')
    st.write('El determinante de una matriz será siempre cero (nulo) si la matriz contiene dos filas o columnas iguales, si los elementos de una fila o columna son todo ceros o si los elementos de una fila o columna son una combinación lineal de las demás.')
    st.write('El determinante del producto de dos matrices será siempre el mismo que el resultado del producto de sus determinantes.')
    st.write('El determinante cambia de signo si se intercambian dos filas o columnas cualesquiera de una matriz.')
    st.write('El determinante de una matriz no se altera si sumamos a una fila o columna un múltiplo de otra fila o columna.')
    st.subheader('Regla de Laplace')
    st.markdown('Mediante esta regla podremos calcular fácilmente el determinante de matrices de dimensiones iguales y mayores a $3x3$. De esta forma, simplificamos el cálculo de las matrices de dimensiones elevadas al utilizar la suma de los determinantes de las matrices menores en las que se descompone la matriz inicial.')
    st.subheader('Regla de Sarrus')
    st.write('La regla de Sarrus es un método usado para calcular el determinante de una matriz cuadrada de tercer orden. Recibe su nombre del matemático francés Pierre Frédéric Sarrus, que la introdujo en el artículo Nouvelles méthodes pour la résolution des équations, publicado en Estrasburgo en 1833')
    st.markdown('Considérese la matriz de $3×3$:')
    st.latex(r'''{{ecuación|
   M =
   \begin{bmatrix}
      a_{11} & a_{12} & a_{13} \\
      a_{21} & a_{22} & a_{23} \\
      a_{31} & a_{32} & a_{33}
   \end{bmatrix}}}''')
    st.write('Su determinante se puede calcular de la siguiente manera:')
    st.write('En primer lugar, repetir las dos primeras filas de la matriz debajo de la misma de manera que queden cinco filas. Después sumar los productos de las diagonales descendentes (en línea continua) y sustraer los productos de las diagonales ascendentes (en trazos). Esto resulta en:')
    st.latex(r'''{{ecuación|
   \det
    \begin{bmatrix}
         a_{11} & a_{12} & a_{13} \\
         a_{21} & a_{22} & a_{23} \\
         a_{31} & a_{32} & a_{33}
   \end{bmatrix}
   =
   \begin{vmatrix}
      a_{11} & a_{12} & a_{13} \\
      a_{21} & a_{22} & a_{23} \\
      a_{31} & a_{32} & a_{33}
   \end{vmatrix}
   =
   a_{11} a_{22} a_{33} + \;
   a_{21} a_{32} a_{13} + \;
   a_{31} a_{12} a_{23} - \;
   a_{13} a_{22} a_{31} - \;
   a_{23} a_{32} a_{11} - \;
   a_{33} a_{12} a_{21}}}''')
    
## Determinantes de orden inferior
    st.subheader("Determinantes de orden inferior")
    st.write('El caso de matrices de orden inferior (orden 1, 2 o 3) es muy simple y su determinante se calcula con sencillas reglas conocidas. Dichas reglas son también deducibles del teorema de Laplace.')
    st.write('Una matriz de orden uno, es un caso trivial, pero lo trataremos para completar todos los casos. Una matriz de orden uno puede ser tratada como un escalar, pero aquí la consideraremos una matriz cuadrada de orden uno:')
    st.latex(r'''A =
    \left [ \begin{array}{c}
      a_{11}
   \end{array} \right ]''')
    st.write('El valor del determinante es igual al único término de la matriz:')
    st.latex(r'''\det A =
   \det 
   \left [ \begin{array} {c}
      a_{11}
   \end{array} \right ]
   =
   a_{11}''')
    st.latex(r'''A =
   \left [ \begin{array}{cc}
      a_{11} & a_{12} \\
      a_{21} & a_{22}
   \end{array} \right ]''')
    st.write('se calculan con la siguiente fórmula')
    st.latex(r'''| A | = 
   \begin{vmatrix}
      a_{11} & a_{12} \\
      a_{21} & a_{22}
   \end{vmatrix}
   =
     a_{11} a_{22}
   - a_{12} a_{21}''')
    st.latex(r'''A =
   \left [ \begin{array}{ccc}
      a_{11} & a_{12} & a_{13} \\
      a_{21} & a_{22} & a_{23} \\
      a_{31} & a_{32} & a_{33}
   \end{array} \right ]''')
    st.write('El determinante de una matriz de orden 3 se calcula mediante la regla de Sarrus:')
    st.latex(r'''|A| = 

   \left | \begin{array}{ccc}
      a_{11} & a_{12} & a_{13} \\
      a_{21} & a_{22} & a_{23} \\
      a_{31} & a_{32} & a_{33}
    \end{array} \right |
   =   (a_{11} a_{22} a_{33} 
   + a_{12} a_{23} a_{31} 
   + a_{13} a_{21} a_{32}) 
   - (a_{31} a_{22} a_{13} 
   + a_{32} a_{23} a_{11} 
   + a_{33} a_{21} a_{12})''')
    
## Bibliografia
if activation_function == 'Bibliografia Recomendada':
    st.title("Bibliografia Recomendada")
    st.write('Curtis, C.W., Linear Algebra. New York: Springer, 1984')
    st.write('Friedberg, S. H., Insel, A. J., Spence, L. E., Álgebra Lineal. México: Publicaciones Cultural,1982.')
    st.write('Lang, S., Álgebra Lineal. México: Sistemas Técnicos de Edición, 1986')
    st.write('Rincón, H. A., Álgebra Lineal. México: Las Prensas de Ciencias, 2002.')
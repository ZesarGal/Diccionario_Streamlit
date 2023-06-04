import numpy as np
import matplotlib.pyplot as plt
import cvxopt as opt
from cvxopt import blas, solvers
import pandas as pd
import pylab
from PIL import Image
import streamlit as st
import streamlit as st
import numpy as np
import plotly.graph_objects as go

from activations import derivative, logistic, relu, elu, selu_alpha, selu_scale, selu, plot_function, plot_function_derivative


st.markdown("# Cálculo 👽")
st.sidebar.markdown("# Cálculo 👽")

activation_function = st.selectbox('Definiciones', ['None', 'Función logística (sigmoidea)', 'Función tangente hiperbólica (Tanh)', 'Derivada Parcial', 'Multiplicadores de Lagrange', 'Matriz Jacobiana', 'Función unitaria lineal exponencial','Bibliografia Sugerida'])

## Función Logística
if activation_function == 'Función logística (sigmoidea)':

    st.header('Función logística (sigmoidea)')

    st.subheader('Descripción')
    st.write('Es una función sigmoidea con una curva característica en forma de "S".')
    st.markdown(r'**$sigmoid(z)=\frac{1}{1+exp(-z)}$**')
    st.write('La salida de la función logística (sigmoide) está siempre entre 0 y 1.')   

    st.subheader('Plot')
    logistic_fig  = plot_function(logistic, title='Logistic (Sigmoid) Activation Function')
    logistic_fig.add_annotation(x=7, y=1, text='<b>Saturation</b>', showarrow=True,
     font=dict(family="Montserrat", size=16, color="#1F8123"),
        align="center",arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor="#A835E1", ax=-20, ay=30,)
    logistic_fig.add_annotation(x=-7, y=0, text='<b>Saturation</b>', showarrow=True,
     font=dict(family="Montserrat", size=16, color="#1F8123"),
        align="center",arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor="#A835E1", ax=0, ay=-30,)
    st.plotly_chart(logistic_fig)
    with st.expander('Plot Explanation'):
        st.write('- La función logística se satura a medida que las entradas son mayores (positivas o negativas).')
        st.write('- Para valores positivos y negativos grandes, la función se acerca asintóticamente a 1 y 0, respectivamente.')
        st.write('- Cuando la función se satura, su gradiente se aproxima mucho a cero, lo que ralentiza el aprendizaje..')

    st.subheader('Derivada')
    st.markdown(r'$sigmoid^{\prime}(z)=sigmoid(z)(1−sigmoid(z))$')
    st.text("")
    logistic_der_fig = plot_function_derivative(logistic, title='Derivada de la función logística')
    st.plotly_chart(logistic_der_fig)
    with st.expander('Plot Explanation'):
        st.write('Observe que la derivada de la función logística se aproxima mucho a cero para entradas positivas y negativas grandes.')

    st.subheader('Pros')
    st.write('1. La función logística introduce la no linealidad en la red, lo que le permite resolver problemas más complejos que las funciones de activación lineales.\n2. Es continua y diferenciable en todas partes.\n3. Como su salida está entre 0 y 1, es muy común utilizarla en la capa de salida en problemas de clasificación binaria.')

    st.subheader('Contras')
    st.write("1. Sensibilidad limitada\n- La función logística satura en la mayor parte de su dominio.\n- Sólo es sensible a las entradas alrededor de su punto medio 0,5.")
    st.write("2. Debido a que la función logística puede saturarse fácilmente con entradas grandes, su gradiente se acerca mucho a cero. Esto hace que los gradientes sean cada vez más pequeños a medida que la retropropagación avanza hacia las capas inferiores de la red.\n- Finalmente, los pesos de las capas inferiores reciben actualizaciones muy pequeñas y nunca convergen a sus valores óptimos.")

    
## Funcion Tangente Hiperbolica
if activation_function == 'Función tangente hiperbólica (Tanh)':
    st.header('Función tangente hiperbólica (Tanh)')

    st.subheader('Descripción')
    st.write('La función tanh también tiene forma de "S" sigmoidea.')
    st.markdown(r'$tanh(z)=\frac{e^{z} - e^{-z}}{e^{z} + e^{-z}}$')
    st.write('El rango de la función tanh está comprendido entre -1 y 1.')

    st.subheader('Plot')
    tanh_fig = plot_function(np.tanh, title='Función Hipérbolica Tangente')
    tanh_fig.add_annotation(x=7, y=1, text='<b>Saturation</b>', showarrow=True,
     font=dict(family="Montserrat", size=16, color="#1F8123"),
        align="center",arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor="#A835E1", ax=-20, ay=30,)
    tanh_fig.add_annotation(x=-7, y=-1, text='<b>Saturation</b>', showarrow=True,
     font=dict(family="Montserrat", size=16, color="#1F8123"),
        align="center",arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor="#A835E1", ax=0, ay=-30,)
    st.plotly_chart(tanh_fig)
    with st.expander('Plot Explanation'):
        st.write('- La función tanh se satura a medida que las entradas son mayores (positivas o negativas).')
        st.write('- Para valores positivos y negativos grandes, la función se aproxima asintóticamente a 1 y -1, respectivamente.')
        st.write('- Cuando la función se satura, su gradiente se aproxima mucho a cero, lo que ralentiza el aprendizaje.')
    
    st.subheader('Derivada')
    st.markdown(r'$tanh^{\prime}(z)= 1 - (tanh(z))^{2}$')
    st.text("")
    tanh_der_fig = plot_function_derivative(np.tanh, title='Derivada de la Función Tanh')
    st.plotly_chart(tanh_der_fig)
    with st.expander('Plot Explanation'):
        st.write('Observe que la derivada de la función tanh se aproxima mucho a cero para entradas positivas y negativas grandes.')
    
    st.subheader('Pros')
    st.write("1. La función tanh introduce no linealidad en la red, lo que le permite resolver problemas más complejos que las funciones de activación lineales.\n2. Es continua, diferenciable y tiene derivadas distintas de cero en todas partes.\n3. Como su valor de salida oscila entre -1 y 1, hace que la salida de cada capa esté más o menos centrada en 0 al principio del entrenamiento, lo que acelera la convergencia.")

    st.subheader('Contras')
    st.write("1. Sensibilidad limitada\nLa función tanh satura en la mayor parte de su dominio. Sólo es sensible a las entradas alrededor de su punto medio 0.")
    st.write("2. Gradientes de fuga en redes neuronales profundas - Debido a que la función tanh puede saturarse fácilmente con entradas grandes, su gradiente se acerca mucho a cero. Esto hace que los gradientes se hagan cada vez más pequeños a medida que la retropropagación avanza hacia las capas inferiores de la red. Finalmente, los pesos de las capas inferiores reciben actualizaciones muy pequeñas y nunca convergen a sus valores óptimos..")

    st.markdown("**Nota**: el problema del gradiente de fuga es menos grave con la función tanh porque tiene una media de 0 (en lugar de 0,5 como la función logística).).")

    

## Función unitaria lineal exponencial
if activation_function == 'Función unitaria lineal exponencial':
    st.title('Función unitaria lineal exponencial)')

    st.subheader('Descripción')
    st.markdown(r'$$ELU_{\alpha}(z)= \left\{\begin{array}{ll}z & z>0 \\{\alpha}(exp(z)-1) & z<=0 \\\end{array}\right.$$')

    st.write('La función unitaria lineal exponencial mostrará la entrada directamente si es positiva (función de identidad).')
    st.write('La salida de esta función es negativa para entradas negativas dependiendo del valor de α')

    st.subheader('Plot')

    with st.sidebar.form('leakage'):
        alpha = st.slider('α Value', 0.0, 1.0, 0.2)
        st.form_submit_button('Aplicar cambios')

    def elu(z, alpha=alpha):
        return np.where(z < 0, alpha * (np.exp(z) - 1), z)

    elu_fig = plot_function(elu, title="Función de unidad lineal exponencial (ELU)", alpha=alpha)
    st.plotly_chart(elu_fig)

    with st.expander('Plot Explanation'):
        st.write("- Este gráfico cambiará automáticamente cuando cambie el valor de α en el control deslizante de la barra lateral.")
        st.write('- la salida de la función nunca es un cero verdadero para entradas negativas,')
        st.write('- El valor de α suele fijarse en 1, o elegirse en el intervalo de [0,1 y 0,3].')
        st.write('- Si α es igual a 1, la función es suave en todas partes (optimización más fácil).')
    
    st.subheader('Derivada')
    st.markdown(r'$$ELU^{\prime}(z)= \left\{\begin{array}{ll}1 & z>0 \\{\alpha}*exp(z) & z<=0 \\\end{array}\right.$$')

    elu_der_fig = plot_function_derivative(elu, title='Derivative of ELU')
    st.plotly_chart(elu_der_fig)

    with st.expander('Plot Explanation'):
        st.write("- Este gráfico cambiará automáticamente cuando cambie el valor de α en el control deslizante de la barra lateral.")
        st.write("- La función tiene un gradiente distinto de cero para entradas negativas.")
    
    st.subheader('Pros')
    st.write("1. Aliviar el problema de la desaparición del gradiente")
    st.write("2. Evita el problema de los ReLUs muertos")
    st.write("3. Convergencia más rápida\n- Cuando el valor de α es igual a 1, la función es suave en todas partes, lo que acelera el descenso del gradiente.")
    st.write("4. Mejor rendimiento.\n- La función ELU supera a la mayoría de las demás variantes de ReLU con un tiempo de entrenamiento reducido.")

    st.subheader("Contras")
    st.write("1. Computacionalmente caro\n- Debido a que utiliza la función exponencial, el ELU es más lento de calcular que otras variantes de ReLU.")
    
## Derivada
if activation_function == 'Derivada Parcial':
    st.title('Derivada Parcial')
    st.write('la derivada parcial de una función de varias variables es la derivada con respecto a cada una de esas variables manteniendo las otras como constantes.')
    st.markdown('La derivada parcial de una función $f(x,y,\dots)$ con respecto a la variable $x$ se puede denotar de distintas maneras:')
    st.latex(r'''\frac{\partial f}{\partial x},\frac{\partial}{\partial x}f,D_1f,\partial_x f,f^\prime_x\text{ o } f_x.''')
    st.subheader('Definicion Formal')
    st.write('Análogamente a la derivada ordinaria (función de una variable real), la derivada parcial está definida como un límite.')
    st.markdown('Sea U es un subconjunto abierto de $\mathbb {R} ^{n}$ y $f:U\to \mathbb {R}$ una función, la derivada parcial de f en el punto $\mathbf {a} =(a_{1},\dots ,a_{n})\in U$ con respecto a la i-ésima variable $x_{i}$ se define como:')
    st.latex(r'''\frac{ \partial }{\partial x_i }f(\mathbf{a}) =
\lim_{h \rightarrow 0}{ 
f(a_1, \dots , a_{i-1}, a_i+h, a_{i+1}, \dots ,a_n) - 
f(a_1, \dots ,a_n) \over h }''')
    st.write('Si existe el límite')
    st.latex('La derivada parcial \frac {\partial f}{\partial x}')
    st.markdown('puede ser vista como otra función definida sobre $U$ y puede ser de nuevo derivada de forma parcial. Si todas las derivadas parciales mixtas de segundo orden son continuas en un punto, entonces $f$ es una función $C^{2}$ en ese punto; en tal caso, las derivadas parciales pueden ser intercambiadas por el teorema de Clairaut:')
    st.latex(r'''\frac{\partial^2f}{\partial x_i\partial x_j}=\frac{\partial^2f}{\partial x_j\partial x_i}''')
    st.subheader('Ejemplo')
    st.markdown('El volumen $V$ de un cono que depende de la altura del cono $h$ y su radio $r$, está dado por la fórmula')
    st.latex(r'''V(r,h) = \frac{\pi r^2h}{3}''')
    st.markdown('Las derivadas parciales de $V$ respecto a $r$ y $h$ son')
    st.latex(r'''\begin{align}
    \frac{\partial V}{\partial r}&=\frac{2\pi rh}{3} \\
    \frac{ \partial V}{\partial h}&=\frac{\pi r^2}{3}
\end{align}''')
    st.write('respectivamente, la primera de ellas representa la tasa a la que el volumen del cono cambia si el radio varía y su altura se mantiene constante, la segunda de ellas representa la tasa a la que el volumen cambia si la altura varía y su radio se mantiene constante.')
    st.markdown('La derivada total de $V$ con respecto a $r$ y $h$ son')
    st.latex(r'''\frac{ d V}{d r}=\underbrace{\frac{2\pi rh}{3}}_{\frac{\partial V}{\partial r}}+\underbrace{\frac{\pi r^2}{3}}_{\frac{\partial V}{\partial h}}\frac{dh}{dr} ''')
    st.write('y')
    st.latex(r'''frac{d V}{d h}=\underbrace{\frac{\pi r^2}{3}}_{\frac{\partial V}{\partial h}}+\underbrace{\frac{2\pi rh}{3}}_{\frac{\partial V}{\partial r}}\frac{dr}{dh} ''')
    st.write('respectivamente.')
    
## Multiplicadores de Lagrange
if activation_function == 'Multiplicadores de Lagrange':
    st.title('Multiplicadores de Lagrange')
    st.markdown('Consideremos un caso tridimensional. Supongamos que tenemos la función, $f(x, y)$, y queremos maximizarla, estando sujeta a la condición:')
    st.markdown('$g(x,y)=c$')
    st.markdown('donde $c$ es una constante. Podemos visualizar las curvas de nivel de $f$ dadas por')
    st.markdown('$f(x,y)=d_{n}$')
    st.markdown('para varios valores de $d_{n}$, y el contorno de g dado por $g(x, y) = c$. Supongamos que hablamos de la curva de nivel donde $g = c$. Entonces, en general, las curvas de nivel de $f$ y $g$ serán distintas, y la curva $g = c$ por lo general intersectará y cruzará muchos contornos de $f$. En general, moviéndose a través de la línea $g=c$ podemos incrementar o disminuir el valor de $f$. Sólo cuando $g=c$ (el contorno que estamos siguiendo) toca tangencialmente (no corta) una curva de nivel de $f$, no se incrementa o disminuye el valor de $f$. Esto ocurre en el extremo local restringido y en los puntos de inflexión restringidos de $f$.')
    st.markdown('Geométricamente traducimos la condición de tangencia diciendo que los gradientes de $f$ y $g$ son vectores paralelos en el máximo. Introduciendo un nuevo escalar, $λ$, resolvemos')
    st.latex(r'''\nabla</math>[''f''(''x'', ''y'') - λ (''g''(''x'', ''y'') − ''c'')] = 0
para λ ≠ 0.''')
    st.markdown('Una vez determinados los valores de $λ$, volvemos al número original de variables y así continuamos encontrando el extremo de la nueva ecuación no restringida')
    st.latex(r'''F(x,y)=f(x,y)-\lambda (g(x,y)-c)''')
    st.markdown('de forma tradicional. Eso es, $F(x,y)=f(x,y)$ para todo $(x, y)$ satisfaciendo la condición porque $g(x,y)-c$ es igual a cero en la restricción, pero los ceros de $∇F(x, y)$ están todos en $g(x,y)=c$.')
    st.subheader('El método de los multiplicadores de Lagrange')
    st.markdown('Sea $f(x)$ una función definida en un conjunto abierto $n-dimensional$ $\{x ∈ \mathbb R ^{n}\}$ Se definen $s$ restricciones $g_{k}(x) = 0,k=1,..., s$, y se observa que:')
    st.latex(r'''h(\mathbf x, \mathbf \lambda) = f + \sum_{k=1}^s \lambda_k g_k ''')
    st.markdown('Se procede a buscar un extremo para $h$')
    st.latex(r'''\frac{\partial h}{\partial x_i} = 0,''')
    st.write('lo que es equivalente a')
    st.latex(r'''\frac{\partial f}{\partial x_i} = -\sum_k^s \lambda_k \frac{\partial g_k}{\partial x_i}.''')
    st.subheader('Ejemplo')
    st.write('Supongamos que queremos encontrar la distribución probabilística discreta con máxima entropía. Entonces')
    st.latex(r'''f(p_1,p_2,\ldots,p_n) = -\sum_{k=1}^n p_k\log_2 p_k.''')
    st.latex(r'''g(p_1,p_2,\ldots,p_n)=\sum_{k=1}^n p_k=1.''')
    st.markdown('Podemos usar los multiplicadores de Lagrange para encontrar el punto de máxima entropía (dependiendo de las probabilidades). Para todo $k$ desde 1 hasta $n$, necesitamos')
    st.latex(r'''\frac{\partial}{\partial p_k}(f+\lambda (g-1))=0,''')
    st.write('lo que nos da')
    st.latex(r'''\frac{\partial}{\partial p_k}\left(-\sum_{k=1}^n p_k \log_2 p_k + \lambda\sum_{k=1}^n p_k - \lambda\right) = 0.''')
    st.markdown('Derivando estas $n$ ecuaciones obtenemos')
    st.latex(r'''-\left(\frac{1}{\ln 2}+\log_2 p_k \right) + \lambda = 0.''')
    st.markdown('Esto muestra que todo $p_{i}$ es igual (debido a que depende solamente de $λ$). Usando la restricción $∑_{k} p_{k} = 1$ encontramos .')
    st.latex(r'''p_k = \frac{1}{n}.''')
    st.write('Ésta (la distribución uniforme discreta) es la distribución con la mayor entropía.')
    
## Matriz Jacobiana
if activation_function == 'Matriz Jacobiana':
    st.title('Matriz Jacobiana')
    st.write('La matriz jacobiana es una matriz formada por las derivadas parciales de primer orden de una función. Una de las aplicaciones más interesantes de esta matriz es la posibilidad de aproximar linealmente a la función en un punto. En este sentido, el jacobiano representa la derivada de una función multivariable. Propiamente deberíamos hablar más que de matriz jacobiana, de diferencial jacobiana o aplicación lineal jacobiana ya que la forma de la matriz dependerá de la base o coordenadas elegidas. Es decir, dadas dos bases diferentes la aplicación lineal jacobiana tendrá componentes diferentes aún tratándose del mismo objeto matemático. La propiedad básica de la "matriz" jacobiana es la siguiente,')
    st.markdown('dada una aplicación cualquiera $\mathbf {F}:\mathbb{R} ^{n}\to \mathbb{R} ^{m}$ continua se dirá que es diferenciable si existe una aplicación lineal $λ$ tal que:')
    st.latex(r'''\lim_{\|\mathbf{x}-\mathbf{y}\|\to 0}
\frac{ \| (\mathbf{F}(\mathbf{x}) - \mathbf{F}(\mathbf{y})) -
\boldsymbol\lambda(\mathbf{x}-\mathbf{y}) \|}{\|\mathbf{x}-\mathbf{y}\|} = 0''')
    st.subheader('Determinante Jacobiano')
    st.markdown('Si $m=n$ entonces $\mathbf F$ es una función que va de $\mathbb {R} ^{n}$ a $\mathbb {R} ^{n}$')
    st.write('y en este caso la matriz jacobiana es una matriz cuadrada, por lo que podemos calcular su determinante, este es conocido como el determinante jacobiano.')
    st.markdown('El determinante jacobiano en un punto dado nos da información importante sobre el comportamiento de $\mathbf F$ cerca de ese punto. Una función continuamente diferenciable $\mathbf F$ es invertible cerca del punto $p \in \mathbb R$ si el determinante jacobiano en $p$ es no nulo. Este es el teorema de la función inversa.')
    st.subheader('Ejemplo')
    st.latex(r'''La matriz jacobiana de la función \mathbf{F}:\mathbb{R}^3\to\mathbb{R}^3 dada por \mathbf{F}(x_1,x_2,x_3)= (x_1,5x_3,4x_2^2 - 2x_3) cuyas funciones componentes son''')
    st.latex(r'''\begin{align}
    f_1&=x_1 \\
    f_2&=5x_3 \\
    f_3&=4x_2^2-2x_3
\end{align} ''')
    st.write('es')
    st.latex(r'''\mathbf{J}_{\mathbf{F}}(x_1,x_2,x_3)=
\begin{bmatrix}
    \cfrac{\partial f_1}{\partial x_1} & \cfrac{\partial f_1}{\partial x_2} & \cfrac{\partial f_1}{\partial x_3} \\
    \cfrac{\partial f_2}{\partial x_1} & \cfrac{\partial f_2}{\partial x_2} & \cfrac{\partial f_2}{\partial x_3} \\
    \cfrac{\partial f_3}{\partial x_1} & \cfrac{\partial f_3}{\partial x_2} & \cfrac{\partial f_3}{\partial x_3}
\end{bmatrix}
=
\begin{bmatrix}
    1 & 0 & 0 \\ 
    0 & 0 & 5 \\ 
    0 & 8x_2 & -2
\end{bmatrix}''')
    
## Bibliografia
if activation_function == 'Bibliografia Sugerida':
    st.title('Bibliografia Sugerida') 
    st.write('Apostol, T.M., Calculus, Volumen I. México: Ed. Reverté, 2001.')
    st.write('Courant, R., Differential and Integral Calculus, Volumen II. New York: J. Wiley, 1936.')
    st.write('Lang, S., Calculus of Several Variables. New York: Springer, 1987')
    st.write('Marsden, J., Tromba, A., Cálculo Vectorial. México: Addison-Wesley, Pearson Educación,1998.')
    st.write('Thomas, G.B., Finney, R.L., Cálculo: varias variables. México: Adisson-Wesley Longman,1999')
    st.write('Budak, B.M., Fomin, S.V., Multiple Integrals Field Theory and Series. Moscú: MIR,1973.')
    st.write('Spivak, M., Cálculo en Variedades. México: Ed. Reverté, 1987.')
    st.write('Spivak, M., Cálculo Infinitesimal (2a ed.). México: Ed Reverté, 1998.')
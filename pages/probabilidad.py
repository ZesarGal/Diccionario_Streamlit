import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from prob import dleyS
import plotly.express as px



from activations import derivative, logistic, relu, elu, selu_alpha, selu_scale, selu, plot_function, plot_function_derivative


st.markdown("# Probabilidad 🎉")
st.sidebar.markdown("# Probabilidad 🎉")

activation_function = st.selectbox('Elige una definición', ['None', 'Modelo clásico de probabilidad', 'Variable aleatoria discreta' ,'Densidad normal estándar'])

## Modelo laplaciano
if activation_function == 'Modelo clásico de probabilidad':

    st.header('Modelo clásico de probabilidad')

    st.subheader('Descripción')
    st.write('Supuestos para el modelo clásico de probabilidad.')
    st.write("- Espacio muestral $\Omega$ (conjunto de todos los posibles resultados de un experimento aleatorio) finito.")
    st.markdown(r'- Si $\omega\in \Omega$, entonces a $\{ \omega \}$ se le asigna una función $\mathbb{P}: \mathcal{P}(\Omega)\to [0,1]$')
    st.latex(r'''\mathbb{P}(\{ \omega \})=\frac{1}{\#\Omega}.''')   
    st.write("Supongamos que estamos interesados en el experimento aleatorio de lanzar dos dados honestos; esto es, la probabilidad de que salga...")
    st.markdown("El espacio muestral $\Omega$ del experimento de lanzar dos dados honestos, está compuesto de todas las parejas ordenadas $(i,j)$ tales que $1\le i,j\le 6$ (enteros). Esto es")
    st.latex(r'''\Omega=\{(i,j):1\le i,j\le 6\}=\{1,2,3,4,5,6\}\times \{1,2,3,4,5,6\}.''') 
    st.write(dleyS())
    st.subheader('Plot')
    fig = px.histogram(dleyS(), x="rango")
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    
    expander = st.expander("Explicación")
    expander.write("""
    Histograma que representa la elección, al azar, de 6 números en el lanzamiento de un dado 
""")
    expander.image("https://static.streamlit.io/examples/dice.jpg")
    
# Variable aleatoria discreta
if activation_function == 'Variable aleatoria discreta':
    st.header('Variable aleatoria discreta')

    st.subheader('Descripción')
    st.markdown('Una variable aleatoria, $X$, es una cantidad numérica generada por un experimento aleatorio.')
    st.write('Decimos que una variable aleatoria es discreta si su rango (el conjunto de sus valores) es numerable.')
    st.markdown("Sea $X$ una variable aleatoria discreta con rango $R_{X}=\{x_{1}, x_{2},\dots \}$. La función:")
    st.latex(r'''p_{X}(x_{k})=\mathbb{P}(X=x_{k}),''')   
    st.markdown('se llama función de masa de probabilidad asociada de $X$.')

    st.subheader('Ejemplo')
    st.markdown('Decimos que una variable aleatoria es de tipo binomial con parámetros $n$ y $p\in [0,1]$, si su función de masa de probabilidad está dada por:')
    st.latex(r'''P_X(k)={n \choose k}p^k(1-p)^{n-k}, \textrm{ for }k=0,1,2,...,n.''')
    st.latex(r'''
    \frac{\partial^{2}f}{\partial x_{i}\partial x_{j}}=\frac{\partial^{2}f}{\partial x_{j}\partial x_{i}}
    ''')
    
    st.title('Histograma de una variable aleatoria de tipo binomial')
    st.markdown('Simulamos mil realizaciones de una variable aleatoria binomial cuando variamos la probabilidad $p$')
    perc_heads = st.number_input(
    label='Probabilidad de éxito', min_value=0.0, max_value=1.0, value=.5)
    binom_dist = np.random.binomial(1, perc_heads, 1000)
    list_of_means = []
    for i in range(0, 1000):
        list_of_means.append(np.random.choice(binom_dist, 100, replace=True).mean())
    fig, ax = plt.subplots()
    ax = plt.hist(list_of_means)
    st.pyplot(fig)


    
    
# Densidad normal estándar    
if activation_function == 'Densidad normal estándar':

    st.header('Variable aleatoria normal estándar')

    st.subheader('Descripción')
    st.write('It is a sigmoid function with a characteristic "S"-shaped curve.')
    st.latex(r'''f(x)=\frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}.''') 
  
    st.subheader('Gráfica')
    st.text("")
    logistic_der_fig = plot_function_derivative(logistic, title='Dendidad normal estándar')
    st.plotly_chart(logistic_der_fig)
    with st.expander('Observación'):
        st.write('La densidad normal se aproxima a cero para valores muy grandes positiva y negativamente.')











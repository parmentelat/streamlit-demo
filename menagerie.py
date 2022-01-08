import streamlit as st
import pandas as pd

def demo(code, optional=""):
    line = code.split('\n')[0] if '\n' in code else code
    st.markdown(f"# `{line}`")
    if optional:
        st.write(optional)
    eval(code)



demo('''st.write("""# My first streamlit app

talks markdown""")''')

demo(r'st.latex(r"\forall x\in\mathbb{R}")')

names = 'Id,Surv,Class,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked'.split(',')

df = pd.read_csv('petit-titanic.csv', sep=';', names=names)
df = df.loc[:, ['Id', 'Class', 'Name', 'Age', 'Sex']]

demo("st.write(df)", "also st.dataframe(df)")

demo("st.table(df)")

import matplotlib.pyplot as plt
fig = plt.figure()
df['Age'].plot()

demo("st.write(fig)")

demo("st.line_chart(df['Age'])")

demo("""st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
''')
""")


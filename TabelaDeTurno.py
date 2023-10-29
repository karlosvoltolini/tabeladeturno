import streamlit as st
import pandas as pd
#from unidecode import unidecode

# from st_aggrid import AgGrid, GridOptionsBuilder
import calendar
import datetime


# Configurações da página


st.set_page_config(
    page_title="Tabela de Turno Repar",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

#esconde o menu do streamlit
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)


#reduz o espaçamento
padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)



# Funções para retornar o array com os valores da tabela de turno de cada grupo,
# o preenchimento do array deve ser feito copiando os valores da tabela de turno iniciando
# pelo indice_inicial e se repetindo de forma cíclica até o final do array
def preencher_array(indice_inicial):
    tabela = ['07x19','07x19','19x07','19x07','F','F','F','F','F','F']
    array = []
    for i in range(60):
        array.append(tabela[(indice_inicial+i)%10])
    return array



def TabelaGrupoA(data):

    aux = abs((data+datetime.timedelta(days=-5)-datetime.date(year=2023, month=4,day=12)).days)
    return preencher_array(aux%10)

def TabelaGrupoB(data):
    aux = abs((data+datetime.timedelta(days=-5)-datetime.date(year=2023, month=4,day=14)).days)
    return preencher_array(aux%10)

def TabelaGrupoC(data):
    aux = abs((data+datetime.timedelta(days=-5)-datetime.date(year=2023, month=4,day=16)).days)
    return preencher_array(aux%10)

def TabelaGrupoD(data):
    aux = abs((data+datetime.timedelta(days=-5)-datetime.date(year=2023, month=4,day=18)).days)
    return preencher_array(aux%10)

def TabelaGrupoE(data):
    aux = abs((data+datetime.timedelta(days=-5)-datetime.date(year=2023, month=5,day=20)).days)
    return preencher_array(aux%10)


def main():


    st.header("REPAR")

    st.subheader("Tabela de Turno 12x12 h")



    # Sidebar para seleção da data e grupo de turno
    st.sidebar.title("REPAR")
    st.sidebar.text('')
    selected_date = st.sidebar.date_input("Data:")
    selected_group = st.sidebar.selectbox("Grupo de Turno:", ["GRUPO A", "GRUPO B", "GRUPO C", "GRUPO D", "GRUPO E"])

    TabelaGrupoA(selected_date)

    # Função para substituir o nome do mês
    def traduzir_mes(mes):
        meses = {
            "January": "Janeiro",
            "February": "Fevereiro",
            "March": "Março",
            "April": "Abril",
            "May": "Maio",
            "June": "Junho",
            "July": "Julho",
            "August": "Agosto",
            "September": "Setembro",
            "October": "Outubro",
            "November": "Novembro",
            "December": "Dezembro"
        }
        return meses.get(mes, mes)

    # Função para substituir o nome do dia da semana
    def traduzir_dia_semana(dia_semana):
        dias_semana = {
            "Monday": "Segunda-feira",
            "Tuesday": "Terça-feira",
            "Wednesday": "Quarta-feira",
            "Thursday": "Quinta-feira",
            "Friday": "Sexta-feira",
            "Saturday": "Sábado",
            "Sunday": "Domingo"
        }
        return dias_semana.get(dia_semana, dia_semana)

    # Criação do DataFrame
    date_range = pd.date_range(selected_date + datetime.timedelta(days=-5), periods=60, freq='D')
    df = pd.DataFrame({
        'Data': date_range.strftime("%d/%m/%Y"),
        'Mês': date_range.strftime("%B").map(traduzir_mes),
        'Dia da Semana': date_range.strftime("%A").map(traduzir_dia_semana),
        'GRUPO A': TabelaGrupoA(selected_date),
        'GRUPO B': TabelaGrupoB(selected_date),
        'GRUPO C': TabelaGrupoC(selected_date),
        'GRUPO D': TabelaGrupoD(selected_date),
        'GRUPO E': TabelaGrupoE(selected_date)
    })

    # st.text(days_in_month)
    # st.text(date_range)

    # Destaca a coluna correspondente ao grupo de turno selecionado
    df_styled = df.style.set_properties(selected_group,**{'background-color': 'green'})



    # Destaca a linha correspondente à data selecionada
    def highlight_date(row):
        if row['Data'] == selected_date.strftime("%d/%m/%Y"):
            return ['background-color: orange'] * len(row)
        else:
            return [''] * len(row)

    df_styled = df_styled.apply(highlight_date, axis=1)


    # Exibe a tabela na área principal do aplicativo

    # CSS to inject contained in a string
    hide_dataframe_row_index = """
                    <style>
                    .row_heading.level0 {display:none}
                    .blank {display:none}
                    </style>
                    """

    # Inject CSS with Markdown
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

    # Boolean to resize the dataframe, stored as a session state variable

    # st.dataframe(df.set_index(df.columns[0]), height=2150, use_container_width=True)
    st.dataframe(df_styled, height=2150,use_container_width=True)



    # gb = GridOptionsBuilder.from_dataframe(df)
    # gb.configure_selection("single", pre_selected_rows=[10],)
    #
    # response = AgGrid(
    #     df,
    #     editable=True,
    #     gridOptions=gb.build(),
    #     data_return_mode="filtered_and_sorted",
    #     update_mode="no_update",
    #     fit_columns_on_grid_load=True,

# )



if __name__ == '__main__':
    main()

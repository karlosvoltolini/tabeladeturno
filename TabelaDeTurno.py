import streamlit as st
import pandas as pd
# from st_aggrid import AgGrid, GridOptionsBuilder
import calendar
import datetime

st.set_page_config(
    page_title="Tabela de Turno Repar",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

def preencher_array(indice_inicial):
    tabela = ['07','07','15','15','23','23','F','F','F','F']
    array = []
    for i in range(60):
        array.append(tabela[(10- indice_inicial + i) % len(tabela)])
    return array

def TabelaGrupoA(data):
    for i in range (60):
        aux = abs((data+datetime.timedelta(days=-5)-datetime.date(year=2023, month=4,day=22)).days)
    return preencher_array(aux)

def TabelaGrupoB(data):
    for i in range (60):
        aux = abs((data+datetime.timedelta(days=-5)-datetime.date(year=2023, month=4,day=24)).days)
    return preencher_array(aux)

def TabelaGrupoC(data):
    for i in range (60):
        aux = abs((data+datetime.timedelta(days=-5)-datetime.date(year=2023, month=4,day=26)).days)
    return preencher_array(aux)

def TabelaGrupoD(data):
    for i in range (60):
        aux = abs((data+datetime.timedelta(days=-5)-datetime.date(year=2023, month=4,day=28)).days)
    return preencher_array(aux)

def TabelaGrupoE(data):
    for i in range (60):
        aux = abs((data+datetime.timedelta(days=-5)-datetime.date(year=2023, month=5,day=1)).days)
    return preencher_array(aux)



def main():


    st.header("REPAR")

    st.subheader("Tabela de Turno 08 h")



    # Sidebar para seleção da data e grupo de turno
    st.sidebar.title("REPAR")
    st.sidebar.text('')
    selected_date = st.sidebar.date_input("Data:")
    selected_group = st.sidebar.selectbox("Grupo de Turno:", ["GRUPO A", "GRUPO B", "GRUPO C", "GRUPO D", "GRUPO E"])

    TabelaGrupoA(selected_date)

    # Criação do DataFrame

    date_range = pd.date_range(selected_date+datetime.timedelta(days=-5), periods=60, freq='D')
    df = pd.DataFrame({
        'Data': date_range.strftime("%d/%m/%Y"),
        'Mês' : date_range.month_name(),
        'Dia da Semana': date_range.day_name(),
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

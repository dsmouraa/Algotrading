import numpy as np
import pandas as pd
import yfinance as yf
import argparse
from datetime import datetime

TICKERS = ["A1MD34.SA", "A1UA34.SA", "A1ZN34.SA", "A2MC34.SA", "AALL34.SA", "AALR3.SA", "AAPL34.SA", "ABBV34.SA", "ABCB4.SA", "ABEV3.SA", "ADBE34.SA", "AERI3.SA", "AESB3.SA", "AGRO3.SA", "AGXY3.SA", "AIEC11.SA", "AIRB34.SA", "ALLD3.SA", "ALPA3.SA", "ALPA4.SA", "ALPK3.SA", "ALSO3.SA", "ALUP11.SA", "ALZR11.SA", "AMAR3.SA", "AMBP3.SA", "AMER3.SA", "AMZO34.SA", "ANIM3.SA", "APER3.SA",  "ARML3.SA", "ARMT34.SA", "ARRI11.SA", "ARZZ3.SA", "ASAI3.SA", "ATTB34.SA", "ATVI34.SA", "AURE3.SA", "AVGO34.SA", "AVLL3.SA", "AXPB34.SA", "AZUL4.SA", "B1IL34.SA", "B1NT34.SA", "B1PP34.SA", "B1SA34.SA", "B1TI34.SA", "B2YN34.SA", "B3SA3.SA", "BABA34.SA", "BAHI3.SA", "BARI11.SA", "BBAS3.SA", "BBDC3.SA", "BBDC4.SA", "BBPO11.SA", "BBSE3.SA", "BCIA11.SA", "BCRI11.SA", "BCSA34.SA", "BEEF3.SA", "BERK34.SA", "BGIP4.SA", "BIDU34.SA", "BIOM3.SA", "BKNG34.SA", "BLAK34.SA", "BLAU3.SA", "BMEB4.SA", "BMGB4.SA", "BMOB3.SA", "BOAC34.SA", "BOAS3.SA", "BOEI34.SA", "BONY34.SA", "BPAC11.SA", "BPAN4.SA", "BPFF11.SA", "BRAP3.SA", "BRAP4.SA", "BRBI11.SA", "BRCO11.SA", "BRCR11.SA", "BRFS3.SA", "BRIT3.SA", "BRKM3.SA", "BRKM5.SA", "BRML3.SA", "BRPR3.SA", "BRSR3.SA", "BRSR6.SA",  "BTCR11.SA", "BTLG11.SA", "C1CL34.SA", "C1SU34.SA", "C2OI34.SA",  "CAML3.SA", "CASH3.SA", "CATP34.SA", "CBAV3.SA", "CCRO3.SA", "CEAB3.SA", "CEDO3.SA", "CEDO4.SA", "CGRA3.SA", "CGRA4.SA", "CHCM34.SA", "CHVX34.SA", "CIEL3.SA", "CLSA3.SA", "CLSC3.SA", "CLSC4.SA", "CMCS34.SA", "CMIG3.SA", "CMIG4.SA", "CMIN3.SA", "COCA34.SA", "COCE5.SA", "COGN3.SA", "COLG34.SA", "COPH34.SA", "COWC34.SA", "CPFE3.SA",  "CPLE3.SA", "CPLE6.SA", "CRFB3.SA", "CSAN3.SA", "CSCO34.SA", "CSED3.SA", "CSMG3.SA", "CSNA3.SA", "CSUD3.SA", "CTGP34.SA", "CTNM4.SA", "CURY3.SA", "CVCB3.SA", "CXSE3.SA", "CYRE3.SA", "D1OC34.SA", "D1VN34.SA", "DASA3.SA", "DESK3.SA", "DEXP3.SA", "DEXP4.SA", "DIRR3.SA", "DISB34.SA", "DMMO3.SA", "DMVF3.SA", "DOTZ3.SA", "DXCO3.SA", "E1DU34.SA", "EAIN34.SA", "ECOR3.SA", "EGIE3.SA", "ELET3.SA", "ELET6.SA", "ELMD3.SA", "EMBR3.SA", "ENAT3.SA", "ENBR3.SA", "ENEV3.SA", "ENGI11.SA", "ENJU3.SA", "EQIX34.SA", "EQTL3.SA", "ESPA3.SA", "EUCA3.SA", "EUCA4.SA", "EVEN3.SA", "EXXO34.SA", "EZTC3.SA", "FCXO34.SA", "FDMO34.SA", "FESA3.SA", "FESA4.SA", "FHER3.SA", "FIQE3.SA", "FLRY3.SA", "FRAS3.SA", "GEOO34.SA", "GEPA4.SA",  "GFSA3.SA", "GGBR3.SA", "GGBR4.SA", "GGPS3.SA", "GMAT3.SA", "GMCO34.SA", "GOAU3.SA", "GOAU4.SA", "GOGL34.SA", "GOGL35.SA", "GOLL4.SA", "GRND3.SA", "GSGI34.SA", "GSHP3.SA", "GUAR3.SA", "HAPV3.SA", "HBOR3.SA", "HBRE3.SA", "HBSA3.SA", "HGLG11.SA",  "HOME34.SA",  "HYPE3.SA", "I1SR34.SA", "IFCM3.SA", "INTB3.SA", "IRBR3.SA", "ITLC34.SA", "ITSA3.SA", "ITSA4.SA", "ITUB3.SA", "ITUB4.SA", "JALL3.SA", "JBSS3.SA", "JDCO34.SA", "JHSF3.SA", "JNJB34.SA", "JPMC34.SA", "JSLG3.SA", "KEPL3.SA",  "KHCB34.SA", "KLBN11.SA", "KRSA3.SA", "L1YG34.SA", "LAND3.SA", "LAVV3.SA", "LEVE3.SA", "LIGT3.SA", "LJQQ3.SA", "LOGG3.SA", "LOGN3.SA", "LPSB3.SA", "LREN3.SA",  "LVTC3.SA", "LWSA3.SA", "M1NS34.SA", "M1RN34.SA", "M1TA34.SA", "MACY34.SA",  "MATD3.SA", "MBLY3.SA", "MCDC34.SA" , "MDIA3.SA", "MDNE3.SA", "MEAL3.SA", "MEGA3.SA", "MELI34.SA", "MELK3.SA", "MGLU3.SA", "MILS3.SA", "MLAS3.SA", "MMMC34.SA", "MODL3.SA", "MOSC34.SA", "MOVI3.SA", "MRCK34.SA", "MRFG3.SA", "MRVE3.SA", "MSBR34.SA", "MSCD34.SA", "MSFT34.SA", "MTRE3.SA", "MULT3.SA", "MUTC34.SA", "MYPK3.SA", "N1DA34.SA", "N1EM34.SA", "N1VO34.SA",  "NEOE3.SA", "NEXT34.SA", "NFLX34.SA", "NGRD3.SA", "NIKE34.SA", "NINJ3.SA", "NTCO3.SA", "NVDC34.SA", "ODPV3.SA", "OFSA3.SA", "ONCO3.SA", "OPCT3.SA", "ORCL34.SA", "ORVR3.SA", "OSXB3.SA", "OXYP34.SA", "P1DD34.SA", "P1LD34.SA", "PAGS34.SA", "PARD3.SA", "PCAR3.SA", "PDGR3.SA", "PDTC3.SA", "PEPB34.SA", "PETR3.SA", "PETR4.SA", "PETZ3.SA", "PFIZ34.SA", "PFRM3.SA", "PGCO34.SA", "PGMN3.SA", "PINE4.SA", "PLPL3.SA", "PMAM3.SA", "PNVL3.SA", "POMO3.SA", "POMO4.SA", "PORT3.SA", "POSI3.SA", "PRIO3.SA", "PRNR3.SA", "PSSA3.SA", "PTBL3.SA", "PTNT4.SA", "PYPL34.SA",  "QCOM34.SA", "QUAL3.SA", "R1KU34.SA", "R2BL34.SA", "RADL3.SA", "RAIL3.SA", "RAIZ4.SA", "RANI3.SA", "RAPT3.SA", "RAPT4.SA", "RCSL3.SA", "RDNI3.SA", "RDOR3.SA", "RECV3.SA", "RENT3.SA", "RIGG34.SA", "RIOT34.SA", "ROMI3.SA", "RRRP3.SA",  "RYTT34.SA", "S1BS34.SA", "S1PO34.SA", "S2EA34.SA", "S2HO34.SA", "S2QU34.SA", "S2TO34.SA",  "SANB11.SA", "SAPR11.SA", "SBFG3.SA", "SBSP3.SA", "SBUB34.SA", "SCAR3.SA", "SCHW34.SA", "SEER3.SA", "SEQL3.SA", "SGPS3.SA", "SHOW3.SA", "SIMH3.SA", "SIMN34.SA", "SMFT3.SA", "SMTO3.SA",  "SNEC34.SA",  "SOJA3.SA", "SOMA3.SA", "SQIA3.SA", "SSFO34.SA", "STBP3.SA", "SULA11.SA", "SUZB3.SA", "SYNE3.SA", "T1AL34.SA", "T1TW34.SA", "T2DH34.SA", "T2TD34.SA", "TAEE11.SA", "TASA3.SA", "TASA4.SA", "TCSA3.SA", "TECN3.SA", "TEND3.SA", "TEXA34.SA", "TFCO4.SA", "TGMA3.SA", "TGTB34.SA", "TIMS3.SA", "TLNC34.SA", "TMCO34.SA", "TMOS34.SA", "TOTS3.SA", "TPIS3.SA", "TRAD3.SA", "TRIS3.SA", "TRPL3.SA", "TRPL4.SA", "TSLA34.SA", "TSMC34.SA", "TTEN3.SA", "TUPY3.SA", "TXSA34.SA", "U1BE34.SA", "U2ST34.SA", "UCAS3.SA", "UGPA3.SA", "ULEV34.SA", "UNHH34.SA", "UNIP6.SA", "USIM3.SA", "USIM5.SA", "USSX34.SA", "VALE3.SA", "VAMO3.SA", "VBBR3.SA", "VERZ34.SA", "VIIA3.SA",  "VISA34.SA", "VITT3.SA", "VIVA3.SA", "VIVT3.SA", "VLID3.SA", "VULC3.SA", "VVEO3.SA", "WALM34.SA", "WEGE3.SA", "WEST3.SA", "WFCO34.SA", "WIZS3.SA","YDUQ3.SA", "Z1OM34.SA", "ZAMP3.SA"]

#### Parsear parâmetros do script rodando a partir da linha de comando, comentar este trecho para debug
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--ticker", help="ticker a ser analizado", default=TICKERS)
parser.add_argument("-p", "--parametro", 
                    help="valor do parâmetro a utilizar no formato p (exemplo: -0.5), padrão é um range [-0.5, -4.0]",
                    type=float,
                    default=np.arange(-0.5, -4.05, -0.1))
parser.add_argument("-d", "--data", 
                    help="data final para os cálculos no formato AAAA-MM-DD (exemplo: 2022-12-01), padrão hoje", 
                    default=datetime.now().strftime("%Y-%m-%d"))

args = parser.parse_args()

TICKERS = [args.ticker] if type(args.ticker) == str else args.ticker
PARAM = [args.parametro] if type(args.parametro) == float else args.parametro
DATA_FINAL = args.data
DATA_INICIO = DATA_FINAL.split('-')
DATA_INICIO[0] = str(int(DATA_INICIO[0])-2)
DATA_INICIO = '-'.join(DATA_INICIO)
####

#### Descomentar este trecho para debug no Spyder
# TICKER = "AMZN"
# PARAM = [-0.5]
# DATA_FINAL = "2021-12-31"
# DATA_INICIO = DATA_FINAL.split('-')
# DATA_INICIO[0] = str(int(DATA_INICIO[0])-2)
# DATA_INICIO = '-'.join(DATA_INICIO)
####

# Baixando os dados para 2 anos e filtrando para 365 pregões
resultados = []
for TICKER in TICKERS:
    print(f'Baixando dados ticker {TICKER}...')
    df = np.round(yf.download(TICKER, start=DATA_INICIO, end=DATA_FINAL)[-247:], 2)
    print('Dados baixados!')
    #print(df)
    # Para salvar o dataframe com as cotações, descomentar a linha:
     #df.to_csv(f'yfinance_{TICKER}.csv')
    
    for param in PARAM:
        parametro = float(param)

        # Encontra a entrada
        df['Entrada'] = np.round((df['Close'] * parametro)/100 + df['Close'], 2)
        
        # Resultado da entrada menos o valor de fechamento sem condição
        df['Resultado'] = np.round((df['Close'][1:].values - df['Entrada'][:-1].values)*100, 2).tolist() + [np.nan]
        
        # Executa a condição para verificar se a entrada no dia foi executada ou não
        mask = df['Entrada'][:-1].values >= df['Low'][1:].values
        mask = np.array(mask.tolist() + [False])
        df['Resultado'] = [res if b else 0 for res, b in zip(df['Resultado'].values, mask)]
        
        # Transforma o resultado em percentual
        df['Percentual'] = np.round(df['Resultado']/(df['Open']*100)*100,2)
        
        try:
            op_vencedoras = np.round(sum(df['Percentual'][158:] > 0) / sum(df['Percentual'][158:] != 0)*100, 2)
        except ZeroDivisionError:
            op_vencedoras = np.nan
        
        try:
            op_perdedoras = np.round(sum(df['Percentual'][158:] < 0) / sum(df['Percentual'][158:] != 0)*100, 2)
        except ZeroDivisionError:
            op_perdedoras = np.nan
        #df.to_csv(f'yfinance_{TICKER}.csv')    
        #print(df)
        
        # Formatação final e salvamento no disco
        resultado = pd.DataFrame({
            'Ticker': TICKER,
            'Parametro Utilizado': parametro,
            'Resultado 12 meses': df['Percentual'].sum(),
            'Resultado 3 meses': df['Percentual'][158:].sum(),
            'Total de operações': sum(df['Percentual'][158:] != 0),
            'Operações vencedoras': sum(df['Percentual'][158:] > 0),
            'Operações perdedoras': sum(df['Percentual'][158:] < 0),
            'Operações vencedoras(%)': op_vencedoras,
            'Operações Perdedoras(%)': op_perdedoras,
            'Maior DD da operação': min(df['Percentual'][158:]),
            'Maior ganho da operação': max(df['Percentual'][158:]),
            'Lucro Médio': np.mean(df['Percentual'][158:].values)
        }, index=[df.index[-1]])
        #print(resultado)
        # Acumula os resultados
        resultados.append(resultado)

# Concatena os resultados e salva
df_final = np.round(pd.concat(resultados), 2)
df_final.to_csv(f'resultados_{TICKER}.csv')
 

print('Finalizado!')

import pandas as pd
from src.analysis import kpis, grouped_profitability

def sample():
    return pd.DataFrame({
        'Faturamento':[100.,200.,50.], 'Lucro':[20.,-10.,5.], 'Order ID':[1,2,2],
        'Custo de Envio':[5.,10.,2.], 'Desconto':[0.1,0.2,0.0], 'Row ID':[1,2,3],
        'Foi devolvido?':[0,1,0], 'Categoria':['A','A','B']
    })

def test_kpis():
    k=kpis(sample())
    assert k['revenue']==350
    assert k['profit']==15
    assert k['orders']==2
    assert k['loss_rows']==1

def test_grouped_profitability():
    out=grouped_profitability(sample(),'Categoria').set_index('Categoria')
    assert out.loc['A','profit']==10
    assert out.loc['B','margin']==0.1

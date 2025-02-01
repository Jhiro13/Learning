import pandas as pd
if __name__=='__main__':
    d={'col1':[1,2], 'col2':[3,4]}
    df=pd.DataFrame(d)
    print(df)
"""si quiero compartir todas las librerias usadas hago esto
    pip freeze > requirements.txt
    pip install -r requirements.txt
    """
sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
restante = 19849.53

soma = sp + rj + mg + es + restante

percentual_sp = sp/soma * 100
percentual_rj = rj/soma * 100
percentual_mg = mg/soma * 100
percentual_es = es/soma * 100
percentual_restante = restante/soma * 100

print("SP: {:.2f}%\nRJ: {:.2f}%\nMG: {:.2f}%\nES: {:.2f}%\nOutros: {:.2f}%".format(percentual_sp, percentual_rj, percentual_mg, percentual_es, percentual_restante))


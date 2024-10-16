L, D = map(int,input().split()) # L representa comprimento da estrada e D a distancia entre os pedagios
K, P = map(int, input().split()) # K Custo por km percorrido P valor de cada pedagio
custoPorQuilometro = L*K
numeroPedagio = L//D
custoPedagio = numeroPedagio * P
custoTotal = custoPorQuilometro + custoPedagio
print(custoTotal)
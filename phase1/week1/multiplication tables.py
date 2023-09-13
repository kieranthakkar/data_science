def decor(func):
    def wrapper(table,final):
        top_decor = "="*3 +" "+str(table) +" "+ "TIMES TABLE" +" "+ "="*3
        print(top_decor)
        func(table,final)
        print("="*len(top_decor))
    return wrapper

@decor
def times_tables(table: int, final: int) -> None:
    for i in range(1,(final+1)):
        result = i * table
        print(f"{i} X {table} = {result}")
    return

times_tables(12,9)
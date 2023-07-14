import pandas
from cls.inc import inc

def create_hist(inp):
    df = pandas.read_csv(inp,delimiter=";",encoding="UTF8")
    df["Nazwa odbiorcy"].to_csv(r"import/out.csv")
    



def main():
    # l = inc("14/07/2023","AMS","5000")
    # print(l.who)
    #df=pandas.read_csv(r"import/hi.CSV",delimiter=";",encoding="UTF8")
    #print(df)
    create_hist(r"import/hi.CSV")

    


if __name__=="__main__":
    main()


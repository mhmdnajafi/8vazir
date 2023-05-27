from Genetic import Gentic
vazir=Gentic(7,500,0.8,0.2)
run_l,answer_l,time_l,answer=vazir.run(300)
print(answer)
path_save=vazir.folder(2)
vazir.chart(run_l,answer_l,'Run','True Answer',show=False,path=path_save,save=True)
vazir.chart(time_l[2:],answer_l,'Time','True Answer',show=False,path=path_save,save=True)
vazir.chart(time_l[2:],run_l,'Time','Run',show=False,path=path_save,save=True)